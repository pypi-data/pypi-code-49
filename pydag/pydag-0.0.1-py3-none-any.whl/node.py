

class Node:
    def __init__(self, name):
        self.name = name
        self._previous = list()
        self._next = list()

    def __lshift__(self, node):
        if not isinstance(node, Node):
            name = node.__class__.__name__
            raise TypeError(f'Operator of type "{name}" is not a Node object')

        self._previous.append(node)
        node._next.append(self)
        return node

    def __rshift__(self, node):
        if not isinstance(node, Node):
            name = node.__class__.__name__
            raise TypeError(f'Operator of type "{name}" is not a Node object')

        node._previous.append(self)
        self._next.append(node)
        return node
