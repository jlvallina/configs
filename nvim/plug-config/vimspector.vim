" remap debugger
nnoremap <leader>dd :call vimspector#Launch()<CR>
nnoremap <leader>de :call vimspector#Reset()<CR>

nnoremap <leader>dcb :call vimspector#CleanLineBreakpoint()<CR>

nmap <leader>dl <Plug>VimspectorStepInto
nmap <leader>dj <Plug>VimspectorStepOver
nmap <leader>dk <Plug>VimspectorRestart
nmap <leader>do <Plug>VimspectorStepOut
nnoremap <leader>d<space> :call vimspector#Continue()

nmap <leader>drc <Plug>VimspectorRunToCursor
nmap <leader>dbp <Plug>VimspectorToggleBreakpoint 
nmap <leader>dcbp <Plug>VimspectorToggleConditionalBrakpoint
nmap <leader><space> <Plug>VimspectorBalloonEval


" for normal mode - the word under the cursor
nmap <Leader>di <Plug>VimspectorBalloonEval
" for visual mode, the visually selected text
xmap <Leader>di <Plug>VimspectorBalloonEval

" toggle the breakpoints window
nmap <Leader>db <Plug>VimspectorBreakpoints
