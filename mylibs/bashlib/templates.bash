#!/bin/bash
# Install template files to their respective directories.
COPY=${MYPYLIB}/copy_templates.py
TEMPLATES=${SETTINGS}/templates

MAIN_SRC=${TEMPLATES}/main
MAIN_DST=${HOME}

RPM_SRC=${TEMPLATES}/rpm
RPM_DST=${RPM_SRC}

OLD=.${USER}.temp
OPT="$1"

ERROR="FOOBAR"

function removeold
{
    while [ "$1" != "" ]; do
        DIRECTORY=$1
        echo "Removing $OLD files from $DIRECTORY"
        rm -f "$DIRECTORY"/*"$OLD" "$DIRECTORY"/.*"$OLD"
        shift
    done
}

function init
{
    # Base templates for DOT files in the home directory
    python ${COPY} -p . ${MAIN_SRC} ${MAIN_DST}
    # Base templates for makefiles when building an rpm
    python ${COPY} ${RPM_SRC} ${RPM_DST}
}

function clean
{
    removeold ${MAIN_DST} ${RPM_DST}
}

function reset
{
    init
    clean
}
if [ ! -z "$INIT" ]; then
    OPT=$ERROR
fi

case "$OPT" in
    "$INIT") init
        ;;
    "$CLEAN") clean
        ;;
    "$RESET") reset
        ;;
    *) echo "Incorrect template.bash invocation."
esac

exit 0
