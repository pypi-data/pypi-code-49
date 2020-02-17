import socket 
import json 
import logging as lgg 

from .converters import PydtpError, PydtpString, PydtpDict, PydtpArray, to_array, from_PyDTP, to_PyDTP


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

    ## Convert arguments, if any 
    args = args or [] 
    kwargs = kwargs or {}

    args = [to_PyDTP (a) for a in args] 
    kwargs = {k:to_PyDTP (v) for k,v in kwargs.items()}

    # Send the data
    data = {'FUNCTION': function, 'ARGS' : args, 'KWARGS': kwargs} 
    message = bytes(json.dumps(data), encoding='utf-8') 
    self.logger.debug('sending data: "%s"', str(message, encoding='utf-8'))
    len_sent = s.send(message)

    # Receive a response
    self.logger.debug('waiting for response')
    response = str(s.recv(self.maxlen), encoding='utf-8') 
    self.logger.debug('response from server: "%s"', response)
    s.close() 

    ret = json.loads(response)

    return from_PyDTP ( ret )
