from os import listdir
from os.path import join, normpath, isdir
from threading import Thread, RLock
from queue import Queue
from pathlib import Path
from time import sleep

from .inotify import Inotify, FLAGS, mask_str


globals().update(FLAGS)
ALL = ACCESS|MODIFY|ATTRIB|WRITE|CLOSE|OPEN|CREATE|DELETE


class Event:
    def __init__(self, wd, watcher, mask, cookie, name):
        self.wd = wd
        self.watcher = watcher
        self.mask = mask
        self.cookie = cookie
        self.name = name

    @property
    def watch(self):
        return self.watcher.watches[self.wd]

    @property
    def path(self):
        path = self.watch.path
        path = join(path, self.name) if self.name else path
        return Path(path)

    def __str__(self):
        return '{} -> {}'.format(mask_str(self.mask), self.path)


class Watch:
    def __init__(self, wd, watcher, mask, path, callback, recur=False, _parent=None):
        self.wd = wd
        self.watcher = watcher
        self.mask = mask
        self.path = normpath(path)
        self.callback = callback
        self.recur = recur
        self._parent =_parent
        if isdir(self.path) and self.recur:
            for name in listdir(self.path):
                path =  join(self.path, name)
                if isdir(path):
                    self.watcher.add(
                        path, mask, callback, recur=True, _parent=self
                    )

    def __str__(self):
        return 'Watch {}.{} {} {} -> {}'.format(
            self.watcher.inotify.ifd,
            self.wd,
            self.path,
            mask_str(self.mask),
            self.callback.__name__,
        )


def default(event):
    if event.mask not in (ISDIR|OPEN, ISDIR|CLOSE): print(event)


class Watcher:
    def __init__(self):
        self.inotify = Inotify()
        self.watches = {}
        self.queue = Queue()
        self.lock = RLock()
        for t in (self._push, self._pull):
            t = Thread(target=t)
            t.setDaemon(True)
            t.start()

    def _push(self):
        while True:
            for wd, mask, cookie, name in self.inotify.read():
                self.queue.put(
                    Event(wd, self, mask, cookie, name)
                )

    def _pull(self):
        while True:
            event = self.queue.get()
            mask = event.mask
            with self.lock:
                watch = self.watches.get(event.wd)
            watch.callback(event)
            if mask&ISDIR and mask&CREATE and watch.recur:
                self.add(
                    event.path,
                    watch.mask,
                    watch.callback,
                    recur = True,
                    _parent = watch,
                )
            if mask&IGNORED:
                # text editors (vim, ...) -> IGNORE ???
                self.rem(watch)
                self.add(
                    path = watch.path,
                    mask = watch.mask,
                    callback = watch.callback,
                    recur = watch.recur,
                    _parent = watch._parent,
                )

    def add(self, path, mask=ALL, callback=default, recur=False, _parent=None):
        with self.lock:
            wd = self.inotify.add_watch(path, mask)
            watch = Watch(wd, self, mask, path, callback, recur, _parent)
            self.watches[wd] = watch
        return watch

    def rem(self, watch):
        with self.lock:
            for w in list(self.watches.values()):
                if w._parent==watch:
                    self.rem(w)
            wd = watch.wd
            self.watches.pop(wd)

    def close(self):
        self.inotify.close()

    def __enter__(self):
        return self

    def __exit__(self, typ, val, tbk):
        try:
            while True: sleep(11)
        except KeyboardInterrupt:
            print
        finally:
            self.close()

