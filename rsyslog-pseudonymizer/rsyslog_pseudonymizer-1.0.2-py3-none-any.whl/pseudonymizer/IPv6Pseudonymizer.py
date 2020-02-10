import re
import ipaddress

from .Disassembler import Disassembler
from .Reassembler import Reassembler
from .DisassembleResult import DisassembleResult
from .Pseudonymizer import Pseudonymizer
from .HierarchicalPseudonymDataGenerator import (
    HierarchicalPseudonymDataGenerator
)

class IPv6Disassembler(Disassembler):
    def __init__(self):
        b = r"[A-Fa-f0-9]{1,4}"
        bf = r"(?:" + b + ":)"
        bb = r"(?::" + b + ")"
        self.__regex = re.compile(
            r"(?<![A-Fa-f0-9:])" + \
            r"(?:" + \
                # with IPv4 ending
                r"(?:" + \
                    r"::" + bf + r"{1,5}|" + \
                    bf + r"{1,5}:" + bf + r"{0,4}|" + \
                    bf + r"{6}" + \
                r")(?:" + \
                    r"(?:[01]?\d?\d|2(?:[0-4]\d|5[0-5]))\.){3}" + \
                    r"(?:[01]?\d?\d|2(?:[0-4]\d|5[0-5])" + \
                r")" + \
            r"|" + \
                # without IPv4 ending
                r"(?::|" + bf + r"{1,7})(?::|" + bb + r"{1,7})|" + \
                bf + r"{7}" + b + \
            r")" + \
            r"(?![A-Fa-f0-9])"
        )
        self.__lowercase_regex = re.compile(r"[a-f]")
        self.__ipv4_regex = re.compile(r"\.")

    def get_regex(self):
        return self.__regex

    def disassemble(self, text):
        try:
            address = ipaddress.IPv6Address(text)
        except ValueError:
            return None
        data = tuple(map(
            lambda block: int(block, 16),
            address.exploded.split(":")
        ))
        lowercase = bool(self.__lowercase_regex.search(text))
        ipv4_representation = bool(self.__ipv4_regex.search(text))
        return DisassembleResult(
            data,
            IPv6Reassembler(lowercase, ipv4_representation)
        )

class IPv6Reassembler(object):
    def __init__(self, lowercase, ipv4_representation):
        self.lowercase = lowercase
        self.ipv4_representation = ipv4_representation

    def reassemble(self, flat_data):
        integer = 0
        for i in range(8):
            if i < 6 or not self.ipv4_representation:
                integer = integer * 2**16 + flat_data[i]
            else:
                integer = integer * 2**16 + 0xFFFF
        compressed = ipaddress.IPv6Address(integer).compressed
        if self.ipv4_representation:
            assert compressed[-9:].lower() == "ffff:ffff", \
                "unexpected IPv6 format"
            first_6_blocks = compressed[:-9]
            ipv4 = ipaddress.IPv4Address(flat_data[6] * 2**16 + flat_data[7])
            lower = first_6_blocks + ipv4.compressed
        else:
            lower = compressed
        if self.lowercase:
            return lower
        return lower.upper()

    def __eq__(self, other):
        if not isinstance(other, IPv6Reassembler):
            return NotImplemented
        return (
            self.lowercase == other.lowercase and
            self.ipv4_representation == other.ipv4_representation
        )

    def __hash__(self):
        return hash((self.lowercase, self.ipv4_representation))

class IPv6Pseudonymizer(Pseudonymizer):
    def __init__(self):
        disassembler = IPv6Disassembler()
        data_generator = HierarchicalPseudonymDataGenerator()
        super().__init__(disassembler, data_generator)
