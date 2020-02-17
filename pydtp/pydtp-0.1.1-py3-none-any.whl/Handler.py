from socketserver import TCPServer, BaseRequestHandler 
import numpy as np 
import logging as lgg 
import json 
import os 

from .converters import PydtpError, PydtpString, PydtpDict, PydtpArray, from_PyDTP, to_PyDTP

class Handler ( BaseRequestHandler ):
    def __init__ ( self, *args, **kwargs ):
        self.logger = lgg.getLogger ( 'PyDTP Handler' ) 
        super().__init__ ( *args, **kwargs ) 

    @property
    def forbiddenTokens ( self ):
      return ['', ' '] 

    def handle (self):
        data = self.request.recv(1024)
        remote = self.request.getpeername() 
        

        self.logger.info ( "Received a query of %d bytes from %s:%d", len(data), *remote ) 
        retvalue = self.parse ( data ) 
        self.request.send(bytes(json.dumps(retvalue), encoding='utf-8')) 


    def parse ( self, data ):
        try: 
          query = json.loads ( str ( data, encoding='utf-8' ) )
        except Exception as e:
          return PydtpError (str(e))

        try:
          function = getattr ( self, query['FUNCTION'] )
        except Exception as e: 
          if 'function' not in query:
            lgg.error ( "Malformed query" ) 
            return PydtpError ("Missing Function in query: %s" % str( query ) ) 
          else:
            lgg.error ( "Failed upon %s request", query['function'] ) 
            return PydtpError ("Failed upon %s request" % query['function'] ) 

        args = query['ARGS'] if 'ARGS' in query.keys() else [] 
        kwargs = query['KWARGS'] if 'KWARGS' in query.keys() else {}

        args = [from_PyDTP (a) for a in args] 
        kwargs = {k:from_PyDTP (v) for k,v in kwargs.items()}

        return to_PyDTP  ( function ( *args, **kwargs ) )



