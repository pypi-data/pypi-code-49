import re

from .Pseudonymizer import Pseudonymizer
from .Disassembler import Disassembler
from .DisassembleResult import DisassembleResult
from .Reassembler import Reassembler
from .PseudonymDataGenerator import PseudonymDataGenerator
from .PseudonymData import PseudonymData
from .UsernameDomainPseudonymDataGenerator import (
    UsernameDomainPseudonymDataGenerator
)

class MatrixIDDisassembler(Disassembler):
    def __init__(self, domain_regex_pattern):
        self.__reassembler = MatrixIDReassembler()
        self.__regex = re.compile(
            r"@[\w_](?:[\w_.+-]*[\w_]+)?:(" + \
            domain_regex_pattern + \
            r"|\w[\w-]+\w+(?![\w-]))"
        )

    def get_regex(self):
        return self.__regex

    def disassemble(self, text):
        (username_with_at, domain) = text.split(":")
        username = username_with_at[1:]
        return DisassembleResult((domain, username), self.__reassembler)

class MatrixIDReassembler(Reassembler):
    def reassemble(self, flat_data):
        (domain, username) = flat_data
        return "@" + username + ":" + domain


class MatrixIDPseudonymizer(Pseudonymizer):
    def __init__(self, domain_pseudonymizer, username_pseudonymizer_factory):
        disassembler = MatrixIDDisassembler(
            domain_pseudonymizer.get_regex().pattern
        )
        data_generator = UsernameDomainPseudonymDataGenerator(
            domain_pseudonymizer,
            username_pseudonymizer_factory
        )
        super().__init__(disassembler, data_generator)
