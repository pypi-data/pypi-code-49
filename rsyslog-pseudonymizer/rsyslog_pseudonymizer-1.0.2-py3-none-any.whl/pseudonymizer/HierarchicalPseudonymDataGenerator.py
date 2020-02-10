from .PseudonymDataGenerator import PseudonymDataGenerator
from .PseudonymData import PseudonymData

class _HierarchyNode(object):
    def __init__(self, index_as_child):
        self.children_count = 0
        self.index_as_child = index_as_child

class HierarchicalPseudonymDataGenerator(object):
    def __init__(self):
        self.__pseudonyms = {
            (): _HierarchyNode(0)
        }

    def get_pseudonym_data(self, data):
        prev_entry = self.__pseudonyms[()]
        result = []
        for i in range(len(data)):
            curr_key = data[:i + 1]
            curr_entry = self.__pseudonyms.get(curr_key)
            if curr_entry is None:
                index_as_child = prev_entry.children_count
                prev_entry.children_count += 1
                curr_entry = _HierarchyNode(index_as_child)
                self.__pseudonyms[curr_key] = curr_entry
            else:
                index_as_child = curr_entry.index_as_child
            result.insert(i, index_as_child)
            prev_entry = curr_entry
        tuple_result = tuple(result)
        return PseudonymData(tuple_result, tuple_result)
