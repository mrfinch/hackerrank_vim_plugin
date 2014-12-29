function! SetQuesURL(arg1)
	let g:url_arg=a:arg1
	call CheckCode()
endfunction


function! CheckCode()

python << EOF

import vim,urllib2,sys
sys.path.append(vim.eval("expand('<sfile>:p:h')"))
import hackerrank 

h=hackerrank.run_code(vim.eval("g:url_arg"),vim.eval("expand ('%:p')"))


EOF

endfunction

