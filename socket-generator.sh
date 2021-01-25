#!/bin/sh

#          Copyright Torge Matthies 2021.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

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
    ln -s "${out_dir}/minecraft-server-properties@.path" "${out_dir}/paths.target.wants/minecraft-server-properties@$1.path"
}

mkdir -p "${out_dir}/paths.target.wants"
cat >"${out_dir}/minecraft-server-properties@.path" <<EOF
[Unit]
Description=Minecraft server socket update path unit (%i)

[Path]
PathModified=/var/lib/minecraft-server/%i/server.properties
EOF
cat >"${out_dir}/minecraft-server-properties@.service" <<EOF
[Unit]
Description=Minecraft server socket update service (%i)
RefuseManualStart=yes

[Service]
ExecStart=/bin/sh -c '/usr/bin/systemctl daemon-reload; /usr/bin/systemctl is-active "minecraft-server@%i.socket" && /usr/bin/systemctl restart "minecraft-server@%i.socket"'
EOF
cat >"${out_dir}/minecraft-server-properties.path" <<EOF
[Unit]
Description=Minecraft server socket update path unit

[Path]
PathModified=/var/lib/minecraft-server
EOF
ln -s "${out_dir}/minecraft-server-properties.path" "${out_dir}/paths.target.wants/minecraft-server-properties.path"
cat >"${out_dir}/minecraft-server-properties.service" <<EOF
[Unit]
Description=Minecraft server socket update service
RefuseManualStart=yes

[Service]
ExecStart=/usr/bin/systemctl daemon-reload
EOF
for server_dir in /var/lib/minecraft-server/*; do
    [ -f "${server_dir}/server.properties" ] || continue
    process_server_dir "${server_dir##*/}"
done
