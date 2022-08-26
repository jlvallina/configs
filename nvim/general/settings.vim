let g:mapleader = "\<Space>"

set number relativenumber
set colorcolumn=81
set laststatus=0
set smartindent
set autoindent
set expandtab
set smarttab
set tabstop=4
set shiftwidth=4
set showtabline=4
set formatoptions-=cro
set hidden
set nowrap
set encoding=utf-8
set fileencoding=utf-8
set ruler
set mouse=a
set cursorline
set splitbelow
set splitright
set clipboard=unnamedplus
set background=dark
set autochdir
syntax enable
filetype on
filetype indent on
filetype plugin on

" Python format
au BufNewFile,BufRead *.py
    \ set tabstop=4
    \| set softtabstop=4
    \| set shiftwidth=4
    \| set textwidth=79
    \| set expandtab
    \| set autoindent
    \| set fileformat=unix


" Web format
au BufNewFile,BufRead *.js,*.html,*.css
    \ set tabstop=2
    \| set softtabstop=2
    \| set shiftwidth=2

