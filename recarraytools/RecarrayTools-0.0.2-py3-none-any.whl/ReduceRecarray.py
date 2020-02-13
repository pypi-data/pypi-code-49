import numpy as np

def ReduceRecarray(data,fields):
	'''
	This routine will reduce the number of fields stored in a 
	numpy.recarray.
	
	Inputs:
		data: Original numpy.recarray
		fields: list of field names to preserve
		
	Returns
		numpy.recarray containing on the fields listed in 'fields'.
	'''
	
	dtype = []
	for f in fields:
		sh = data[f].shape
		if len(sh) == 1:
			dtype.append((f,str(data[f].dtype)))
		else:
			dtype.append((f,str(data[f].dtype),(sh[1],)))
	out = np.recarray(data.size,dtype=dtype)
	for f in fields:
		out[f] = np.copy(data[f])
	return out
