class PseudonymData(object):
    def __init__(self, deep, flat):
        self.deep = deep
        self.flat = flat

    def __eq__(self, other):
        if not isinstance(other, PseudonymData):
            return NotImplemented
        return (
            self.deep == other.deep and
            self.flat == other.flat
        )

    def __hash__(self):
        return hash((self.deep, self.flat))

    def __repr__(self):
        return str(self.__dict__)
