from unittest import TestCase

from chibi_command import lxc


class Test_lxc_attach( TestCase ):

    def test_add_double_dash_in_end( self ):
        preview = lxc.Attach.name( 'test' ).preview( 'some_command' )
        self.assertEqual( preview, 'lxc-attach -n test -- some_command' )
