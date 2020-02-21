from anytree import PreOrderIter, RenderTree, AnyNode
from psutil import Process


class ProcessTree:
    def __init__(self):
        self.root = self.build_node(Process(1))
        self.render_tree = RenderTree(self.root)

    def build_node(self, process):
        return AnyNode(
            process=process,
            children=list(map(
                lambda c: self.build_node(c),
                process.children()
            )),
            collapsed=False
        )

    def flatten(self):
        return list(PreOrderIter(self.root))

    @staticmethod
    def is_visible(node):
        """
        Node is hidden if any of its parents are collapsed
        """
        while node.parent:
            node = node.parent
            if node.collapsed:
                return False
        return True

    @staticmethod
    def prefix(node):
        return next(r for r in RenderTree(node.root) if r[2] == node)
