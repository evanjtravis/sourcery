#/bin/bash
# Script to download Vundle if it does not exist
if [ ! -d "/home/ejtravis/.vim/bundle/Vundle.vim" ]; then
    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
    vim +PluginInstall +qall
fi
