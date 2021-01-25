#!/bin/sh

idle_time="$(cat /tmp/minecraft-server-idle-time.txt 2>/dev/null)" || idle_time=0
player_count="$(/usr/lib/minecraft-server/player-count.py)" ||:
if [ "${player_count}" -eq 0 ]; then
    idle_time="$((idle_time + 1))"
    if [ "${idle_time}" -eq 3 ]; then
        systemctl stop minecraft-server.service
        systemctl start minecraft-server.socket
        idle_time=0
    fi
fi
printf '%i\n' "${idle_time}" >/tmp/minecraft-server-idle-time.txt
