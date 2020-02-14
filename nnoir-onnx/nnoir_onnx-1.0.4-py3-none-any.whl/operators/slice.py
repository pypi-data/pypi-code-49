from nnoir.functions import *
from .utils import *


class OpSlice(Op):

    def __init__(self, node):
        super(OpSlice, self).__init__(node)

    def to_function(self, env, constants):
        [x] = self.node.input
        [y] = self.node.output
        return [
            Reshape(
                [x],
                list(self.node.output),
                shape=list(map(int, env[y].shape))
            )
        ]


class OpMul(Op):

    def __init__(self, node):
        super(OpMul, self).__init__(node)

    def to_function(self, env, constants):
        [x, _] = self.node.input
        [y] = self.node.output
        return [
            Reshape(
                [x],
                list(self.node.output),
                shape=list(map(int, env[y].shape))
            )
        ]


class OpDiv(Op):

    def __init__(self, node):
        super(OpDiv, self).__init__(node)

    def to_function(self, env, constants):
        [x, _] = self.node.input
        [y] = self.node.output
        return [
            Reshape(
                [x],
                list(self.node.output),
                shape=list(map(int, env[y].shape))
            )
        ]


class OpExp(Op):

    def __init__(self, node):
        super(OpExp, self).__init__(node)

    def to_function(self, env, constants):
        [x] = self.node.input
        [y] = self.node.output
        return [
            Reshape(
                [x],
                list(self.node.output),
                shape=list(map(int, env[y].shape))
            )
        ]
