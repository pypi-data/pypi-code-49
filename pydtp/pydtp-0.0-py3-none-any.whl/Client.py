import socket 
import json 
import logging as lgg 

class Client: 
  def __init__ ( self, address, maxlen = 1024, name = 'PyDTP Client' ):
    self.logger = lgg.getLogger (str(name)) 
    self.address = address
    self.maxlen = maxlen
    self.name  = name 


  def query ( self, function, args = None, kwargs = None ): 
    # Connect to the server
    self.logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.logger.debug('connecting to server')
    s.connect(self.address) 

    # Send the data
    data = {'FUNCTION': function, 'ARGS' : args or [], 'KWARGS': kwargs or {}} 
    message = bytes(json.dumps(data), encoding='utf-8') 
    self.logger.debug('sending data: "%s"', str(message, encoding='utf-8'))
    len_sent = s.send(message)

    # Receive a response
    self.logger.debug('waiting for response')
    response = str(s.recv(self.maxlen), encoding='utf-8') 
    self.logger.debug('response from server: "%s"', response)
    s.close() 

    ret = json.loads(response)

    if 'STATUS' not in ret.keys():
      raise KeyError ( 'Unexpectedly missing STATUS key in %s response'%self.name ) 

    if ret['STATUS'] == 'ERROR':
      raise RuntimeError ( ret['VALUE'] ) 

    if ret['STATUS'] == 'DICT':
      return ret['VALUE'] 

    if ret['STATUS'] == 'STRING':
      return str(ret['VALUE']) 
      

