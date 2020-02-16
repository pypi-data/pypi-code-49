from socketserver import TCPServer, BaseRequestHandler 
import logging as lgg 
import json 
import os 


def PydtpError ( value ):
  return {'STATUS': 'ERROR', 'VALUE': value } 

def PydtpDict ( value ):
  return {'STATUS': 'DICT', 'VALUE': value } 

def PydtpString ( value ):
  return {'STATUS': 'STRING', 'VALUE': value } 



class Handler ( BaseRequestHandler ):
    def __init__ ( self, *args, **kwargs ):
        self.logger = lgg.getLogger ( 'PydtpServer' ) 
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

        return function ( *args, **kwargs ) 


    def info ( self ):
      dir_path = os.path.dirname(os.path.realpath(__file__))
      with open ( os.path.join ( dir_path, 'INFO' ) ) as f:
        string = f.read ()

      return PydtpString ("Printing server info: \n" + string[:-2]) 


    def get ( self, *variables ):
      from ImageDictionary import ImageDictionary 
      imdictLoader = ImageDictionary ( self.config.tmpfsdir, self.config.dbfile ) 
      image_dict = imdictLoader.load() 
      res = [ image_dict [k] for k in variables if k in image_dict.keys()]
      return PydtpString ( ", ".join (res) ) 

