set nocompatible            " Set compatibility to Vim only.
set showmatch				" show matching brackets.
set ignorecase              " case insensitive matching
set hlsearch                " highlight search results
set tabstop=4               " number of columns occupied by a tab character
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set number                  " add line numbers
set cc=80                   " set an 80 column border for good coding style
set encoding=utf-8
filetype plugin indent on   " allows auto-indenting depending on file type
syntax on					" Turn on syntax highlighting.
filetype off 				" Helps force plug-ins to load correctly when it is turned back on below.
set wrap					" Automatically wrap text that extends beyond the screen length.
set modelines=0             " Turn off modelines

set nolist
set rnu


" Extra files
so ~/.config/nvim/parts/general.vim
so ~/.config/nvim/parts/plugins.vim
so ~/.config/nvim/parts/plugin-config.vim
so ~/.config/nvim/parts/maps.vim

" Colors 
colorscheme gruvbox
