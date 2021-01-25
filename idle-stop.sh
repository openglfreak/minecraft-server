#!/bin/sh

idle_time="$(cat "/tmp/minecraft-server-idle-time-$1.txt" 2>/dev/null)" || idle_time=0
player_count="$(/usr/lib/minecraft-server/player-count.py "$1")" ||:
if [ "${player_count}" -eq 0 ]; then
    idle_time="$((idle_time + 1))"
    if [ "${idle_time}" -ge 3 ]; then
        systemctl stop "minecraft-server@$1.service"
        systemctl start "minecraft-server@$1.socket"
        idle_time=0
    fi
fi
umask 117
printf '%i\n' "${idle_time}" >"/tmp/minecraft-server-idle-time-$1.txt"
