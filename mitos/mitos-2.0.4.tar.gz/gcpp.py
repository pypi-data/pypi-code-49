#!/usr/bin/venv python

'''
@author: M. Bernt

This is a confidential release. Do not redistribute without 
permission of the author (bernt@informatik.uni-leipzig.de).

create a nice output of genetic codes
'''

import sys
import re
from optparse import OptionParser

from Bio.Data import CodonTable


class TerminalController:
    """
    A class that can be used to portably generate formatted output to
    a terminal.  

    `TerminalController` defines a set of instance variables whose
    values are initialized to the control sequence necessary to
    perform a given action.  These can be simply included in normal
    output to the terminal:

        >>> term = TerminalController()
        >>> print 'This is '+term.GREEN+'green'+term.NORMAL

    Alternatively, the `render()` method can used, which replaces
    '${action}' with the string required to perform 'action':

        >>> term = TerminalController()
        >>> print term.render('This is ${GREEN}green${NORMAL}')

    If the terminal doesn't support a given action, then the value of
    the corresponding instance variable will be set to ''.  As a
    result, the above code will still work on terminals that do not
    support color, except that their output will not be colored.
    Also, this means that you can test whether the terminal supports a
    given action by simply testing the truth value of the
    corresponding instance variable:

        >>> term = TerminalController()
        >>> if term.CLEAR_SCREEN:
        ...     print 'This terminal supports clearning the screen.'

    Finally, if the width and height of the terminal are known, then
    they will be stored in the `COLS` and `LINES` attributes.
    """
    # Cursor movement:
    BOL = ''  # : Move the cursor to the beginning of the line
    UP = ''  # : Move the cursor up one line
    DOWN = ''  # : Move the cursor down one line
    LEFT = ''  # : Move the cursor left one char
    RIGHT = ''  # : Move the cursor right one char

    # Deletion:
    CLEAR_SCREEN = ''  # : Clear the screen and move to home position
    CLEAR_EOL = ''  # : Clear to the end of the line.
    CLEAR_BOL = ''  # : Clear to the beginning of the line.
    CLEAR_EOS = ''  # : Clear to the end of the screen

    # Output modes:
    BOLD = ''  # : Turn on bold mode
    BLINK = ''  # : Turn on blink mode
    DIM = ''  # : Turn on half-bright mode
    REVERSE = ''  # : Turn on reverse-video mode
    NORMAL = ''  # : Turn off all modes

    # Cursor display:
    HIDE_CURSOR = ''  # : Make the cursor invisible
    SHOW_CURSOR = ''  # : Make the cursor visible

    # Terminal size:
    COLS = None  # : Width of the terminal (None for unknown)
    LINES = None  # : Height of the terminal (None for unknown)

    # Foreground colors:
    BLACK = BLUE = GREEN = CYAN = RED = MAGENTA = YELLOW = WHITE = ''

    # Background colors:
    BG_BLACK = BG_BLUE = BG_GREEN = BG_CYAN = ''
    BG_RED = BG_MAGENTA = BG_YELLOW = BG_WHITE = ''

    _STRING_CAPABILITIES = """
    BOL=cr UP=cuu1 DOWN=cud1 LEFT=cub1 RIGHT=cuf1
    CLEAR_SCREEN=clear CLEAR_EOL=el CLEAR_BOL=el1 CLEAR_EOS=ed BOLD=bold
    BLINK=blink DIM=dim REVERSE=rev UNDERLINE=smul NORMAL=sgr0
    HIDE_CURSOR=cinvis SHOW_CURSOR=cnorm""".split()
    _COLORS = """BLACK BLUE GREEN CYAN RED MAGENTA YELLOW WHITE""".split()
    _ANSICOLORS = "BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE".split()

    def __init__(self, term_stream=sys.stdout):
        """
        Create a `TerminalController` and initialize its attributes
        with appropriate values for the current terminal.
        `term_stream` is the stream that will be used for terminal
        output; if this stream is not a tty, then the terminal is
        assumed to be a dumb terminal (i.e., have no capabilities).
        """
        # Curses isn't available on all platforms
        try:
            import curses
        except:
            return

        # If the stream isn't a tty, then assume it has no capabilities.
        if not term_stream.isatty():
            return

        # Check the terminal type.  If we fail, then assume that the
        # terminal has no capabilities.
        try:
            curses.setupterm()
        except:
            return

        # Look up numeric capabilities.
        self.COLS = curses.tigetnum('cols')
        self.LINES = curses.tigetnum('lines')

        # Look up string capabilities.
        for capability in self._STRING_CAPABILITIES:
            (attrib, cap_name) = capability.split('=')
            setattr(self, attrib, self._tigetstr(cap_name) or '')

        # Colors
        set_fg = self._tigetstr('setf')
        if set_fg:
            for i, color in zip(list(range(len(self._COLORS))), self._COLORS):
                setattr(self, color, curses.tparm(set_fg, i) or '')
        set_fg_ansi = self._tigetstr('setaf')
        if set_fg_ansi:
            for i, color in zip(list(range(len(self._ANSICOLORS))), self._ANSICOLORS):
                setattr(self, color, curses.tparm(set_fg_ansi, i) or '')
        set_bg = self._tigetstr('setb')
        if set_bg:
            for i, color in zip(list(range(len(self._COLORS))), self._COLORS):
                setattr(self, 'BG_' + color, curses.tparm(set_bg, i) or '')
        set_bg_ansi = self._tigetstr('setab')
        if set_bg_ansi:
            for i, color in zip(list(range(len(self._ANSICOLORS))), self._ANSICOLORS):
                setattr(
                    self, 'BG_' + color, curses.tparm(set_bg_ansi, i) or '')

    def _tigetstr(self, cap_name):
        # String capabilities can include "delays" of the form "$<2>".
        # For any modern terminal, we should be able to just ignore
        # these, so strip them out.
        import curses
        cap = curses.tigetstr(cap_name) or ''
        return re.sub(r'\$<\d+>[/*]?', '', cap)

    def render(self, template):
        """
        Replace each $-substitutions in the given template string with
        the corresponding terminal control string (if it's defined) or
        '' (if it's not).
        """
        return re.sub(r'\$\$|\${\w+}', self._render_sub, template)

    def _render_sub(self, match):
        s = match.group()
        if s == '$$':
            return s
        else:
            return getattr(self, s[2:-1])


usage = """%prog [OPTIONS] list of genetic codes
gcpp outputs the given or all standard genetic codes: 
- first 3 lines gives the codons
- then one line per genetic code (*: stop, inverted text: start)

if a reference genetic code is given, the differences are shown
"""
parser = OptionParser(usage)
parser.add_option("-r", "--ref", action="store", type="int",
                  metavar="CODE", help="reference genetic code")
(options, args) = parser.parse_args()

term = TerminalController()
bases = ["T", "C", "A", "G"]
for i in range(3):
    sys.stdout.write("   ")
    for x in bases:
        for y in bases:
            for z in bases:
                triple = x + y + z
                sys.stdout.write(triple[i])
    sys.stdout.write("\n")

codes = []
for a in args:
    try:
        CodonTable.unambiguous_dna_by_id[int(a)]
        codes.append(int(a))
    except:
        sys.stderr.write("unknown genetic code", a)

if len(codes) == 0:
    codes = list(range(1, 24))

for i in codes:
    try:
        CodonTable.unambiguous_dna_by_id[i]
    except:
        continue

    sys.stdout.write("%.2d " % i)
    for x in bases:
        for y in bases:
            for z in bases:
                if x + y + z in CodonTable.unambiguous_dna_by_id[i].start_codons:
                    sys.stdout.write(term.REVERSE)

                if options.ref != None and \
                    ((x + y + z in CodonTable.unambiguous_dna_by_id[options.ref].start_codons) !=
                     (x + y + z in CodonTable.unambiguous_dna_by_id[i].start_codons)):
                    sys.stdout.write(term.RED)

                try:
                    if options.ref != None and \
                            CodonTable.unambiguous_dna_by_id[i].forward_table[x + y + z] != \
                            CodonTable.unambiguous_dna_by_id[i].forward_table[x + y + z]:

                        sys.stdout.write(term.RED)

                    sys.stdout.write(
                        CodonTable.unambiguous_dna_by_id[i].forward_table[x + y + z])

                except:
                    sys.stdout.write("*")
                sys.stdout.write(term.NORMAL)

    sys.stdout.write("\n")
