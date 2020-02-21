import curses
from curses import window

import psutil as ps
from psutil import Process

from pmn.abstract_process_view import AbstractProcessView
from pmn.info_format import InfoFormat
from pmn.search_view import SearchView
from pmn.status_view import StatusView


class ListProcessView(AbstractProcessView):
    def __init__(self, screen, config):
        super().__init__(screen)
        self.processes = list(filter(
            lambda p: p.cmdline(),
            map(lambda pid: Process(pid), ps.pids())
        ))
        self.visible_processes = self.processes
        self.layout = config.list_layout
        self.keymap = config.list_keymap
        self.pad: window = None
        self.status = StatusView(self.screen)
        self.search = SearchView(self.screen)
        self.search_string = ''

        self.current_process_index = 0
        self.page_scroll_offset = 0

    def show(self):
        self.screen.refresh()
        h, w = self.screen.getmaxyx()

        self.pad = curses.newpad(len(self.visible_processes) if self.visible_processes else 1, w)

        for i, p in enumerate(self.visible_processes):
            if p.is_running():
                self.print_process(p, i)

        self.pad.refresh(self.page_scroll_offset, 0, 0, 0, h - 1 - 1, w - 1)
        self.status.draw(f'{self.current_process_index + 1}/{len(self.visible_processes)}')

    def loop(self):
        return self.keymap(self)

    def search_loop(self):
        curses.curs_set(1)
        while True:
            self.first()
            self.screen.erase()
            self.visible_processes = self.search_processes(
                self.search_string
            )
            self.show()
            self.search.draw(self.search_string)
            search_key = self.screen.getch()
            if search_key == curses.KEY_BACKSPACE:
                self.search_string = self.search_string[:-1]
            elif search_key == ord('\n'):
                curses.curs_set(0)
                break
            elif search_key == 27:
                self.clear_search()
                break
            else:
                self.search_string += chr(search_key)

    def clear_search(self):
        curses.curs_set(0)
        self.first()
        self.search_string = ''
        self.screen.erase()
        self.visible_processes = self.search_processes(
            self.search_string
        )
        self.show()

    def resize(self, h):
        new_h, new_w = self.screen.getmaxyx()
        delta_current = self.current_process_index - self.page_scroll_offset + 1
        if delta_current > h / 2:
            delta_h = h - new_h
            self.page_scroll_offset += delta_h
        self.screen.erase()

    def next(self):
        if self.current_process_index == len(self.visible_processes) - 1:
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
        self.current_process_index = len(self.visible_processes) - 1
        self.page_scroll_offset = self.current_process_index - self.screen.getmaxyx()[0] + 2

    def print_process(self, process: Process, index):
        formats = self.layout(process)
        InfoFormat.print_formats(
            formats,
            self.screen.getmaxyx()[1],
            index,
            self.current_process_index,
            self.pad
        )

    def search_processes(self, search_string):
        return list(filter(
            lambda p: search_string in ' '.join(p.cmdline()),
            self.processes
        ))
