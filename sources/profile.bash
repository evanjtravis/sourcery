NAME=$(uname -o)
export MYNAME

if [ "$NAME" == "Cygwin" ]; then
    MYNAME=$USER
else
    MYNAME=$TTY_OWNER
fi

export MYHOME=/home/${MYNAME}
export SETTINGS=${MYHOME}/sourcery
export SOURCES=${SETTINGS}/sources

echo -e "Sourced:\n\t${SOURCES}/profile.bash"

source ${SOURCES}/all/bashrc

