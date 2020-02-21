from functools import reduce
from unittest import TestCase

from marshmallow import Schema, pre_load, INCLUDE, fields

from chibi_requests import Chibi_url, Response


class Four_chan_schema( Schema ):
    id = fields.Integer( data_key='no' )
    replies = fields.Integer()

    class Meta:
        unknown = INCLUDE

    @pre_load( pass_many=True )
    def pre_load( self, data, **kw ):
        threads = reduce(
            ( lambda x, y: x + y ),
            ( page[ 'threads' ] for page in data ) )
        return threads


class Response_threads( Response ):
    serializer = Four_chan_schema


threads = Chibi_url(
    'http://a.4cdn.org/{board}/threads.json',
    response_class=Response_threads ).format( board='w' )


class Test_four_chan_with_schema( TestCase ):
    def test_should_work( self ):
        response = threads.get()
        native = response.native
        self.assertIsInstance( native, list )
        self.assertTrue( native )
        for n in native:
            self.assertIn( 'id', n )
            self.assertIsInstance( n[ 'id' ], int )
            self.assertIn( 'replies', n )
            self.assertIsInstance( n[ 'replies' ], int )
