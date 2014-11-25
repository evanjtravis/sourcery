#####################################################################
# Paths
#####################################################################
umask 022

export SERVICE=crl-svcs
export PATH=$PATH:/services/$SERVICE/sdg/share/python/django/bin:/home/ejtravis/settings

export PYTHONPATH=/services/$SERVICE/sdg/share/python/django:/services/$SERVICE/share/python:/usr/lib/python2.6/site-packages:/usr/lib64/python2.6/site-packages:/home/ejtravis/settings/mypylib

export PYTHONSTARTUP=/home/ejtravis/settings/mypylib/pythonstartup.py
export PYLINTRC=/home/ejtravis/settings/pylint/.pylintrc
export SETTINGS=/home/ejtravis/settings/
export MYPYLIB=/home/ejtravis/settings/mypylib/

#####################################################################
# Settings
#####################################################################
export LS_COLORS='di=36'

#####################################################################
# Aliases
#####################################################################
alias c="clear"
alias cdd="cd ../"
alias ls="ls --color=auto"              # See LS_COLORS
alias test="python manage.py test"

pylintless() {
     pylint $1 | less
}
alias pylint="pylintless"

alias sourcee="source ~/.bash_profile"
alias vim="vim -u /home/ejtravis/settings/vim/.vimrc"
alias vi="vim"



