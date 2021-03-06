#!/usr/bin/env -S python3 -OO

#          Copyright Torge Matthies 2021.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

# pylint: disable=invalid-name,missing-module-docstring,missing-function-docstring
import socket
import re
import sys

# pylint: disable=line-too-long
PLAYER_COUNT_PATTERN = re.compile(r'\[\d{2}:\d{2}:\d{2}\] \[Server thread/INFO\]: There are (\d+) of a max of \d+ players online: .*$')


def receive_lines_bin(sock):
    carry = b''
    while True:
        try:
            data = sock.recv(4096)
        except socket.timeout:
            break
        lines = (carry + data).split(b'\n')
        carry = lines[-1]
        yield from lines[:-1]
        if not data:
            yield carry
            break


def receive_lines(sock):
    for line in receive_lines_bin(sock):
        try:
            yield line.decode()
        except UnicodeDecodeError:
            pass


def find_player_count(sock):
    for line in receive_lines(sock):
        match = PLAYER_COUNT_PATTERN.fullmatch(line)
        if match:
            return int(match.group(1))
    return None


def main(argv):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect('/run/minecraft-server/%s/console.socket' % (argv[1],))
        sock.settimeout(3.0)
        sock.send(b'list\n')
        player_count = find_player_count(sock)
        if player_count is None:
            return 1
        print(player_count)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv) or 0)
