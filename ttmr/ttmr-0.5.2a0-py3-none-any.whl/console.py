from sys import stdin
from sys import stdout

ESC = "\033["
NL = "\n"
CR = "\r"
BOLD = ESC + "1m"
CLEAR = ESC + "0m"

BLACK = ESC + "30m"
RED = ESC + "31m"
GREEN = ESC + "32m"
YELLOW = ESC + "33m"
BLUE = ESC + "34m"
MAGENTA = ESC + "35m"
CYAN = ESC + "36m"
WHITE = ESC + "37m"

BG_BLACK = ESC + "40m"
BG_RED = ESC + "41m"
BG_GREEEN = ESC + "42m"
BG_YELLOW = ESC + "43m"
BG_BLUE = ESC + "44m"
BG_MAGENTA = ESC + "45m"
BG_CYAN = ESC + "46m"
BG_WHITE = ESC + "47m"


class Console(object):
    @classmethod
    def cursor_up(cls):
        stdout.write(ESC + "A")

    @classmethod
    def cursor_to_left_margin(cls):
        stdout.write(CR)

    @classmethod
    def clear_line(cls):
        stdout.write(ESC + "K")

    @classmethod
    def init(cls):
        cls.clear_formating()
        stdout.write(NL + ESC + "A")

    @classmethod
    def overwrite(cls):
        cls.cursor_up()
        cls.cursor_to_left_margin()
        cls.clear_line()

    @classmethod
    def write(cls, message):
        stdout.write(message)

    @classmethod
    def writeline(cls, message):
        stdout.write(message + NL)

    @classmethod
    def read(cls):
        stdout.write(stdin.read() + NL)

    @classmethod
    def readline(cls):
        return stdin.readline()

    @classmethod
    def newline(cls):
        stdout.write(NL)

    @classmethod
    def clear_formating(cls):
        stdout.write(CLEAR)
