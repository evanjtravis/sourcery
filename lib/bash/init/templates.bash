#!/bin/bash
# Install template files to their respective directories.
OPT="${1}"

function init
{
    # Base templates for DOT files in the home directory
    python ${SOURCERY_PYLIB}/link_dotfiles.py
}

function clean
{
}

function reset
{
    init
    clean
}

case "${OPT}" in
    "${INIT}") init
        ;;
    "${CLEAN}") clean
        ;;
    "${RESET}") reset
        ;;
    *) echo "Incorrect template.bash invocation."
esac

exit 0
