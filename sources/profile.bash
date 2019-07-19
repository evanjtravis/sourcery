#!/usr/bin/bash

NAME=$(uname -o)
export SOURCERY_MYNAME

SOURCERY_MYNAME="ejtravis"

export SOURCERY_MYHOME=~/
export SOURCERY=${SOURCERY_MYHOME}/.sourcery
export SOURCERY_SOURCES=${SOURCERY}/sources
export SOURCERY_STATIC=${SOURCERY}/static
export SOURCERY_ERRORS=${SOURCERY}/errors

export PROMPT_COMMAND=""

echo -e "Sourced:\n\t${SOURCERY_SOURCES}/profile.bash"

source ${SOURCERY_SOURCES}/all/main

