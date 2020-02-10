import re
import ipaddress

from .Disassembler import Disassembler
from .Reassembler import Reassembler
from .DisassembleResult import DisassembleResult
from .Pseudonymizer import Pseudonymizer
from .HierarchicalPseudonymDataGenerator import (
    HierarchicalPseudonymDataGenerator
)

class IPv4Disassembler(Disassembler):
    def __init__(self):
        super().__init__()
        self.__reassembler = IPv4Reassembler()
        self.__regex = re.compile(
            r"(?<!\d\.)(?<!\d)(([01]?\d?\d|2(5[0-5]|[0-4]\d))\.){3}" + \
            r"([01]?\d?\d|2(5[0-5]|[0-4]\d))(?!\.\d)(?!\d)"
        )

    def get_regex(self):
        return self.__regex

    def disassemble(self, text):
        try:
            address = ipaddress.IPv4Address(text)
        except ValueError:
            return None
        return DisassembleResult(tuple(address.packed), self.__reassembler)

class IPv4Reassembler(Reassembler):
    def reassemble(self, flat_data):
        return ".".join(map(str, flat_data))

class IPv4Pseudonymizer(Pseudonymizer):
    def __init__(self, disassembler=None, data_generator=None):
        disassembler = disassembler or IPv4Disassembler()
        data_generator = data_generator or HierarchicalPseudonymDataGenerator()
        super().__init__(disassembler, data_generator)
