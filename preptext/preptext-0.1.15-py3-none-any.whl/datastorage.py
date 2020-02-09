# -*- coding: utf-8 -*-
import pickle

from .entry import Entry


class DataStorage(object):
    """
    Defines a container to store a dataset composed of entries.

    Attributes:
        fields (dict[str, Field]): Contains the name of each column or field,
            together with the corresponding Field object. Two fields with the
            same Field object will have a shared vocabulary.
        entries (list(Entry)): The entries in this dataset.
    """
    def __init__(self, entries=None):
        self.fields = None
        self.entries = []
        if entries is not None:
            assert isinstance(entries, list), "entries must be list"
            for entry in entries:
                self.add_entry(entry)

    def filter_pred(self, pred):
        """
        pred (callable): Use only entries for which
            filter_pred(entries) is True.
        """
        entries = filter(pred, self.entries)
        self.entries = list(entries)

    def add_entry(self, entry):
        assert isinstance(entry, Entry), "entry must be instance of Entry"
        if self.fields is not None:
            assert entry.fields == self.fields, \
                "fields used in the entry must be the same as used" \
                "in DataStorage"
        else:
            self.fields = entry.fields
        self.entries.append(entry)

    def dump(self, file_name):
        with open(file_name, 'wb') as fwb:
            pickle.dump(self, fwb)

    @classmethod
    def load(cls, file_name):
        with open(file_name, 'rb') as frb:
            cls = pickle.load(frb)
        return cls

    def get_entry(self, i):
        return [getattr(self.entries[i], attr) for attr in self.fields]

    def get_array(self, i):
        return self.entries[i].get_array()

    def sort(self, key=None, reverse=False):
        self.entries.sort(key=key, reverse=reverse)

    def __getitem__(self, i):
        return self.entries[i]

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        for x in self.entries:
            yield x

    def __getattr__(self, attr):
        if attr in self.fields:
            for x in self.entries:
                yield getattr(x, attr)
        else:
            raise ValueError("{} is not in the fields".format(attr))

    def __getstate__(self):
        attrs = dict(self.__dict__)
        return attrs

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __eq__(self, other):
        if not isinstance(other, DataStorage):
            return False
        return self.__dict__ == other.__dict__
