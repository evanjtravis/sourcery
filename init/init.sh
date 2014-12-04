#/bin/bash
# Script to set up everything for 'settings' git.

if pip install -U pip; then
    echo "Pip upgraded."
else
    python $SETTINGS/init/get_get_pip.py
    python $SETTINGS/init/get-pip.py
fi
