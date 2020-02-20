from chibi_hybrid.chibi_hybrid import Chibi_hybrid

from chibi_command import Command


class Rsync( Command ):
    command = 'rsync'
    captive = False;

    @Chibi_hybrid
    def options( cls, *options ):
        return cls( *options )

    @options.instancemethod
    def options( self, *options ):
        return self.add_args( *options )

    @Chibi_hybrid
    def archive_mode( cls ):
        return cls.options( '-a' )

    @archive_mode.instancemethod
    def archive_mode( self ):
        return self.options( '-a' )

    @Chibi_hybrid
    def verbose( cls ):
        return cls.options( '-v' )

    @verbose.instancemethod
    def verbose( self ):
        return self.options( '-v' )

    @Chibi_hybrid
    def compress( cls ):
        return cls.options( '-z' )

    @compress.instancemethod
    def compress( self ):
        return self.options( '-z' )

    @Chibi_hybrid
    def human( cls ):
        return cls.options( '-h' )

    @human.instancemethod
    def human( self ):
        return self.options( '-h' )

    @Chibi_hybrid
    def progress( cls ):
        return cls.options( '--progress' )

    @progress.instancemethod
    def progress( self ):
        return self.options( '--progress' )
