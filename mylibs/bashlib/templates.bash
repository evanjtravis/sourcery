# Install template files to their respective directories.
COPY=${MYPYLIB}/copy_templates.py
TEMPLATES=${SETTINGS}/templates

MAIN_SRC=${TEMPLATES}/main
MAIN_DST=${HOME}

RPM_SRC=${TEMPLATES}/rpm
RPM_DST=${RPM_SRC}

OLD=.${USER}.temp

function removeold
{
    while [ "$1" != "" ]; do
        DIRECTORY=$1
        echo "Removing $OLD files from $DIRECTORY"
        rm -f "$DIRECTORY"/*"$OLD" "$DIRECTORY"/.*"$OLD"
        shift
    done
}

if [ "$1" = "--initialize" ]; then
    # Base templates for DOT files in the home directory
    python ${COPY} -p . ${MAIN_SRC} ${MAIN_DST}
    # Base templates for makefiles when building an rpm
    python ${COPY} ${RPM_SRC} ${RPM_DST}
elif [ "$1" = "--clean" ]; then
    removeold ${MAIN_DST} ${RPM_DST}
else
    echo "Incorrect template.bash invocation."
fi

