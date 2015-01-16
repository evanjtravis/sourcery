NAME=$(uname -o)
export MYNAME

if [ "$NAME" == "Cygwin" ]; then
    MYNAME=$USER
else
    MYNAME=$TTY_OWNER
fi

export MYHOME=/home/${MYNAME}
export SOURCERY=${MYHOME}/sourcery
export SOURCES=${SOURCERY}/sources

echo -e "Sourced:\n\t${SOURCES}/profile.bash"

source ${SOURCES}/all/main

