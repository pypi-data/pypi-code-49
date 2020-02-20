# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import itertools
import logging

__author__ = """dem4ply"""
__email__ = 'dem4ply@gmail.com'
__version__ = '0.0.3'

logger = logging.getLogger( 'chibi.command' )


class Command_result:
    def __init__( self, result, error, return_code ):
        self.result = result
        self.error = error
        self.return_code = return_code
        self.parse_result()

    def __str__( self ):
        if self:
            return self.result
        return self.error

    def __bool__( self ):
        return self.return_code == 0

    def parse_result( self ):
        pass


class Command:
    command = ''
    captive = False
    args = None
    kw = None
    kw_format = "{key} {value}"
    result_class = Command_result

    def __init__(
            self, *args, captive=None, command=None, result_class=None, **kw ):
        if captive is not None:
            self.captive = captive

        if result_class is not None:
            self.result_class = result_class

        if command is not None:
            self.command = command

        if not command and not self.command and args:
            self.command = args[0]
            args = args[1:]
        if self.args is None:
            self.args = tuple()
        else:
            self.args = tuple( self.args )
        self.args = ( *self.args, *args )

        if self.kw is None:
            self.kw = {}
        else:
            self.kw = self.kw.copy()
        self.kw.update( kw )

    @property
    def stdout( self ):
        if self.captive:
            return PIPE
        return None

    @property
    def stderr( self ):
        if self.captive:
            return PIPE
        return None

    def _build_proccess( self, *args, stdin=None, **kw ):
        if isinstance( stdin, str ):
            stdin = PIPE
        arguments = self.build_tuple( *args, **kw )
        logger.debug(
            'coamndo con argumentos "{}"'.format( str( arguments  ) ) )
        proc = Popen(
            arguments, stdin=stdin, stdout=self.stdout, stderr=self.stderr )
        return proc

    def build_tuple( self, *args, **kw ):
        return ( self.command, *self.build_kw( **kw ), *self.args, *args )

    def build_kw( self, **kw ):
        params = self.kw.copy()
        params.update( kw )
        return tuple(
            self.kw_format.format( key=k, value=v )
            for k, v in params.items() )

    def preview( self, *args, **kw ):
        tuples = self.build_tuple( *args, **kw )
        return " ".join( tuples )

    def run( self, *args, stdin=None, **kw ):
        logger.info( 'ejecutando "{}"'.format( self.preview( *args, **kw ) ) )
        proc = self._build_proccess( *args, stdin=stdin, **kw )
        if isinstance( stdin, str ):
            result, error = proc.communicate( stdin.encode() )
        else:
            result, error = proc.communicate()

        if result is not None:
            result = result.decode( 'utf-8' )
        if error is not None:
            error = error.decode( 'utf-8' )
        return self.result_class( result, error, proc.returncode )

    def __call__( self, *args, **kw ):
        return self.run( *args, **kw )

    def __hash__( self ):
        return hash( self.preview() )

    def __eq__( self, other ):
        if isinstance( other, Command ):
            return self.preview() == other.preview()
        else:
            raise NotImplementedError

    def __copy__( self ):
        args = tuple( *self.args )
        kw = self.kw.copy()
        new_command = type( self )(
            *args, command=self.command, captive=self.captive, **kw )
        return new_command

    def add_args( self, *new_args, **new_kw ):
        if new_args:
            self.args = tuple( itertools.chain( self.args, new_args ) )

        if new_kw:
            self.kw.update( new_kw )
