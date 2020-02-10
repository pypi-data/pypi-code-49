import re
from tld import parse_tld

from .Disassembler import Disassembler
from .Reassembler import Reassembler
from .PseudonymDataGenerator import PseudonymDataGenerator
from .DisassembleResult import DisassembleResult
from .Pseudonymizer import Pseudonymizer
from .HierarchicalPseudonymDataGenerator import (
    HierarchicalPseudonymDataGenerator
)

class DomainDisassembler(Disassembler):
    def __init__(self):
        self.__reassembler = DomainReassembler()
        self.__regex = re.compile(
            r"(?<![\w_-])(?<![\w-][./])" + \
            r"(?:(?!-)(?:xn--|_)?[\w-]{0,61}\w\.)+" + \
            r"(?!-)(?:xn--|_)?[\w-]{0,61}\w" + \
            r"(?![\w-])(?!\.[\w_])"
        )

    def get_regex(self):
        return self.__regex

    def disassemble(self, text):
        combined_tld = parse_tld("x://" + text)
        if combined_tld[0] is None or combined_tld[0] == "":
            return None
        data = tuple(reversed(text.split(".")))
        return DisassembleResult(data, self.__reassembler)

class DomainReassembler(Reassembler):
    def reassemble(self, flat_data):
        return ".".join(map(
            lambda index: "dom" + str(index),
            reversed(flat_data)
        ))

class DomainPseudonymizer(Pseudonymizer):
    def __init__(self):
        disassembler = DomainDisassembler()
        data_generator = HierarchicalPseudonymDataGenerator()
        super().__init__(disassembler, data_generator)
