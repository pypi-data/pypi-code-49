# -*- coding: utf-8 -*-
import contextlib
import math
import sys
import time

# pylint: skip-file


def _default_fp(fp):
    return fp or sys.stderr


def _dynamic_display(fp):
    return (hasattr(fp, 'isatty') and fp.isatty()) or 'ipykernel' in sys.modules


class _NopeProgressbar:
    def update(self, inc=1):
        pass

    def set_postfix_str(self, s='', refresh=True):
        pass


class _SimpleProgressbar:
    def __init__(self, target, width=30, interval=0.05, fp=None):
        self._target = target
        self._width = width
        self._interval = interval
        self._desc = None

        self.__fp = _default_fp(fp)

        self._seen_so_far = 0
        self._start = time.time()
        self._last_update = 0

    def __get_time_per_unit(self, current, now):
        return (now - self._start) / current if current else 0

    @classmethod
    def __get_eta_format(cls, eta):
        if eta > 3600:
            eta_format = ('%d:%02d:%02d' %
                          (eta // 3600, (eta % 3600) // 60, eta % 60))
        elif eta > 60:
            eta_format = '%d:%02d' % (eta // 60, eta % 60)
        else:
            eta_format = '%ds' % eta

        return eta_format

    def __get_eta_str(self, current, now):
        info = ' - %.0fs' % (now - self._start)

        time_per_unit = self.__get_time_per_unit(current, now)

        if current < self._target:
            eta = time_per_unit * (self._target - current)

            if self._desc is not None:
                info += ' - %s' % self._desc

            info += ' - ETA: %s' % self.__get_eta_format(eta)

        return info

    def _should_skip_draw(self, current, now):
        return now - self._last_update < self._interval and self._target is not None and current < self._target

    def _get_bar(self, current):
        num_digits = int(math.floor(math.log10(self._target))) + 1 if self._target > 0 else 1

        prog = float(current) / self._target if self._target > 0 else 1

        prog_width = int(self._width * prog) or 1

        bar_str = '%%%dd/%d [' % (num_digits, self._target)
        progress_bar = bar_str % current

        progress_bar += ('=' * (prog_width - 1))

        if current < self._target:
            progress_bar += '>'
        else:
            progress_bar += '='

        progress_bar += ('.' * (self._width - prog_width))
        progress_bar += ']'

        return progress_bar

    def _full_update(self, current):
        self._seen_so_far = current

        now = time.time()
        if self._should_skip_draw(current, now):
            return

        self.__fp.write('\n')

        progress_bar = self._get_bar(current)

        self.__fp.write(progress_bar)

        info = self.__get_eta_str(current, now)

        self.__fp.write(info)
        self.__fp.flush()

        self._last_update = now

    def update(self, inc=1):
        self._full_update(self._seen_so_far + inc)

    def set_postfix_str(self, desc='', refresh=True):
        self._desc = desc


def _default_interval(interval, def_interval):
    return interval if interval is not None else def_interval


@contextlib.contextmanager
def create_progress_bar(total, desc=None, disable=False, interval=None, fp=None, **kwargs):
    from tqdm import tqdm

    if disable:
        yield _NopeProgressbar()
        return

    fp = _default_fp(fp)

    if _dynamic_display(fp):
        default_dynamic_interval = 0.1

        unit = kwargs.get('unit', 'it')
        ncols = kwargs.get('ncols', 80)
        unit_scale = kwargs.get('unit_scale', False)

        with tqdm(total=total, desc=desc, unit=unit, ncols=ncols,
                  disable=None, unit_scale=unit_scale, file=fp,
                  mininterval=_default_interval(interval, default_dynamic_interval)) as progress_bar:
            yield progress_bar
    else:
        default_static_interval = 5

        progress_bar = _SimpleProgressbar(total, interval=_default_interval(interval, default_static_interval), fp=fp)
        progress_bar.update(0)
        yield progress_bar
