from unittest import TestCase

from chibi_command import lxc


class Test_lxc_create( TestCase ):

    def test_name_return_instance( self ):
        c = lxc.Create()
        c2 = c.name( 'test' )
        self.assertIs( c, c2 )

    def test_template_return_instance( self ):
        c = lxc.Create()
        c2 = c.template( 'test' )
        self.assertIs( c, c2 )


class Test_lxc_attach( TestCase ):

    def test_add_double_dash_in_end( self ):
        preview = lxc.Attach.name( 'test' ).preview( 'some_command' )
        self.assertEqual( preview, 'lxc-attach -n test -- some_command' )

    def test_name_return_instance( self ):
        c = lxc.Attach()
        c2 = c.name( 'test' )
        self.assertIs( c, c2 )
