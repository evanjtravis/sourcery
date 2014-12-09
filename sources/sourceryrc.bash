echo -e "\t${SOURCES}/sourceryrc.bash"

#####################################################################
# Environment Variables
#####################################################################

export MYLIBS=${SETTINGS}/mylibs
export MYPYLIB=${MYLIBS}/pylib
export MYBASHLIB=${MYLIBS}/bashlib

export PYLINTRC=${SETTINGS}/pylint/pylintrc
export PYTHONSTARTUP=${MYPYLIB}/pythonstartup.py

export PATH=$PATH:${SETTINGS}:${MYBASHLIB}
export PYTHONPATH=$PYTHONPATH:${MYPYLIB}

#####################################################################
# Aliases
#####################################################################

alias sourcery="source ~/.bash_profile"
alias sourcery.clean="make -f ${SETTINGS}/init/Makefile clean;sourcery"
alias sourcery.init="sourcery;make -f ${SETTINGS}/init/Makefile init;sourcery"
alias tosourcery="cd ${SETTINGS}"
alias vim="vim -u ${SETTINGS}/vim/vimrc"

#####################################################################
# Favorites
#####################################################################


