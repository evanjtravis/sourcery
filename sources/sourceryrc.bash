echo -e "\t${SOURCES}/sourceryrc.bash"

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

# For user only.
if [ "$MYNAME" == "$USER" ]; then
    alias sourcery.clean="sourcery.bash ${CLEAN};sourcery"
    alias sourcery.init="sourcery;sourcery.bash ${INIT};sourcery"
    alias sourcery.reset="sourcery.bash ${RESET};sourcery"
    alias tosourcery="cd ${SETTINGS}"
fi

alias v="vim -u ${VIMRC}"

#####################################################################
# Favorites
#####################################################################


