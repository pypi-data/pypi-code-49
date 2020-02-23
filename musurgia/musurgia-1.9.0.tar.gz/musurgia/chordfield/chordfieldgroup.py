from musicscore.musicstream.streamvoice import SimpleFormat

from musurgia.chordfield import ChordField


class ChordFieldGroup(object):
    def __init__(self, *fields):
        self._fields = []
        self.fields = fields
        self._current_field = None
        self._field_iter = None
        self._simple_format = None

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, values):
        self._fields = []
        for value in values:
            self.add_field(value)

    def add_field(self, field):
        if field is None:
            field = ChordField()
        if not isinstance(field, ChordField):
            raise TypeError('{} has wrong type for Field'.format(field))
        else:
            self._fields.append(field)

    def __iter__(self):
        return self

    def __next__(self):
        if self._simple_format is None:
            self._simple_format = SimpleFormat()
        if self._current_field is None:
            self._field_iter = iter(self.fields)
            self._current_field = self._field_iter.__next__()
        try:
            chord = self._current_field.__next__()
            self._simple_format.add_chord(chord)
            return chord
        except StopIteration:
            self._current_field = self._field_iter.__next__()
            self.__next__()

    @property
    def simple_format(self):
        if self._simple_format is None:
            list(self)
        return self._simple_format
