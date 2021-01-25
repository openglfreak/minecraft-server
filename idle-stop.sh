#!/bin/sh

idle_time="$(cat "/run/minecraft-server/$1/idle-time.txt" 2>/dev/null)" || idle_time=0
player_count="$(/usr/lib/minecraft-server/player-count.py "$1")" || player_count=1
if [ "${player_count}" -eq 0 ]; then
    idle_time="$((idle_time + 1))"
    if [ "${idle_time}" -ge 3 ]; then
        systemctl stop "minecraft-server@$1.service"
        systemctl start "minecraft-server@$1.socket"
    fi
fi
printf '%i\n' "${idle_time}" >"/run/minecraft-server/$1/idle-time.txt"
