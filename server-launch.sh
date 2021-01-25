#!/bin/sh

[ -r ./start.sh ] || exec java -jar server.jar --nogui
[ -x ./start.sh ] && exec ./start.sh
. ./start.sh
