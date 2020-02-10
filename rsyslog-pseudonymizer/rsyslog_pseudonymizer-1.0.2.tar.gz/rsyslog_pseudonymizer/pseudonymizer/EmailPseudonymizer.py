import re

from .Pseudonymizer import Pseudonymizer
from .Disassembler import Disassembler
from .DisassembleResult import DisassembleResult
from .Reassembler import Reassembler
from .UsernameDomainPseudonymDataGenerator import (
    UsernameDomainPseudonymDataGenerator
)

class EmailDisassembler(Disassembler):
    def __init__(self, domain_regex_pattern):
        self.__reassembler = EmailReassembler()
        self.__regex = re.compile(
            r"(?<![\w_.+-])\w([\w_.+-]*\w+)?@(" + \
            domain_regex_pattern + \
            r"|\w[\w-]+\w+(?![\w-]))"
        )

    def get_regex(self):
        return self.__regex

    def disassemble(self, text):
        (username, domain) = text.split("@")
        return DisassembleResult((domain, username), self.__reassembler)

class EmailReassembler(Reassembler):
    def reassemble(self, flat_data):
        (domain, username) = flat_data
        return username + "@" + domain


class EmailPseudonymizer(Pseudonymizer):
    def __init__(self, domain_pseudonymizer, username_pseudonymizer_factory):
        disassembler = EmailDisassembler(
            domain_pseudonymizer.get_regex().pattern
        )
        data_generator = UsernameDomainPseudonymDataGenerator(
            domain_pseudonymizer,
            username_pseudonymizer_factory
        )
        super().__init__(disassembler, data_generator)
