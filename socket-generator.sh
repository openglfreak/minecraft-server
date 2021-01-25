#!/bin/sh

server_ip="$(sed -n 's/^[[:space:]]*server-ip[[:space:]]*=[[:space:]]*\([0-9][0-9]*\)[[:space:]]*$/1/p' /var/lib/minecraft-server/server.properties 2>/dev/null)"
port="$(sed -n 's/^[[:space:]]*server-port[[:space:]]*=[[:space:]]*\([0-9][0-9]*\)[[:space:]]*$/\1/p' /var/lib/minecraft-server/server.properties 2>/dev/null)"
: "${port:=25565}"

if [ "x${server_ip:+set}" = 'xset' ]; then
    case "${server_ip}" in
        # IPv6
        *:*) _ip_port="[${server_ip}]:${port}";;
        # IPv4/Hostname
        *)   _ip_port="${server_ip}:${port}";;
    esac
else
    _ip_port="${port}"
fi

mkdir -p "$1/minecraft-server.socket.d"
cat >"$1/minecraft-server.socket.d/override.conf" <<EOF
[Socket]
ListenStream=
ListenStream=${_ip_port}
EOF
