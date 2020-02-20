# A dictionary-like class that manages sets of acronyms.
from acronyms.json_codec import AcronymJSONEncoder
from acronyms.acronym import Acronym
import json


class Acronyms:
    """A dictionary-like class that manages sets of acronyms."""

    def __init__(self):
        self._values = {}

    @property
    def values(self):
        return self._values

    def set(self, acronym):
        self._values[acronym.key] = acronym

    def get(self, key):
        value = self._values.get(key)
        return value

    @staticmethod
    def Read(fileobject):
        """Read() generates an Acronyms object from the JSON data and returns it."""
        data = json.load(fileobject)
        acronyms = Acronyms()
        for key, value in data.items():
            acronym = Acronym()
            acronym.key = key
            acronym.shortform = value.get('shortform', '')
            acronym.longform = value.get('longform', '')
            acronyms.set(acronym)
        return acronyms

    def write(self, fileobject):
        data = AcronymJSONEncoder().encode(self.values)
        fileobject.write(data.encode('utf-8'))

    def merge(self, acronyms):
        """Merge the acronyms from the specified set into this one."""
        if not isinstance(acronyms, Acronyms):
            raise NotImplementedError("Only Acronyms objects can be merged.")
        for value in acronyms.values.values():
            self.set(value)

    def __eq__(self, other):
        if not isinstance(other, Acronyms):
            return NotImplemented
        return self.values == other.values
