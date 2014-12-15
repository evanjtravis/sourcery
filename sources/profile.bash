export MYNAME=ejtravis
export MYHOME=/home/${MYNAME}

if [ "$MYNAME" != "$USER" ]; then
    export SETTINGS=${MYHOME}/sourcery
else
    export SETTINGS=~/sourcery
fi

export SOURCES=${SETTINGS}/sources
echo -e "Sourced:\n\t${SOURCES}/profile.bash"

source ${SOURCES}/bashrc

