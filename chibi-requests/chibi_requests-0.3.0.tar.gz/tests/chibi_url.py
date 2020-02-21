from chibi_requests import Chibi_url, Response
from chibi.atlas import Chibi_atlas
from unittest import TestCase
from unittest.mock import Mock, patch
from requests.auth import HTTPBasicAuth
from chibi.metaphors import Book


class Test_url( TestCase ):
    def setUp( self ):
        self.url = Chibi_url( "https://google.com" )


class Test_base_name( Test_url ):
    def test_base_name_should_return_the_last_part( self ):
        self.url = self.url + "1234567"
        base_name = self.url.base_name
        self.assertEqual( "1234567", base_name )


class Test_url_add( Test_url ):
    def test_can_add_parts( self ):
        self.assertIsInstance( self.url + "cosa", Chibi_url )
        self.assertEqual( "https://google.com/cosa", self.url + "cosa" )
        self.assertEqual(
            "https://google.com/cosa/cosa2", self.url + "cosa/cosa2" )
        self.assertEqual(
            "https://google.com/cosa/cosa2/cosa3",
            ( self.url + "cosa/cosa2" ) + "cosa3" )

    def test_add_a_query( self ):
        result = self.url + "?param1=value1"
        self.assertEqual( { 'param1': 'value1' }, result.params )
        self.assertEqual(
            { 'param1': 'value1', 'param2': 'value2' },
            ( result + "?param2=value2" ).params )

    def test_add_a_dict_should_add_the_query( self ):
        result = self.url + { 'param1': 'value1' }
        self.assertEqual( { 'param1': 'value1' }, result.params )

        result = result + { 'param2': 'value2' }
        self.assertEqual(
            { 'param1': 'value1', 'param2': 'value2' },
            result.params )

        result = self.url + { 'param1': 'value1', 'param2': 'value2' }
        self.assertEqual(
            { 'param1': 'value1', 'param2': 'value2' }, result.params )

    def test_add_a_book_should_add_the_query( self ):
        book = Book( page=20, page_size=10, total_elements=1000 )
        result = self.url + book
        offset = { k: str( v ) for k, v in book.offset.items() }
        self.assertEqual( result.params, offset )


class Test_add_mainteing_the_response_class( Test_url ):
    def setUp( self ):
        super().setUp()
        self.response_class = Mock
        self.url = Chibi_url(
            "https://google.com", response_class=self.response_class )

    def test_with_dict_should_mainteing_the_response_class( self ):
        result = self.url + { 'param1': 'value1' }
        self.assertEqual( result.response_class, self.response_class )

    def test_with_str_should_mainteing_the_response_class( self ):
        result = self.url + 'cosa'
        self.assertEqual( result.response_class, self.response_class )

    def test_with_query_should_mainteing_the_response_class( self ):
        result = self.url + "?param1=value1"
        self.assertEqual( result.response_class, self.response_class )

    def test_with_book_should_mainteing_the_response_class( self ):
        book = Book( page=20, page_size=10, total_elements=1000 )
        result = self.url + book
        self.assertEqual( result.response_class, self.response_class )


class Test_property( Test_url ):
    def test_host_should_return_host( self ):
        host = self.url.host
        self.assertEqual( "google.com", host )

    def test_schema_should_return_schema( self ):
        schema = self.url.schema
        self.assertEqual( "https", schema )


class Test_methods( Test_url ):
    def setUp( self ):
        self.url = Chibi_url( 'http://ifconfig.me' )

    def test_get( self ):
        response = self.url.get()
        self.assertTrue( response )
        self.assertIsInstance( response, Response )
        self.assertTrue( response.is_text )
        self.assertIsInstance( response.native, str )
        self.assertTrue( response.native )

    def test_post( self ):
        response = self.url.post()
        self.assertTrue( response )
        self.assertIsInstance( response, Response )
        self.assertTrue( response.is_json )
        self.assertIsInstance( response.native, Chibi_atlas )
        self.assertTrue( response.native )


class Test_meta( Test_url ):
    def test_meta_empty( self ):
        self.assertEqual( self.url.kw, {} )

    def test_meta_with_values( self ):
        url = Chibi_url(
            "https://www.google.com", cosa1="cosa1", cosa2="cosa2" )
        self.assertEqual( url.kw, { 'cosa1': 'cosa1', 'cosa2': 'cosa2' } )


class Test_str_functions( Test_url ):
    def setUp( self ):
        super().setUp()
        self.url = Chibi_url( 'http://a.4cdn.org/{board}/threads.json' )

    def test_format( self ):
        result = self.url.format( board='a' )
        self.assertIsInstance( result, Chibi_url )
        self.assertEqual( result, "http://a.4cdn.org/a/threads.json" )

    def test_format_with_params( self ):
        url = self.url + { 'param1': 'value1' }
        result = url.format( board='a' )
        self.assertIsInstance( result, Chibi_url )
        self.assertEqual(
            result, "http://a.4cdn.org/a/threads.json?param1=value1" )
        self.assertEqual(
            result.params, { 'param1': 'value1' } )

    def test_format_shoudl_add_meta( self ):
        url = self.url.format( board='a' )
        self.assertEqual( url.kw, { 'board': 'a' } )

    def test_format_should_conservate_meta( self ):
        url = Chibi_url( self.url, cosa1="cosa1" )
        url = url.format( board='a' )
        self.assertEqual( url.kw, { 'board': 'a', "cosa1": "cosa1" } )

    def test_format_should_conservate_response_class( self ):
        url = Chibi_url( self.url, response_class=Mock )
        url = url.format( board='a' )
        self.assertEqual( url.response_class, Mock )


class Test_auth( Test_url ):
    def setUp( self ):
        super().setUp()
        self.url = Chibi_url( 'http://a.4cdn.org/{board}/threads.json' )

    def test_when_add_a_auth_class_should_create_a_new_object( self ):
        url_other = self.url + HTTPBasicAuth( 'some_user', 'some_password' )
        self.assertIsNot( self.url, url_other )
        self.assertEqual( self.url, url_other )

    @patch( 'requests.get' )
    def test_should_send_the_auth_using_get( self, requests ):
        self.url += HTTPBasicAuth( 'some_user', 'some_password' )
        self.url.get()
        self.assertEqual( requests.call_args[1][ 'auth' ], self.url.auth )

    @patch( 'requests.post' )
    def test_should_send_the_auth_using_post( self, requests ):
        self.url += HTTPBasicAuth( 'some_user', 'some_password' )
        self.url.post()
        self.assertEqual( requests.call_args[1][ 'auth' ], self.url.auth )
