from quicktions import Fraction


class InterpolationSection(object):
    def __init__(self, start, end, duration, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._start = None
        self._end = None
        self._duration = None
        self.start = start
        self.end = end
        self.duration = duration

    def get_value(self, x):
        if x < 0 or x > self.duration:
            raise ValueError()
        return Fraction(Fraction(x * (self.end - self.start)), self.duration) + self.start


class Interpolation(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sections = []

    def add_section(self, start, end, duration):
        section = InterpolationSection(start, end, duration)

        if not isinstance(section, InterpolationSection):
            raise TypeError()
        self._sections.append(section)

    def get_value(self, x):
        temp_x = x
        for section in self._sections:
            try:
                return section.get_value(temp_x)
            except ValueError:
                temp_x -= section.duration

        raise ValueError(x)
