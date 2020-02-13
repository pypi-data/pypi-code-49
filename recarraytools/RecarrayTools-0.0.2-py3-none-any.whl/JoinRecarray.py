import numpy as np

def JoinRecarray(a1,a2):
	'''
	Simple routine to append two numpy.recarrays.
	
	Inputs:
		a1: numpy.recarray
		a2: numpy.recarray - must have same dtypes as a1!
		
	Returns:
		numpy.recarray where data from a1 is at the beginning and a2 at
		the end.
	'''
	dt = a1.dtype
	n1 = np.size(a1)
	n2 = np.size(a2)
	
	out = np.recarray(n1+n2,dtype=dt)
	out[0:n1] = a1
	out[n1:n1+n2] = a2
	
	return out
