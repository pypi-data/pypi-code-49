class PseudonymizeResult(object):
    def __init__(self, formatted, deep_data):
        self.formatted = formatted
        self.deep_data = deep_data

    def __eq__(self, other):
        if not isinstance(other, PseudonymizeResult):
            return  NotImplemented
        return (
            self.formatted == other.formatted and
            self.deep_data == other.deep_data
        )

    def __hash__(self):
        return hash((self.formatted, self.deep_data))

    def __repr__(self):
        return str(self.__dict__)
