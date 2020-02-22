from chibi.atlas import Chibi_atlas
from chibi_command import Command
import json

from chibi_command import Command_result


class Journal_status( Command_result ):
    def __init__( self, result, error, return_code ):
        super().__init__( result, error, return_code )
        pre_parse = self.result.split( '\n' )
        end_of_status = pre_parse.index( '' )

        status = pre_parse[ :end_of_status ]
        pre_messages = pre_parse[ end_of_status:]
        messages = [ json.loads( m ) for m in pre_messages if m ]

        self.result = Chibi_atlas(
            human=status, messages=messages )


class Systemctl( Command ):
    command = 'systemctl'
    captive = True
    kw = { '--output': 'json' }
    kw_format = "{key}={value}"
    result_class = Journal_status

    @classmethod
    def status( cls, *services ):
        result = cls( 'status', *services )()
        return result

    @classmethod
    def start( cls, *services ):
        result = cls( 'start', *services )()
        return result

    @classmethod
    def enable( cls, *services ):
        result = cls( 'enable', *services )()
        return result

    @classmethod
    def restart( cls, *services ):
        result = cls( 'restart', *services )()
        return result

    @classmethod
    def daemon_reload( cls, *services ):
        result = cls( 'daemon-reload', *services )()
        return result
