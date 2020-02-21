import ctypes,os.path
DLLS = map(ctypes.CDLL,[ 
	os.path.join(os.path.dirname(__file__),'libmosek64.so.9.1'),
	os.path.join(os.path.dirname(__file__),'libcilkrts.so.5') ])
