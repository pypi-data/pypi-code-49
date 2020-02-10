from .Disassembler import Disassembler
from .DisassembleResult import DisassembleResult

class IdentityDisassembler(Disassembler):
    def __init__(self, reassembler):
        self.__reassembler = reassembler

    def disassemble(self, text):
        return DisassembleResult(text, self.__reassembler)
