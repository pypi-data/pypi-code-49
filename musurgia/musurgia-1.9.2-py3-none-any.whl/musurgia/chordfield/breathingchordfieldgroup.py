from musurgia.chordfield import ChordField, ChordFieldGroup


class Breathe(ChordFieldGroup):
    def __init__(self, duration=None, proportions=None, durations=None, repose_1=None, inspiration=None, climax=None,
                 expiration=None, repose_2=None):
        super().__init__(None, None, None, None, None)
        self._duration = None
        self._proportions = None
        self._durations = [None, None, None, None, None]

        self.duration = duration
        self.proportions = proportions
        self.durations = durations

        self._repose_1 = None
        self.repose_1 = repose_1
        self._inspiration = None
        self.inspiration = inspiration
        self._climax = None
        self.climax = climax
        self._expiration = None
        self.expiration = expiration
        self.repose_2 = None
        self.repose_2 = repose_2

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
        self.calculate_durations()

    @property
    def repose_1(self):
        return self.fields[0]

    @repose_1.setter
    def repose_1(self, value):
        if value is not None and not isinstance(value, ChordField):
            raise TypeError(
                'repose_1 value should be of type Field. If None a new instance of Field() will be assigned')
        elif value is None:

            field = ChordField()
            field.duration = self.durations[0]
            self.fields[0] = field
        else:
            field = value
            if self.durations[0] is not None:
                field.duration = self.durations[0]

        self.fields[0] = field

    @property
    def inspiration(self):
        return self.fields[1]

    @inspiration.setter
    def inspiration(self, value):
        if value is not None and not isinstance(value, ChordField):
            raise TypeError(
                'inspiration value should be of type Field. If None a new instance of Field() will be assigned')
        elif value is None:
            field = ChordField()
            field.duration = self.durations[1]
            self.fields[1] = field
        else:
            field = value
            if self.durations[1] is not None:
                field.duration = self.durations[1]

        self.fields[1] = field

    @property
    def climax(self):
        return self.fields[2]

    @climax.setter
    def climax(self, value):
        if value is not None and not isinstance(value, ChordField):
            raise TypeError('climax value should be of type Field. If None a new instance of Field() will be assigned')
        elif value is None:
            field = ChordField()
            field.duration = self.durations[2]
            self.fields[2] = field
        else:
            field = value
            if self.durations[2] is not None:
                field.duration = self.durations[2]

        self.fields[2] = field

    @property
    def expiration(self):
        return self.fields[3]

    @expiration.setter
    def expiration(self, value):
        if value is not None and not isinstance(value, ChordField):
            raise TypeError(
                'expiration value should be of type Field. If None a new instance of Field() will be assigned')
        elif value is None:
            field = ChordField()
            field.duration = self.durations[3]
            self.fields[3] = field
        else:
            field = value
            if self.durations[3] is not None:
                field.duration = self.durations[3]

        self.fields[3] = field

    @property
    def repose_2(self):
        return self.fields[4]

    @repose_2.setter
    def repose_2(self, value):
        if value is not None and not isinstance(value, ChordField):
            raise TypeError(
                'repose_2 value should be of type Field. If None a new instance of Field() will be assigned')
        elif value is None:

            field = ChordField()
            field.duration = self.durations[4]
            self.fields[4] = field
        else:
            field = value
            if self.durations[4] is not None:
                field.duration = self.durations[4]

        self.fields[4] = field

    @ChordFieldGroup.fields.getter
    def fields(self):
        self._fields[0].name = 'repose_1'
        self._fields[1].name = 'inspiration'
        self._fields[2].name = 'climax'
        self._fields[3].name = 'expiration'
        self._fields[4].name = 'repose_2'
        return self._fields

    def calculate_durations(self):
        if self.duration is not None and self.proportions is not None:
            self.durations = [proportion * float(self.duration) / sum(self.proportions) for proportion in
                              self.proportions]

    @property
    def proportions(self):
        return self._proportions

    @proportions.setter
    def proportions(self, values):
        self._proportions = values
        self.calculate_durations()

    @property
    def durations(self):
        return [self.repose_1.duration, self.inspiration.duration, self.climax.duration, self.expiration.duration,
                self.repose_2.duration]

    @durations.setter
    def durations(self, values):
        try:
            self.repose_1.duration = values[0]
            try:
                self.inspiration.duration = values[1]
                try:
                    self.climax.duration = values[2]
                    try:
                        self.expiration.duration = values[3]
                        try:
                            self.repose_2.duration = values[4]
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except Exception as err:
            pass

    def add_field(self, field):
        if len(self._fields) < 5:
            if field is None:
                field = ChordField()
            if not isinstance(field, ChordField):
                raise TypeError('wrong type for Field')
            else:
                self._fields.append(field)
        else:
            raise Exception('Breath() does not support add_field')
