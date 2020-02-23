from itertools import cycle

from musicscore.musicstream.streamvoice import SimpleFormat
from musicscore.musictree.treechord import TreeChord
from musicscore.musicxml.elements.note import Lyric

from musurgia.arithmeticprogression import ArithmeticProgression


class ChordField(object):
    """duration_ or midi_ or chord_generator can be iterators or classes with call method which use current time
    position to output a value. If a value_generator has a duration attribute, it will be overwritten by Field.duration. The same is
    the case for sum (s) in ArithmeticProgression """

    def __init__(self, quarter_duration, duration_generator=None, midi_generator=None, chord_generator=None,
                 transition_mode=None,
                 name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._quarter_duration = None
        self._current_duration = None
        self._position = 0
        self._duration_generator = None
        self._midi_generator = None
        self._chord_generator = None
        self._transition_mode = None
        self._exit = False
        self._first = True
        self._simple_format = SimpleFormat()
        self.quarter_duration = quarter_duration
        self.duration_generator = duration_generator
        self.midi_generator = midi_generator
        self.chord_generator = chord_generator
        self.transition_mode = transition_mode
        self.name = name

    def _set_value_generator_duration(self, value_generator):
        if value_generator is not None:
            if isinstance(value_generator, ArithmeticProgression):
                value_generator.s = self.quarter_duration
            else:
                try:
                    value_generator.duration = self.quarter_duration
                except AttributeError:
                    pass

    @property
    def quarter_duration(self):
        return self._quarter_duration

    @quarter_duration.setter
    def quarter_duration(self, value):
        if not value:
            raise ValueError('quarter_duration can not be None.')
        self._quarter_duration = value
        self._set_value_generator_duration(self.duration_generator)
        self._set_value_generator_duration(self.midi_generator)
        self._set_value_generator_duration(self.chord_generator)

    @property
    def duration_generator(self):
        return self._duration_generator

    @duration_generator.setter
    def duration_generator(self, value):
        if value is None:
            value = cycle([1])
        self._duration_generator = value
        self._set_value_generator_duration(self.duration_generator)

    @property
    def midi_generator(self):
        return self._midi_generator

    @midi_generator.setter
    def midi_generator(self, value):
        if value is None:
            value = cycle([71])
        self._midi_generator = value
        self._set_value_generator_duration(self.midi_generator)

    @property
    def chord_generator(self):
        return self._chord_generator

    @chord_generator.setter
    def chord_generator(self, value):
        self._chord_generator = value
        if value is not None:
            self._set_value_generator_duration(self.chord_generator)

    @property
    def transition_mode(self):
        return self._transition_mode

    @transition_mode.setter
    def transition_mode(self, value):
        if value not in [None, 'pre', 'post']:
            raise ValueError('transition_mode can only be None, pre or post')
        self._transition_mode = value

    @property
    def position(self):
        return self._position

    def __iter__(self):
        return self

    def __next__(self):
        if self.quarter_duration == 0:
            raise StopIteration()

        if self._exit:
            raise StopIteration()

        try:
            if self.chord_generator is None:
                next_duration = None
                next_midi = None

                if callable(getattr(self.duration_generator, '__next__', None)):
                    next_duration = self.duration_generator.__next__()
                elif hasattr(self.duration_generator, '__call__'):
                    next_duration = self.duration_generator(self.position)

                if callable(getattr(self.midi_generator, '__next__', None)):
                    next_midi = self.midi_generator.__next__()
                elif hasattr(self.midi_generator, '__call__'):
                    next_midi = self.midi_generator(self.position)

                remain = self.quarter_duration - self.position
                self._position += next_duration

                if self._position < self.quarter_duration:
                    pass
                elif self._position == self.quarter_duration:
                    self._exit = True

                elif self._position > self.quarter_duration:
                    if self.transition_mode is None:
                        next_duration = remain
                        self._position = self.quarter_duration
                    elif self.transition_mode == 'post':
                        self.quarter_duration = self.position
                    elif self.transition_mode == 'pre':
                        self.quarter_duration = self.position - remain
                        raise StopIteration()

                    self._exit = True
                chord = TreeChord(quarter_duration=next_duration, midis=next_midi)
                if self._first:
                    if self.name is not None:
                        chord.add_lyric(Lyric(self.name))
                    self._first = False

                self._simple_format.add_chord(chord)
                return chord
            else:
                try:
                    next_chord = self.chord_generator(self.position)
                except TypeError:
                    next_chord = self.chord_generator.__next__()
                remain = self.quarter_duration - self.position
                self._position += next_chord.duration
                if self._position < self.quarter_duration:
                    pass
                elif self._position == self.quarter_duration:
                    self._exit = True
                elif self._position > self.quarter_duration:
                    if self.transition_mode is None:
                        next_chord.quarter_duration = remain
                        self._position = self.duration
                    elif self.transition_mode == 'post':
                        self.quarter_duration = self.position
                    elif self.transition_mode == 'pre':
                        self.quarter_duration = self.position - remain
                        raise StopIteration()

                    self._exit = True

                if self._first:
                    if self.name is not None:
                        next_chord.add_lyric(self.name)
                    self._first = False
                self._simple_format.add_chord(next_chord)
                return next_chord
        except StopIteration:
            raise StopIteration()

    @property
    def simple_format(self):
        list(self)
        return self._simple_format
