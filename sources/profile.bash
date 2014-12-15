export MYNAME=ejtravis
export MYHOME=/home/${MYNAME}

export SETTINGS=${MYHOME}/sourcery
export SOURCES=${SETTINGS}/sources

echo -e "Sourced:\n\t${SOURCES}/profile.bash"

source ${SOURCES}/all/bashrc

