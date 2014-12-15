echo -e "\t${SOURCES}/all/sourceryrc.bash"

#####################################################################
# Environment Variables
#####################################################################
export MYLIBS=${SETTINGS}/mylibs
export MYPYLIB=${MYLIBS}/pylib
export MYBASHLIB=${MYLIBS}/bashlib

export PYTHONSTARTUP=${MYPYLIB}/pythonstartup.py

export PATH=$PATH:${SETTINGS}:${MYBASHLIB}
export PYTHONPATH=$PYTHONPATH:${MYPYLIB}

export VIMRC=${MYHOME}/.vimrc

export INIT='--initialize'
export CLEAN='--clean'
export RESET='--reset'
#####################################################################
# Aliases
#####################################################################

alias sourcery="source ${MYHOME}/.bash_profile"

