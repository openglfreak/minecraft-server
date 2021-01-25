#!/bin/sh
exec socat STDIO UNIX-CONNECT:"/run/minecraft-server-console-$1.socket"
