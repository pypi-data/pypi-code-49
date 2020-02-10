from .PseudonymizeResult import PseudonymizeResult


class Pseudonymizer(object):
    def __init__(self, disassembler, data_generator):
        self.disassembler = disassembler
        self.data_generator = data_generator

    def get_regex(self):
        return self.disassembler.get_regex()

    def get_pseudonym(self, text):
        disassemble_result = self.disassembler.disassemble(text)
        if disassemble_result is None:
            return None
        flat_original_data = disassemble_result.data
        reassembler = disassemble_result.reassembler
        pseudonym_data = self.data_generator.get_pseudonym_data(
            flat_original_data
        )
        if pseudonym_data is None:
            return None
        deep_pseudonym_data = pseudonym_data.deep
        flat_pseudonym_data = pseudonym_data.flat
        formatted = reassembler.reassemble(flat_pseudonym_data)
        return PseudonymizeResult(
            formatted,
            deep_pseudonym_data
        )
