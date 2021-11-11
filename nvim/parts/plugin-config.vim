" netrw configuration 
let g:netrw_banner = 0
let g:netrw_altv = 1
let g:netrw_dirhistmax = 0
let g:netrw_liststyle = 3

" Debugger
let g:vimspector_enable_mappings='HUMAN'

" Fuzzy Finder
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'
let g:ctrlp_working_path_mode = 'ra'

set wildignore+=*/tmp/*,*.so,*.swp,*.zip,*.pyc,*.tar.gz    " MacOSX/Linux

let g:ctrlp_custom_ignore = 'venv'



" Vim-Slime
let g:slime_target = "tmux"
let g:slime_default_config = {"socket_name": get(split($TMUX, ","), 0), "target_pane": ":.1"}
