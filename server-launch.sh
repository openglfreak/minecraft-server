#!/bin/sh

#          Copyright Torge Matthies 2021.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

[ -r ./start.sh ] || exec java -jar server.jar --nogui
[ -x ./start.sh ] && exec ./start.sh
. ./start.sh
