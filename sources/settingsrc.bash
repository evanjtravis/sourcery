#####################################################################
# Environment Variables
#####################################################################

export SETTINGS=${HOME}/settings
export PYLINTRC=${SETTINGS}pylint/pylintrc
export MYPYLIB=${SETTINGS}/mypylib
export PYTHONSTARTUP=${MYPYLIB}/pythonstartup.py

export PATH=$PATH:${SETTINGS}
export PYTHONPATH=$PYTHONPATH:${MYPYLIB}

#####################################################################
# Aliases
#####################################################################

alias settings.clean="make -f ${SETTINGS}/init/Makefile clean"
alias settings.init="sourcee;make -f ${SETTINGS}/init/Makefile init;sourcee"
alias tosettings="cd $SETTINGS"

#####################################################################
# Favorites
#####################################################################


