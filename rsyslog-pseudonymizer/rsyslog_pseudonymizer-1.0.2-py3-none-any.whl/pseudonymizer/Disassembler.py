class Disassembler(object):
    def get_regex(self):
        raise NotImplementedError()

    def disassemble(self, text):
        raise NotImplementedError()
