#!/bin/bash
# Script to set up everything for 'settings' git.
ERROR="FOOBAR"
OPT="${1}"
TEMPLATES_PROG=templates.bash

export INIT='--initialize'
export CLEAN='--clean'
export RESET='--reset'

function init
{
    if pip -V 2>/dev/null; then
        echo "Pip exists on system."
        pip -V # Print the current pip version
        # Install favorite python packages using pip
        get_pip_favorites.bash

    elif [ ! -d "/services" ]; then
        python ${SOURCERY_PYINIT}/get_get_pip.py
        chmod 755 ${SOURCERY_PYINIT}/get-pip.py
        python ${SOURCERY_PYINIT}/get-pip.py --user
    else
        echo "Pip cannot be installed (by you) on this system."
    fi

    # Install non-pip favorites
    favorites.bash
    
    # Install templates
    templates.bash ${INIT}

}

function clean
{
    ${TEMPLATES_PROG} ${CLEAN}
}

function reset
{
    ${TEMPLATES_PROG} ${INIT}
    clean
}

function message
{
    case "${1}" in
        "${INIT}") echo "Sourcery initialization complete."
            ;;
        "${CLEAN}") echo "Sourcery clean complete."
            ;;
        "${RESET}") echo "Sourcery reset complete."
            ;;
        *)
            echo "Incorrect invocation of sourcery."
            ;;
    esac
}

case "${OPT}" in
    "${INIT}") init
        ;;
    "${CLEAN}") clean
        ;;
    "${RESET}") reset
        ;;
    *) :
        ;;
esac

# Notify user of success/ failure.
message ${OPT}

# Success
exit 0
