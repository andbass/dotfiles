
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'wlangstroth/vim-racket'

Plugin 'gmarik/Vundle.vim'
Plugin 'plasticboy/vim-markdown'

Plugin 'kien/ctrlp.vim'
Plugin 'rust-lang/rust.vim'

Plugin 'gkz/vim-ls'

Plugin 'cespare/vim-toml'
Plugin 'alvan/vim-closetag'

Plugin 'octol/vim-cpp-enhanced-highlight'

Plugin 'othree/html5.vim'
Plugin 'hail2u/vim-css3-syntax'
Plugin 'jelera/vim-javascript-syntax'
Plugin 'kchmck/vim-coffee-script'

Plugin 'editorconfig/editorconfig-vim'
Plugin 'Slava/vim-spacebars'

Plugin 'itchyny/lightline.vim'
Plugin 'Valloric/YouCompleteMe'

Plugin 'digitaltoad/vim-jade'

Plugin 'nanotech/jellybeans.vim'

call vundle#end()
filetype plugin indent on
