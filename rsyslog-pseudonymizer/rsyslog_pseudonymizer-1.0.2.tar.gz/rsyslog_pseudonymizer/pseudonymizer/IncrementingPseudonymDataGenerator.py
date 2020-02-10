from .PseudonymDataGenerator import PseudonymDataGenerator
from .PseudonymData import PseudonymData

class IncrementingPseudonymDataGenerator(PseudonymDataGenerator):
    def __init__(self):
        self.__names = {}

    def get_pseudonym_data(self, data):
        entry = self.__names.get(data)
        if entry is None:
            entry_count = len(self.__names)
            entry = PseudonymData(entry_count, entry_count)
            self.__names[data] = entry
        return entry
