call plug#begin('~/.vim/plugged')
    
    " git 
    Plug 'tpope/vim-fugitive' " Git integration

    " status bar
    Plug 'vim-airline/vim-airline' " A cool status bar
    Plug 'vim-airline/vim-airline-themes' " Airline themes

    " syntax
    Plug 'sheerun/vim-polyglot'    

    " autocomplete
    Plug 'neoclide/coc.nvim', {'branch': 'release'} " Intellisense engine 

    " Themes
    Plug 'morhetz/gruvbox'

    " ide
    Plug 'kien/ctrlp.vim' " A fuzzy file finder
    Plug 'scrooloose/nerdcommenter' " Comment/Uncomment tool
    Plug 'tmhedberg/matchit' " Switch to the begining and the end of a block by pressing %
    Plug 'jiangmiao/auto-pairs' " Auto-close braces and scopes
    Plug 'jpalardy/vim-slime' "send text to console    

    " Debugger
    Plug 'puremourning/vimspector'

call plug#end()


