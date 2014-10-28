if [ -f $HOME/settings/bash/.bashrc ]; then
	source $HOME/settings/bash/.bashrc
fi

alias ls="ls --color=auto"
alias test="python manage.py test"
alias c="clear"

pylintless() {
    pylint $1 | less
}
alias pylint=pylintless

alias vim="vim -u /home/ejtravis/settings/vim/.vimrc"
