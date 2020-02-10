from .Pseudonymizer import Pseudonymizer
from .IdentityDisassembler import IdentityDisassembler
from .Reassembler import Reassembler
from .IncrementingPseudonymDataGenerator import (
    IncrementingPseudonymDataGenerator
)

class UsernameReassembler(Reassembler):
    def reassemble(self, flat_data):
        return "user" + str(flat_data)

class UsernamePseudonymizer(Pseudonymizer):
    def __init__(self):
        reassembler = UsernameReassembler()
        disassembler = IdentityDisassembler(reassembler)
        data_generator = IncrementingPseudonymDataGenerator()
        super().__init__(disassembler, data_generator)
