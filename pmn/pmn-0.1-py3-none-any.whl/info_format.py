import curses

import pmn.string_format as sf
from pmn.size import Size, Method, Align


class InfoFormat:
    def __init__(self, string, size: Size = Size.self(), color_inactive: int = 1, color_active: int = 2):
        self.string = string
        self.size = size
        self.color_inactive = color_inactive
        self.color_active = color_active

    def format(self, free_width=None):
        if free_width and self.size.method == Method.AVAILABLE:
            if self.size.align == Align.LEFT:
                return sf.left_fit(self.string, free_width)
            if self.size.align == Align.RIGHT:
                return sf.right_fit(self.string, free_width)
        else:
            return self.size.format(self.string)

    @staticmethod
    def free_width(formats, screen_width):
        fixed_size_strings = list(map(
            lambda f: f.format(),
            filter(
                lambda f: f.size.method != Method.AVAILABLE,
                formats
            )
        ))
        occupied_width = sum(map(
            lambda f: len(f),
            fixed_size_strings
        ))
        free_width = screen_width - occupied_width
        if free_width < 0:
            raise Exception('not enough space')
        return free_width

    @staticmethod
    def print_formats(formats, screen_width, index, current_index, win):
        free_width = InfoFormat.free_width(formats, screen_width)
        pos_x = 0
        for string_format in formats:
            pos_y = index
            string = string_format.format(free_width)
            if index == current_index:
                win.insstr(pos_y, pos_x, string, curses.color_pair(string_format.color_active))
            else:
                win.insstr(pos_y, pos_x, string, curses.color_pair(string_format.color_inactive))
            pos_x += len(string)
