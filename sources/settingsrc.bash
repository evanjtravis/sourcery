echo -e "\t${SOURCES}/settingsrc.bash"

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

alias settings.clean="make -f ${SETTINGS}/init/Makefile clean"
alias settings.init="sourcee;make -f ${SETTINGS}/init/Makefile init;sourcee"
alias tosettings="cd ${SETTINGS}"
alias vim="vim -u ${SETTINGS}/vim/vimrc"

#####################################################################
# Favorites
#####################################################################


