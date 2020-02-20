from chibi_command import Command
from chibi_hybrid.chibi_hybrid import Chibi_hybrid


class Create( Command ):
    command = 'lxc-create'
    captive = False;

    @Chibi_hybrid
    def name( cls, name ):
        return cls( '-n', name )

    @name.instancemethod
    def name( self, name ):
        self.add_args( '-n', name )

    @Chibi_hybrid
    def template( cls, template ):
        return cls( '-t', template )

    @template.instancemethod
    def template( self, template ):
        self.add_args( '-t', template )


class Attach( Command ):
    command = 'lxc-attach'
    captive = False;

    @Chibi_hybrid
    def name( cls, name ):
        return cls( '-n', name )

    @name.instancemethod
    def name( self, name ):
        self.add_args( '-n', name )

    def build_tuple( self, *args, **kw ):
        return (
            self.command, *self.build_kw( **kw ), *self.args, '--', *args )
