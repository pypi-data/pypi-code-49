import curses
from curses import window


class SearchView:
    def __init__(self, screen):
        self.screen: window = screen
        self.left_width = 8
        self.text = None

    def draw(self, text):
        h, w = self.screen.getmaxyx()
        self.text: window = curses.newwin(1, w - self.left_width, h - 1, 0)
        self.text.border()
        self.text.erase()
        string = f'/{text}'
        self.text.insstr(0, 0, string)
        self.text.move(0, len(string))
        self.text.refresh()

    def clear(self):
        self.text.erase()
        self.text.refresh()
