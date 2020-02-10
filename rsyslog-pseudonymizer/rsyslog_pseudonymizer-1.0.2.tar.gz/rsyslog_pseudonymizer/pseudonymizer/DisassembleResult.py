class DisassembleResult(object):
    def __init__(self, data, reassembler):
        self.data = data
        self.reassembler = reassembler

    def __eq__(self, other):
        if not isinstance(other, DisassembleResult):
            return NotImplemented
        return (
            self.data == other.data,
            self.reassembler == other.reassembler
        )
    
    def __hash__(self):
        return hash((self.data, self.reassembler))
