import numpy as np
from ._InterpGaps import _InterpGaps

def InterpRecarrayFields(a,b,RefField='ut',InterpFields=[]):
	'''
	This function will attempt to intepolate the fields of 
	numpy.recarray a, such that they match a common reference field
	RefField (by default this is set to 'ut').
	
	Inputs:
		a: original numpy.recarray
		b: numpy.recarray to be interpolated onto.
		RefField: Reference field for interpolation, must be 
			monotonically increasing.
		InterpFields: List of field names to interpolate, must be 
			present in both a and b.
			
	Returns:
		numpy.recarray with interpolated fields.
	'''
	
	nf = np.size(InterpFields)
	adt = a.dtype.names
	bdt = b.dtype.names

	for i in range(0,nf):
		if InterpFields[i] in adt and InterpFields[i] in bdt:
			b[InterpFields[i]] = _InterpGaps(a[RefField],a[InterpFields[i]],b[RefField])
		
	return b
