from nnoir.functions import *
from .utils import *

class OpMul(Op):

    def __init__(self, node):
        super(OpMul, self).__init__(node)

    def get_dummy_output(self, env):
        [a, b] = self.node.input
        return env[a] * env[b]

    def to_function(self, env, constants):
        [a, b] = self.node.input
        if a in constants and b not in constants:
            zero = constants[a].copy()
            zero[:] = 0
            return [Scale([b], list(self.node.output), axis=0, W=encode_ndarray(constants[a]), b=zero)]
        elif a not in constants and b in constants:
            zero = constants[b].copy()
            zero[:] = 0
            return [Scale([a], list(self.node.output), axis=0, W=encode_ndarray(constants[b]), b=zero)]
        elif a not in constants and b not in constants:
            return [Mul(list(self.node.input), list(self.node.output))]
        else:
            raise UnsupportedONNXOperation(self.node, 'bug! (unreachable here)')
