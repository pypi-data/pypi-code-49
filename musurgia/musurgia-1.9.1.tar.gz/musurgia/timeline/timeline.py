from musurgia.agpdf.drawobject import DrawObject
from musurgia.agpdf.linegroup import LineGroup
from musurgia.timeline.ruler import Ruler
from musurgia.timeline.voice import Voice
from musurgia.tree import Tree


class TimeLineError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TimeLine(DrawObject, Tree):
    def __init__(self, length=None, unit=10, inner_distance=7, bottom_distance=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._length = None
        self.length = length
        self._unit = None
        self.unit = unit
        self._inner_distance = None
        self.inner_distance = inner_distance
        self._bottom_distance = None
        self.bottom_distance = bottom_distance
        self._line_groups = None

    @property
    def ruler(self):
        try:
            return self.get_children()[0]
        except IndexError:
            return None

    @property
    def voices(self):
        try:
            return self.get_children()[1:]
        except IndexError:
            return []

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val):
        if val is not None:
            if self._length:
                raise TimeLineError('length can only be set once')
            self.add_child(Ruler(length=val, unit=10))

        self._length = val

    @property
    def unit(self):
        return self._unit

    def update_units(self):
        for child in self.get_children():
            child.update_unit(self.unit)

    @unit.setter
    def unit(self, val):
        self._unit = val
        self.update_units()

    @property
    def inner_distance(self):
        return self._inner_distance

    @inner_distance.setter
    def inner_distance(self, val):
        self._inner_distance = val

    @property
    def bottom_distance(self):
        return self._bottom_distance

    @bottom_distance.setter
    def bottom_distance(self, val):
        self._bottom_distance = val

    def add_voice(self, name):
        if self._line_groups:
            raise Exception()
        voice = Voice(length=self.length, unit=self.unit, name=name)
        return self.add_child(voice)

    @property
    def line_groups(self):
        if self._line_groups is None:
            output = []
            for index, line in enumerate(self.ruler.lines):
                gl = LineGroup(inner_distance=self.inner_distance, bottom_distance=self.bottom_distance)
                gl.add_line(line)
                for voice in self.voices:
                    gl.add_line(voice.lines[index])
                output.append(gl)
            self._line_groups = output
        return self._line_groups

    def get_relative_x2(self):
        raise Exception('timeline has no x2 value')

    def get_relative_y2(self):
        return self.line_groups[0].get_relative_y2()

    def get_height(self):
        return self.get_relative_y2() - self.line_groups[0].relative_y

    def draw(self, pdf):
        for line_group in self.line_groups:
            if line_group == self.line_groups[0]:
                for child, line in zip(self.get_children()[1:], line_group.lines[1:]):
                    line.name = child.name
                    if line.name:
                        line.name.relative_y = line.relative_y

            line_group.draw_with_break(pdf)
            new_x = pdf.x

            if line_group._line_break:
                for child, line in zip(self.get_children(), line_group.lines):
                    pdf.x = new_x - line_group.length
                    line.name = child.name

                    if line.name:
                        line.name.draw(pdf)
                pdf.x = new_x
