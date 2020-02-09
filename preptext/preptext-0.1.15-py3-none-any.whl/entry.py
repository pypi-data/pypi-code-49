# -*- coding: utf-8 -*-
import six


class Entry(object):
    """
    Defines a single training or test entry.
    Stores each column of the entry as an attribute.
    """
    def __init__(self, single_data, fields):
        self.fields = fields
        for (name, field), data in zip(fields.items(), single_data):
            if field is not None:
                if isinstance(data, six.text_type):
                    data = data.rstrip("\n")
                if isinstance(name, tuple):
                    for n, f in zip(name, field):
                        setattr(self, n, f.preprocess(data))
                else:
                    setattr(self, name, field.preprocess(data))

    def get_array(self):
        arr = []
        for name, field in self.fields.items():
            if field is not None:
                arr.append(field.process(getattr(self, name)))
        return arr

    def __str__(self):
        # return str({attr: getattr(self, attr) for attr in self.fields})
        return str([getattr(self, attr) for attr in self.fields])

    def __repr__(self):
        # return str({attr: getattr(self, attr) for attr in self.fields})
        return str([getattr(self, attr) for attr in self.fields])

    def __getitem__(self, attr):
        return getattr(self, attr)

    def __iter__(self):
        return iter(self.fields)

    def __len__(self):
        return len(self.fields)

    def __eq__(self, other):
        if not isinstance(other, Entry):
            return False
        return self.__dict__ == other.__dict__

    def __getstate__(self):
        attrs = dict(self.__dict__)
        return attrs

    def __setstate__(self, state):
        self.__dict__.update(state)
