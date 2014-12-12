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

export VIMRC=${SETTINGS}/vim/vimrc

export INIT='--initialize'
export CLEAN='--clean'
export RESET='--reset'
#####################################################################
# Aliases
#####################################################################

alias sourcery="source ~/.bash_profile"
alias sourcery.clean="sourcery.bash ${CLEAN};sourcery"
alias sourcery.init="sourcery;sourcery.bash ${INIT};sourcery"
alias sourcery.reset="sourcery.bash ${RESET};sourcery"
alias tosourcery="cd ${SETTINGS}"
alias vim="vim -u ${VIMRC}"

#####################################################################
# Favorites
#####################################################################


