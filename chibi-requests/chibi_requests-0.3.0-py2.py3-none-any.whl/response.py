from marshmallow import Schema

from chibi.atlas import Chibi_atlas_ignore_case
from chibi.atlas import _wrap


class Response:
    serializer = None

    def __init__( self, response, url ):
        self._response = response
        self.url = url

    @property
    def headers( self ):
        try:
            return self._headers
        except AttributeError:
            self._headers = Chibi_atlas_ignore_case( self._response.headers )
            return self._headers

    @property
    def body( self ):
        return self._response.text

    @property
    def native( self ):
        try:
            return self._native
        except AttributeError:
            self._native = self.parse_native()
            return self._native

    @property
    def pagination( self ):
        try:
            return self._pagination
        except AssertionError:
            raise NotImplementedError(
                "in the response {} is not implemented the pagination".format(
                    str( type( self ) )
                ) )

    @property
    def content_type( self ):
        return self.headers[ 'Content-Type' ]

    @property
    def is_json( self ):
        return 'application/json' in self.content_type

    @property
    def is_xml( self ):
        return self.content_type == 'application/xml'

    @property
    def is_text( self ):
        return 'text/plain' in self.content_type

    @property
    def status_code( self ):
        return self._response.status_code

    def parse_like_json( self ):
        json_result = self._response.json()
        return _wrap( json_result )

    def parse_like_xml( self ):
        raise NotImplementedError

    def parse_content_type( self ):
        if self.is_json:
            return self.parse_like_json()
        elif self.is_xml:
            return self.parse_like_xml()
        elif self.is_text:
            return self.body
        else:
            raise NotImplementedError

    def get_serializer( self ):
        if self.serializer is None:
            return None
        if isinstance( self.serializer, type ):
            serializer = self.serializer
            if issubclass( serializer, Schema ):
                return serializer
            else:
                raise NotImplementedError(
                    'No implementados los serializadores que '
                    'no son de marshmallow' )
        elif isinstance( self.serializer, Schema ):
            return type( self.serializer )
        else:
            raise NotImplementedError(
                'No implementados los serializadores que '
                'no son de marshmallow' )

    def parse_native( self ):
        parse = self.parse_content_type()
        serializer = self.get_serializer()
        if serializer:
            many = self.native_is_many
            parse = serializer().load( parse, many=many )
        return parse

    @property
    def native_is_many( self ):
        parse = self.parse_content_type()
        return isinstance( parse, list )
