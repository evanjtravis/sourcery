#/bin/bash
# Script to set up everything for 'settings' git.

if pip install -U pip; then
    echo "Pip upgraded."
elif [ ! -d "/services" ]; then
    python ${SETTINGS}/init/get_get_pip.py
    python ${SETTINGS}/init/get-pip.py --user
else
    echo "Cannot install pip on this system."
fi
