import numpy as np
import base64
import json 


def PydtpError ( value ):
  return {'STATUS': 'ERROR', 'VALUE': value } 

def PydtpDict ( value ):
  return {'STATUS': 'DICT', 'VALUE': value } 

def PydtpString ( value ):
  return {'STATUS': 'STRING', 'VALUE': value } 

def PydtpArray ( array ):
  if len(array.shape) == 0 and array.dtype in [np.int16, np.int32, np.int64]: 
    return {'STATUS': 'DICT', 'VALUE': int(array)} 
  elif len(array.shape) == 0 and array.dtype in [np.float16, np.float32, np.float64]: 
    return {'STATUS': 'DICT', 'VALUE': float(array)} 

  value = {
    'dtype': str(array.dtype), 
    'data' : str(base64.b64encode(array), encoding='utf-8'), 
    'shape': str(list(array.shape)) 
   }

  return {'STATUS': 'ARRAY', 'VALUE': value }


def to_array ( obj ):
    r = base64.decodebytes(bytes(obj['data'], encoding='utf-8'))
    q = np.frombuffer(r, dtype=obj['dtype'])
    return q.reshape ( json.loads (obj['shape']) ) 




def from_PyDTP ( obj ): 
  if isinstance(obj, (float, int, str)): return obj
  if not isinstance (obj, dict): 
    raise NotImplementedError ("Missing implementation for type %s" % type(obj)) 

  if 'STATUS' not in obj.keys(): return obj 
  
  status = obj ['STATUS'] 
  if status == 'ERROR':    raise RuntimeError (obj['VALUE'])
  elif status == 'STRING': return str ( obj['VALUE'] )
  elif status == 'DICT':   return obj['VALUE']
  elif status == 'ARRAY':  return to_array (obj['VALUE']) 
  elif status == 'LIST':   return obj['VALUE'] 
  elif status == 'NONE':   return None
  else:
    raise NotImplementedError ( "Missing implementation for obj: %s" % status ) 



def to_PyDTP (obj): 
  if isinstance (obj, (str, float, int)):
    obj = PydtpDict ( obj )
  elif isinstance (obj, (np.ndarray)):
    obj = PydtpArray (obj) 
  elif isinstance (obj, (list, tuple)):
    obj = {'STATUS': 'LIST', 'VALUE': obj }
  elif obj is None:
    obj = {'STATUS': 'NONE'}
      
  return obj


