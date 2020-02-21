import curses
from curses import window

from pmn import string_format as sf


class StatusView:
    def __init__(self, screen):
        self.screen: window = screen
        self.width = 8
        self.status = None

    def draw(self, text):
        h, w = self.screen.getmaxyx()
        self.status: window = curses.newwin(1, self.width, h - 1, w - self.width)
        self.status.border()
        self.status.erase()
        self.status.insstr(0, 0, sf.right_fit(text, self.width))
        self.status.refresh()
