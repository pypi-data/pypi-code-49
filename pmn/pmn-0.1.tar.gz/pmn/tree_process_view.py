import curses
from curses import window

from anytree import AnyNode

from pmn import string_format as sf
from pmn.abstract_process_view import AbstractProcessView
from pmn.info_format import InfoFormat
from pmn.process_tree import ProcessTree
from pmn.status_view import StatusView


class TreeProcessView(AbstractProcessView):
    def __init__(self, screen, config):
        super().__init__(screen)
        self.screen: window = screen
        self.tree = ProcessTree()
        self.processes = self.tree.flatten()
        self.visible = list(filter(lambda n: ProcessTree.is_visible(n), self.processes))
        self.layout = config.tree_layout
        self.keymap = config.tree_keymap
        self.pad: window
        self.status = StatusView(self.screen)

        self.current_process_index = 0
        self.page_scroll_offset = 0

    def show(self):
        self.screen.refresh()
        h, w = self.screen.getmaxyx()

        self.pad = curses.newpad(len(self.processes), w)

        for i, node in enumerate(self.visible):
            if node.process.is_running():
                self._print_process(node, i)

        self.pad.refresh(self.page_scroll_offset, 0, 0, 0, h - 1 - 1, w - 1)
        self.status.draw(sf.right_fit(f'{self.current_process_index + 1}/{len(self.visible)}', w - 1))

    def loop(self):
        return self.keymap(self)

    def resize(self, h):
        new_h, new_w = self.screen.getmaxyx()
        delta_current = self.current_process_index - self.page_scroll_offset + 1
        if delta_current > h / 2:
            delta_h = h - new_h
            self.page_scroll_offset += delta_h
        self.screen.erase()

    def next(self):
        if self.current_process_index == len(self.visible) - 1:
            return
        self.current_process_index += 1
        if self.current_process_index == self.page_scroll_offset + self.screen.getmaxyx()[0] - 1:
            self.page_scroll_offset += 1

    def prev(self):
        if self.current_process_index == 0:
            return
        self.current_process_index -= 1
        if self.current_process_index == self.page_scroll_offset - 1:
            self.page_scroll_offset -= 1

    def first(self):
        self.page_scroll_offset = 0
        self.current_process_index = 0

    def last(self):
        self.current_process_index = len(self.visible) - 1
        self.page_scroll_offset = self.current_process_index - self.screen.getmaxyx()[0] + 2

    def trigger_collapse_current(self):
        current = self.visible[self.current_process_index]
        current.collapsed = not current.collapsed
        self.visible = list(filter(lambda n: ProcessTree.is_visible(n), self.processes))

    def _print_process(self, node: AnyNode, index):
        formats = self.layout(node)
        InfoFormat.print_formats(
            formats,
            self.screen.getmaxyx()[1],
            index,
            self.current_process_index,
            self.pad
        )
