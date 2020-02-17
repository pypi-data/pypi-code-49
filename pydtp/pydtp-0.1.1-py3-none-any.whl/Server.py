import logging 
from socketserver import TCPServer
from threading import Thread 

class Server:
  def __init__ (self, address, handler, name='PyDTP Server'):
    self.name = name 
    self.logger = logging.getLogger ( name )
    self.server = TCPServer ( address, handler ) 
    self.thread = Thread ( target = self.server.serve_forever, daemon = True )

  def start (self):
    self.logger.debug ( "Server started" ) 
    return self.thread.start() 

  def stop (self):
    self.logger.debug ( "Server terminated" ) 
    self.server.socket.close() 
    
