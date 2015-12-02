#!/usr/bin/bash

NAME=$(uname -o)
export MYNAME

if [ "${NAME}" == "Cygwin" ]; then
    MYNAME=${USER}
else
    MYNAME=${TTY_OWNER}
fi

export MYHOME=/home/${MYNAME}
export SOURCERY=${MYHOME}/sourcery
export SOURCES=${SOURCERY}/sources
export STATIC=${SOURCERY}/static

# PROMPT_COMMAND is cleared here and added to later on.
export PROMPT_COMMAND=""

echo -e "Sourced:\n\t${SOURCES}/profile.bash"

source ${SOURCES}/all/main

