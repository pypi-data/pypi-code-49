from unittest import TestCase
import copy

from chibi.atlas import Chibi_atlas
from chibi_command import Command
from chibi_command import Command_result
from chibi_command.nix import Systemctl, Journal_status, Journal_show


class Test_systemctl( TestCase ):
    def test_status( self ):
        result = Systemctl.status( "unkown" )
        self.assertIsNotNone( result )
        self.assertFalse( result )

        result = Systemctl.status( "NetworkManager" )
        self.assertIsNotNone( result )
        self.assertTrue( result )
        self.assertIsInstance( result, Journal_status )

    def test_status_has_the_show_properites( self ):
        result = Systemctl.status( "NetworkManager" )
        self.assertIsNotNone( getattr( result, 'properties', None ) )
        self.assertIsInstance( result.properties, Chibi_atlas )

    def test_show( self ):
        result = Systemctl.show( "NetworkManager" )
        self.assertIsNotNone( result )
        self.assertTrue( result )
        self.assertIsInstance( result, Journal_show )
        self.assertIsInstance( result.result, Chibi_atlas )
