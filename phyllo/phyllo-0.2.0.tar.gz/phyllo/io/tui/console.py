"""Handle simultaneous line input and display with blessed."""

# Builtins

import logging

# Packages

from phyllo.io.cli.stdin import eval_literal


logger = logging.getLogger(__name__)

try:
    import readline
    readline.set_history_length(64)
except ImportError:
    logger.warning('Console input readline capabilities are not available on this platform.')


# Line reading and editing


class ConsoleLineReader(object):
    """Line buffer with readline-like functionality for blessed console."""

    def __init__(self):
        """Initialize members."""
        self.input_line = ''
        self.history_level = 0
        self.line_cursor = 0

    # Readline history functionality

    def increment_history(self):
        """Increment history up to the readline limit."""
        try:
            self.history_level = min(
                self.history_level + 1, readline.get_current_history_length()
            )
        except NameError:
            return
        self.update_from_history()

    def decrement_history(self):
        """Decrement history down to the readline limit."""
        if self.history_level == 1:
            self.clear()
        self.history_level = max(self.history_level - 1, 0)
        if self.history_level:
            self.update_from_history()

    def get_history(self):
        """Get the line by history level."""
        if not self.history_level:
            return None

        try:
            history_index = readline.get_current_history_length() + 1 - self.history_level
            if not history_index:
                return None
            return readline.get_history_item(history_index)
        except NameError:
            return None

    def update_from_history(self):
        """Update the input string with the history level."""
        history_line = self.get_history()
        if history_line is not None:
            self.input_line = history_line
        self.cursor_end()

    # Line editor functionality

    def clear(self):
        """Clear the input line."""
        self.input_line = ''

    def cursor_left(self):
        """Move the line cursor left."""
        self.line_cursor = max(0, self.line_cursor - 1)

    def cursor_right(self):
        """Move the line cursor right."""
        self.line_cursor = min(len(self.input_line), self.line_cursor + 1)

    def cursor_home(self):
        """Move the line cursor to the left end."""
        self.line_cursor = 0

    def cursor_end(self):
        """Move the line cursor to the right end."""
        self.line_cursor = len(self.input_line)

    def delete_back(self):
        """Backspace on the input line."""
        self.input_line = self.line_before_cursor[:-1] + self.line_from_cursor
        self.cursor_left()

    def delete_forward(self):
        """Delete on the input line."""
        self.input_line = self.line_before_cursor + self.line_after_cursor

    def add(self, char):
        """Add a char to the input line."""
        self.input_line = self.line_before_cursor + char + self.line_from_cursor
        self.cursor_right()

    @property
    def line_before_cursor(self):
        """Return the part of the input line before the cursor."""
        return self.input_line[:self.line_cursor]

    @property
    def line_under_cursor(self):
        """Return the part of the input line under the cursor."""
        try:
            return self.input_line[self.line_cursor]
        except IndexError:
            return ' '

    @property
    def line_after_cursor(self):
        """Return the part of the input line after the cursor."""
        try:
            return self.input_line[self.line_cursor + 1:]
        except IndexError:
            return ''

    @property
    def line_from_cursor(self):
        """Return the part of the input line from the cursor."""
        try:
            return self.input_line[self.line_cursor:]
        except IndexError:
            return ''


# Input prompt


def read_line(term, prompt, refresh_interval=0.1):
    """Get console input of literal values and structures.

    Input is displayed on a prompt at the bottom of the screen.
    """
    with term.location(0, term.height - 1):
        print(
            term.clear_eol + prompt + term.underline + ' ' + term.no_underline,
            end=''
        )
    with term.cbreak():
        with term.hidden_cursor():
            reader = ConsoleLineReader()
            while True:
                key = term.inkey(timeout=refresh_interval)
                if key == '':
                    pass
                elif key.is_sequence:
                    if key.code == term.KEY_ENTER:
                        break
                    elif key.code == term.KEY_BACKSPACE:
                        reader.delete_back()
                    elif key.code == term.KEY_DELETE:
                        reader.delete_forward()
                    elif key.code == term.KEY_ESCAPE:
                        reader.clear()
                    elif key.code == term.KEY_UP:
                        reader.increment_history()
                    elif key.code == term.KEY_DOWN:
                        reader.decrement_history()
                    elif key.code == term.KEY_LEFT:
                        reader.cursor_left()
                    elif key.code == term.KEY_RIGHT:
                        reader.cursor_right()
                    elif key.code == term.KEY_HOME:
                        reader.cursor_home()
                    elif key.code == term.KEY_END:
                        reader.cursor_end()
                elif key == '\x04':  # Ctrl-D
                    raise KeyboardInterrupt
                elif key == '\x0c':  # Ctrl-L
                    print(term.clear)
                elif ord(key) >= ord(u' '):
                    reader.add(key)
                with term.location(0, term.height - 1):
                    print(
                        term.clear_eol + prompt
                        + reader.line_before_cursor
                        + term.underline
                        + reader.line_under_cursor
                        + term.no_underline
                        + reader.line_after_cursor,
                        end=''
                    )
    try:
        readline.add_history(reader.input_line)
    except NameError:
        pass
    with term.location(0, term.height - 1):
        print(term.clear_eol, end='')
    return reader.input_line


def input_literal(term, prompt):
    """Get console input of literal values and structures."""
    while True:
        input_string = read_line(term, prompt)
        if input_string:
            break
    return eval_literal(input_string)
