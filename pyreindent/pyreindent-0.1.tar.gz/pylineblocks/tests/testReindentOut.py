# Test with
# $ ./bin/pyreindent.py -rt -f soft4 -t hard -o pylineblocks/tests/testReindentOut.py pylineblocks/tests/testReindentIn.py

def fun1():
	""" a docstring
	that contains
	newlines
	and trailing spaces
	- it should be reindented
	"""

	s = [ ''' a string # totally not a comment  
    literal    
    list		
    element 0''', """
    and now element 1
    """ ] # this definition should be reindented while preserving the strings
	# this comment should be reindented
	return s

print(fun1())
