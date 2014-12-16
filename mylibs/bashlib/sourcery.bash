#!/bin/bash
# Script to set up everything for 'settings' git.
TEMPLATES_PROG=templates.bash
ERROR="FOOBAR"
OPT="$1"

function init
{
    if pip install -U pip; then
        echo "Pip upgraded."

    elif [ ! -d "/services" ]; then
        python ${MYPYLIB}/get_get_pip.py
        chmod 755 ${MYPYLIB}/get-pip.py
        python ${MYPYLIB}/get-pip.py --user

    else
        :
    fi

    # Install favorite python packages.
    get_pip_favorites.bash

    # Install non-pip favorites
    favorites.bash
}

function clean
{
    :
}

function reset
{
    init
    clean
}

function message
{
    case "$1" in
        "$INIT") echo "Sourcery initialization complete."
            ;;
        "$CLEAN") echo "Sourcery clean complete."
            ;;
        "$RESET") echo "Sourcery reset complete."
            ;;
        *)
            echo "Incorrect invocation of sourcery."
            ;;
    esac
}
if [ "$USER" != "$MYNAME" ]; then
    OPT=$ERROR
fi


case "$OPT" in
    "$INIT") init
        ;;
    "$CLEAN") clean
        ;;
    "$RESET") reset
        ;;
    *) :
        ;;
esac

# Either install templates, clean old templates, or both, depending on
# invocation.
$TEMPLATES_PROG $OPT

# Notify user of success/ failure.
message $OPT

# Success
exit 0
