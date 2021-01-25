#!/usr/bin/env -S python3 -OO

#          Copyright Torge Matthies 2021.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

# pylint: disable=invalid-name,missing-module-docstring,missing-class-docstring,missing-function-docstring,raise-missing-from
import os
import select
import selectors
import socket
import sys
import threading
import traceback

import systemd.daemon

EXIT_ON_STDIN_CLOSE = True
EXIT_ON_STDOUT_CLOSE = True


# pylint: disable=too-many-instance-attributes
class SocketPipeProxy:
    __slots__ = ('connections', '_socket', '_inp_pipe', '_outp_pipe', '_selector',
                 '_inp_pipe_closed', '_outp_pipe_closed', '_selector_update_pipe',
                 '_run_running', '_members_lock')

    class _RunExitException(Exception):
        pass

    @property
    def socket(self):
        return self._socket

    @socket.setter
    def socket(self, value):
        with self._members_lock:
            self._selector.unregister(self._socket)
            self._socket = value
            self._selector.register(value, selectors.EVENT_READ, self._handle_accept)
        self._update_selector()

    @property
    def inp_pipe(self):
        return self._inp_pipe

    @inp_pipe.setter
    def inp_pipe(self, value):
        selector_modified = False
        with self._members_lock:
            if not self._inp_pipe_closed:
                self._selector.unregister(self._inp_pipe)
                selector_modified = True
            self._inp_pipe = value
            self._inp_pipe_closed = not value
            if not self._inp_pipe_closed:
                self._selector.register(value, selectors.EVENT_READ, self._handle_pipe_input)
                selector_modified = True
        if selector_modified:
            self._update_selector()

    @property
    def outp_pipe(self):
        return self._outp_pipe

    @outp_pipe.setter
    def outp_pipe(self, value):
        with self._members_lock:
            self._outp_pipe = value
            self._outp_pipe_closed = False

    # pylint: disable=redefined-outer-name
    def __init__(self, socket, inp_pipe, outp_pipe):
        self.connections = []
        self._socket = socket
        self._inp_pipe = inp_pipe
        self._outp_pipe = outp_pipe
        self._selector = selectors.DefaultSelector()
        self._inp_pipe_closed = not inp_pipe
        self._outp_pipe_closed = not outp_pipe
        self._selector_update_pipe = os.pipe()
        self._run_running = False
        self._members_lock = threading.Lock()

        self._selector.register(self._selector_update_pipe[0], selectors.EVENT_READ,
                                lambda x: x.read(1))
        self._selector.register(socket, selectors.EVENT_READ, self._handle_accept)
        if not self._inp_pipe_closed:
            self._selector.register(inp_pipe, selectors.EVENT_READ, self._handle_pipe_input)

    def close(self):
        if self._run_running:
            self._selector_update_pipe[1].write(b'\1')
        self._selector_update_pipe[0].close()
        self._selector_update_pipe[1].close()
        self._unregister_all_connections()

    def _update_selector(self):
        self._selector_update_pipe[1].write(b'\0')

    def _register_connection(self, conn):
        with self._members_lock:
            self.connections.append(conn)
            self._selector.register(conn, selectors.EVENT_READ, self._handle_connection_input)

    def register_connection(self, conn):
        self._register_connection(conn)
        self._update_selector()

    def _unregister_connection(self, conn, close=True):
        with self._members_lock:
            self._selector.unregister(conn)
            self.connections.remove(conn)
        if close:
            conn.close()

    def unregister_connection(self, conn, close=True):
        self._unregister_connection(conn, close)
        self._update_selector()

    def _unregister_all_connections(self, close=True):
        with self._members_lock:
            connections, self.connections = self.connections, []
            for conn in connections:
                self._selector.unregister(conn)
        if close:
            for conn in connections:
                conn.close()
        return connections

    def unregister_all_connections(self, close=True):
        if self._unregister_all_connections(close):
            self._update_selector()

    def _broadcast_to_connections(self, data):
        selector_modified = False
        for conn in self.connections[:]:
            try:
                conn.sendall(data)
            except ConnectionError:
                pass
            except OSError:
                traceback.print_exc()
            else:
                continue
            self._unregister_connection(conn)
            selector_modified = True
        return selector_modified

    def broadcast_to_connections(self, data):
        if self._broadcast_to_connections(data):
            self._update_selector()

    def _handle_update(self, pipe):
        opcode = pipe.read(1)
        if opcode == b'\0':
            return
        if opcode == b'\1':
            self._selector.close()
            raise SocketPipeProxy._RunExitException()

    @staticmethod
    def _socket_accept_all(sock):
        while True:
            try:
                rlist, _, _ = select.select((sock,), (), (), 0)
                if not rlist:
                    break
                yield sock.accept()[0]
            except BlockingIOError:
                break

    def _handle_accept(self, sock):
        for conn in SocketPipeProxy._socket_accept_all(sock):
            self._register_connection(conn)

    @staticmethod
    def _read_pipe_part(pipe):
        try:
            rlist, _, _ = select.select((pipe,), (), (), 0)
            if not rlist:
                return None
            # pipe.read blocks while os.read(pipe.fileno(), ...) doesn't.
            return os.read(pipe.fileno(), 4096)
        except BlockingIOError:
            return None
        except ConnectionError:
            pass
        except OSError:
            traceback.print_exc()
        return False

    @staticmethod
    def _read_pipe_full(pipe):
        while True:
            data = SocketPipeProxy._read_pipe_part(pipe)
            if data is None:
                break
            yield data
            if not data:
                break

    def _handle_pipe_input(self, pipe):
        for data in SocketPipeProxy._read_pipe_full(pipe):
            if not data:
                if EXIT_ON_STDIN_CLOSE:
                    raise SystemExit(0)
                self._inp_pipe_closed = True
                self._selector.unregister(pipe)
                break
            self._broadcast_to_connections(data)

    @staticmethod
    def _read_connection_part(conn):
        try:
            return conn.recv(4096, socket.MSG_DONTWAIT)
        except BlockingIOError:
            return None
        except ConnectionError:
            pass
        except OSError:
            traceback.print_exc()
        return False

    @staticmethod
    def _read_connection_full(conn):
        while True:
            data = SocketPipeProxy._read_connection_part(conn)
            if data is None:
                break
            yield data
            if not data:
                break

    def _write_outp_pipe(self, data):
        if self._outp_pipe_closed or not data:
            return
        try:
            i = 0
            while i < len(data):
                i += self._outp_pipe.write(data[i:])
            self._outp_pipe.flush()
        except BrokenPipeError:
            if EXIT_ON_STDOUT_CLOSE:
                raise SystemExit(0)
            self._outp_pipe_closed = True

    def _handle_connection_input(self, conn):
        for data in SocketPipeProxy._read_connection_full(conn):
            if not data:
                self._unregister_connection(conn)
                break
            self._write_outp_pipe(data)

    def run(self):
        with self._members_lock:
            if self._run_running:
                raise Exception('run() is already running on another thread')
            self._run_running = True
        try:
            while True:
                for key, _ in self._selector.select():
                    key.data(key.fileobj)
        except SocketPipeProxy._RunExitException:
            pass
        finally:
            with self._members_lock:
                self._run_running = False


def get_socket_from_systemd():
    fds = systemd.daemon.listen_fds()
    socket_fd = next(filter(systemd.daemon.is_socket, fds), None)
    if socket_fd is None:
        raise SystemExit(1)
    return socket.socket(fileno=socket_fd)


def main(_):
    with get_socket_from_systemd() as sock:
        SocketPipeProxy(sock, sys.stdin.buffer, sys.stdout.buffer).run()


if __name__ == '__main__':
    raise SystemExit(main(sys.argv) or 0)
