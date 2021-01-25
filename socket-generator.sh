#!/bin/sh

out_dir="$1"

process_server_dir() {
    server_dir="/var/lib/minecraft-server/$1"

    server_ip="$(sed -n 's/^[[:space:]]*server-ip[[:space:]]*=[[:space:]]*\([0-9][0-9]*\)[[:space:]]*$/1/p' "${server_dir}/server.properties" 2>/dev/null)"
    port="$(sed -n 's/^[[:space:]]*server-port[[:space:]]*=[[:space:]]*\([0-9][0-9]*\)[[:space:]]*$/\1/p' "${server_dir}/server.properties" 2>/dev/null)"

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

    mkdir -p "${out_dir}/minecraft-server@$1.socket.d"
    cat >"${out_dir}/minecraft-server@$1.socket.d/override.conf" <<EOF
[Socket]
ListenStream=
ListenStream=${_ip_port}
EOF
}

for server_dir in /var/lib/minecraft-server/*; do
    [ -d "${server_dir}" ] || continue
    process_server_dir "${server_dir##*/}"
done
