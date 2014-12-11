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
alias sourcery.clean="sourcery.bash --clean;sourcery"
alias sourcery.init="sourcery;sourcery.bash --initialize;sourcery"
alias sourcery.reset="sourcery.init; sourcery.clean"
alias tosourcery="cd ${SETTINGS}"
alias vim="vim -u ${SETTINGS}/vim/vimrc"

#####################################################################
# Favorites
#####################################################################


