#/bin/bash
# Script to set up everything for 'settings' git.
TEMPLATES_PROG=templates.bash

if [ "$1" = "--initialize" ]; then
    if pip install -U pip; then
        echo "Pip upgraded."

    elif [ ! -d "/services" ]; then
        python ${MYPYLIB}/get_get_pip.py
        python ${MYPYLIB}/get-pip.py --user

    else
        :
    fi

    # Install favorite python packages.
    get_pip_favorites.bash

    # Install non-pip favorites
    favorites.bash

    # Install template files to their respective directories.
    $TEMPLATES_PROG --initialize
    echo "Sourcery initialization complete."

elif [ "$1" = "--clean" ]; then
    $TEMPLATES_PROG --clean
    echo "Sourcery clean complete."

else
    echo "Incorrect sourcery.bash invocation."
    exit 1

fi

echo "----------> Done"
