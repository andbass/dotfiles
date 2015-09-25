
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'

" Rust and TOML
Plugin 'rust-lang/rust.vim'
Plugin 'cespare/vim-toml'

" GO
Plugin 'fatih/vim-go'

Plugin 'octol/vim-cpp-enhanced-highlight'

" Web dev
Plugin 'othree/html5.vim'
Plugin 'hail2u/vim-css3-syntax'
Plugin 'jelera/vim-javascript-syntax'
Plugin 'gkz/vim-ls'
Plugin 'kchmck/vim-coffee-script'
Plugin 'alvan/vim-closetag'
Plugin 'plasticboy/vim-markdown'

Plugin 'kien/ctrlp.vim'

Plugin 'editorconfig/editorconfig-vim'
Plugin 'Slava/vim-spacebars'

Plugin 'itchyny/lightline.vim'

Plugin 'digitaltoad/vim-jade'

" Awesome color scheme
Plugin 'nanotech/jellybeans.vim'

Plugin 'Valloric/YouCompleteMe'

call vundle#end()
filetype plugin indent on
