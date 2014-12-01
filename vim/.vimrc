""""""""""""""""""""""""""""""""""""""
" Install plugins for vim using VUNDLE
""""""""""""""""""""""""""""""""""""""
set nocompatible           " be iMproved, required
set nocp
filetype off                " required

" Set the runtime path to include Vundle, then initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Istalls pylint-mode
Plugin 'vim-scripts/pylint-mode'
" Configures pyLint-mode to run PyLint when saving
let g:PyLintCWindow = 1
let g:PyLintSigns = 1
let g:PyLintOnWrite = 1

" Installs Tagbar
Plugin 'majutsushi/tagbar'
" Use :TagBarToggle to turn on Tagbar

" Installs NERDTree
Plugin 'scrooloose/nerdtree'
" Use :NERDTreeToggle to turn on NERDTree

" End of Vim plugins, All plugins should be added before this line.
call vundle#end()           " required
filetype plugin indent on   " required

" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append '!' to update
" :PluginUpdate     - update plugins
" :PluginSearch foo - searches for foo; append '!' to refresh local cache
" :PluginClean      - confirms removal of unused plugs; append '!' to
"                     auto-approve removal
"""""""""""""""""""""""""""""""""
" End of Vundle plugin management
"""""""""""""""""""""""""""""""""

syntax on
set backspace=2
set background=light
set number nuw=6 columns=78		" line numbers

set tabstop=4		" size of a hard tabstop
set shiftwidth=4	" size of an indent
set smarttab		" make [tab] insert indents instead of tabs @ line start
set expandtab		" always use spaces instead of tab characters
set ruler           " view status line
" Useful Vim things from training manual
map <F5> :!python % " Press F5 to run the current Python file
set printoptions=number:y

highlight PreProc ctermfg=White  " Improve syntax highlighting, PreProc
highlight LineNr ctermfg=White   " Line number color
highlight Comment ctermfg=Red    " Comment Color syntax highlighting
highlight Constant ctermfg=2     " Green non-bold
highlight Type ctermfg=Magenta   " Type Color syntax highlighting
hi MatchParen cterm=none ctermbg=white ctermfg=blue " Improve paren match

"""""""""""""""""""""""""""""""
" PyLint
"""""""""""""""""""""""""""""""
" Make :make call PyLint
set makeprg=pylint\ --reports=n\ --output-format=parseable\ %:p
set errorformat=%f:%l:\ %m
" Use :cnext and :cprevious to page through results
