from nnoir.functions import *
from .utils import *


class OpConstant(Op):

    def __init__(self, node):
        super(OpConstant, self).__init__(node)

    def to_function(self, env, constants):
        [x, _] = self.node.input
        [y] = self.node.output
        return [
            Constant(
                [x],
                list(self.node.output),
                shape=list(map(int, env[y].shape))
            )
        ]
