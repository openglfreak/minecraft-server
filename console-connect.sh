#!/bin/sh
exec socat STDIO UNIX-CONNECT:"/run/minecraft-server/$1/console.socket"
