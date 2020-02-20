from chibi_command import Command
from chibi_hybrid.chibi_hybrid import Chibi_hybrid


class DD( Command ):
    command = 'dd'
    kw_format = "{key}={value}"
    kw = { 'bs': '1M', 'status': 'progress' }
    captive = False

    @Chibi_hybrid
    def input_file( cls, input_file ):
        return cls( **{ 'if': input_file } )

    @input_file.instancemethod
    def input_file( self, input_file ):
        self.add_args( **{ 'if': input_file } )
        return self

    @Chibi_hybrid
    def output_file( cls, output_file ):
        return cls( **{ 'of': output_file } )

    @output_file.instancemethod
    def output_file( self, output_file ):
        self.add_args( **{ 'of': output_file } )
        return self

