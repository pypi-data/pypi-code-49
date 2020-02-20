# Index manages uses of acronyms.


class Index:
    """Index manages uses of acronyms."""

    def __init__(self):
        self.uses = {}

    @property
    def uses(self):
        return self._uses

    @uses.setter
    def uses(self, values):
        self._uses = values

    def register(self, acronym):
        value = self.uses.get(acronym.key) or 0
        value = value+1
        self.uses[acronym.key] = value
        return value

    def occurences(self, key):
        return self.uses.get(key) or 0
