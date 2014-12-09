echo -e "\t${SOURCES}/sourceryrc.bash"

#####################################################################
# Environment Variables
#####################################################################

export PYLINTRC=${SETTINGS}/pylint/pylintrc
export MYPYLIB=${SETTINGS}/mypylib
export PYTHONSTARTUP=${MYPYLIB}/pythonstartup.py

export PATH=$PATH:${SETTINGS}
export PYTHONPATH=$PYTHONPATH:${MYPYLIB}

#####################################################################
# Aliases
#####################################################################

alias sourcery.clean="make -f ${SETTINGS}/init/Makefile clean;sourcery"
alias sourcery.init="sourcery;make -f ${SETTINGS}/init/Makefile init;sourcery"
alias tosource="cd ${SETTINGS}"
alias vim="vim -u ${SETTINGS}/vim/vimrc"

#####################################################################
# Favorites
#####################################################################


