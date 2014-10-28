if [ -f $HOME/settings/bash/.bashrc ]; then
	source $HOME/settings/bash/.bashrc
fi

alias django-admin="/services/sdg-sandbox/share/python/django16/django/bin/django-admin.py"

alias ls="ls --color=auto --hide=*.pyc"
alias test="python manage.py test"
alias c="clear"

pylintless() {
    pylint $1 | less
}
alias pylint=pylintless

alias vim="vim -u /home/ejtravis/settings/vim/.vimrc"
