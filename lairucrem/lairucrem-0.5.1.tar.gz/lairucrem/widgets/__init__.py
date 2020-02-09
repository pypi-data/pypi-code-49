# Copyright (C) 2016 Alain Leufroy
#
# Author: Alain Leufroy <alain@leufroy.fr>
# Licence: WTFPL, grab your copy here: http://sam.zoy.org/wtfpl/
"""UI widgets for lairucrem."""

import re

import urwid
from urwid.canvas import CompositeCanvas

from .. import config
from ..utils import monkeypatch
from .utils import attrwrap

urwid.set_encoding('utf-8')


@monkeypatch(urwid.CommandMap)
def __getitem__(self, key):
    # Accept a command as a key.
    command = self._command.get(key, None)
    if command:
        return command
    if key in self._command.values():
        return key
    return None


class disablable_button_mixin:

    _disabled = False
    _disabled_map = {None: 'ui.button.disabled'}

    def selectable(self):
        return self._label._selectable and not self._disabled

    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        shouldinvalidate = self._disabled != value
        self._disabled = value
        if shouldinvalidate:
            self._invalidate()

    def render(self, size, focus=False):
        if self._disabled:
            attr_map = self._disabled_map
            canv = super().render(size, focus=focus)
            canv = CompositeCanvas(canv)
            canv.fill_attr_apply(attr_map)
            return canv
        return super().render(size, focus)


class lightbutton(attrwrap, disablable_button_mixin, urwid.Button):
    """Simple button without decoration"""

    _attr_map = {None: 'ui.button'}
    _focus_map = {None: 'ui.button.focus'}
    button_left = urwid.Text("")
    button_right = urwid.Text("")

    def __repr__(self):
        return f'<lightbutton label="{self._label.get_text()}">'

    def keypress(self, size, key):
        if key == ' ':
            return ' '
        else:
            return super().keypress(size, key)


class edit(attrwrap, urwid.Edit):
    """urwid.Edit with default style."""

    _word_sep_regexp = re.compile('(%s)' % '|'.join((
        r'\s', '\.', ',', ';', ':', '\+', '\-', '\*', '%',
        '/', r'\\', '\(', '\)', '\[', '\]', '\{', '\}')))

    _attr_map = {None: 'ui.edit'}
    _focus_map = {None: 'ui.edit.focus'}

    _command_map = config.edit_command_map

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key is None:
            return key
        command = self._command_map[key]
        if command == config.CMD_NEXT_WORD:
            self._move_cursor_next_word()
            return None
        if command == config.CMD_PREV_WORD:
            self._move_cursor_prev_word()
            return None
        if command == config.CMD_KILL_LINE:
            self._trim_edit_text_at_cursor()
            return None
        if command == config.CMD_KILL_PREV_WORD:
            self._remove_previous_word()
            return
        if command == config.CMD_KILL_NEXT_WORD:
            self._remove_next_word()
            return
        return key

    def _move_cursor_next_word(self):
        pos = self._find_next_word_start()
        if pos is not None:
            self.set_edit_pos(pos)

    def _move_cursor_prev_word(self):
        pos = self._find_prev_word_start()
        if pos is not None:
            self.set_edit_pos(pos)

    def _trim_edit_text_at_cursor(self):
        text = self.edit_text
        p = self.edit_pos
        self.set_edit_text(text[:p])

    def _remove_previous_word(self):
        text = self.edit_text
        p = self._find_prev_word_start()
        if p is None or p == self.edit_pos:
            return
        after = text[self.edit_pos:]
        p = self._find_prev_word_start()
        before = text[:p]
        self.set_edit_text(before + after)
        self.set_edit_pos(p)

    def _remove_next_word(self):
        text = self.edit_text
        p = self._find_next_word_start()
        if p is None or p == self.edit_pos:
            return
        before = text[:self.edit_pos]
        p = self._find_next_word_start()
        after = text[p:]
        self.set_edit_text(before + after)

    def _find_prev_word_start(self):
        p = self.edit_pos
        if p is None or p <= 0:
            return
        text = self.edit_text[p - 1::-1]
        match = self._word_sep_regexp.search(text)
        if match:
            p -= match.start() + 1
        else:
            p = 0
        return p

    def _find_next_word_start(self):
        p = self.edit_pos
        text = self.edit_text
        if p is None or p >= len(text):
            return
        match = self._word_sep_regexp.search(text[p + 1:])
        if match:
            p += match.start() + 1
        else:
            p = len(text)
        return p
