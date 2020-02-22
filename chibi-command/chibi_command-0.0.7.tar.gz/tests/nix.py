from unittest import TestCase
import copy

from chibi_command import Command
from chibi_command import Command_result
from chibi_command.nix import Systemctl, Journal_status


class Test_systemctl( TestCase ):
    def test_status( self ):
        result = Systemctl.status( "unkown" )
        self.assertIsNotNone( result )
        self.assertFalse( result )

        result = Systemctl.status( "NetworkManager" )
        self.assertIsNotNone( result )
        self.assertTrue( result )
        self.assertIsInstance( result, Journal_status )
