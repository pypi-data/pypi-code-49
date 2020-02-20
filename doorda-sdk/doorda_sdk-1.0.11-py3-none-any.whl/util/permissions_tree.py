class Node(object):
    def __init__(self, value, children=None):
        if not children:
            children = []
        self.value = value
        self.children = children

    def __str__(self, level=0):
        if not self.value:
            ret = (
                "| Catalogs\t| Schemas\t| Table Names\t\n-----------"
                "------------------------------------------------\n"
            )
        else:
            ret = (
                "|\t\t\t" * (level - 1)
                + "|-- " * (int(level / level) if level > 0 else level)
                + str(self.value)
                + "\n"
            )
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return "<DoordaHost permissions representation>"
