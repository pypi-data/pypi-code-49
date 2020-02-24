import json
from chibi.file import Chibi_file
from chibi.atlas import _wrap


__all__ = [ 'Chibi_yaml' ]


class Chibi_json( Chibi_file ):
    def read( self ):
        self.reread()
        return _wrap( json.load( self.file ) )

    def write( self, data, is_safe=False ):
        super().write( json.dumps( data ) )
