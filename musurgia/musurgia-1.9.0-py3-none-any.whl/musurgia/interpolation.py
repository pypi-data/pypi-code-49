from quicktions import Fraction


class Interpolation(object):
    def __init__(self, start, end, duration, key=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._start = None
        self._end = None
        self._duration = None
        self.start = start
        self.end = end
        self.duration = duration
        self.key = key

    def __call__(self, x):
        if x < 0 or x > self.duration:
            raise ValueError()
        output = Fraction(Fraction(x * (self.end - self.start)), self.duration) + self.start
        if self.key:
            return self.key(output)
        return output


class InterpolationGroup(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sections = []

    def add_section(self, start, end, duration):
        section = Interpolation(start, end, duration)

        if not isinstance(section, Interpolation):
            raise TypeError()
        self._sections.append(section)

    def __call__(self, x):
        temp_x = x
        for section in self._sections:
            try:
                return section.__call__(temp_x)
            except ValueError:
                temp_x -= section.duration

        raise ValueError(x)
