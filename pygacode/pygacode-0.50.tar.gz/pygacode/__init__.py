import sys

from gacode_ext import expro
from gacode_ext import geo
from gacode_ext import vis


def gapystr_get(s):
    u = []
    for i in range(len(s)):
        if sys.version_info[0] == 2:
            u.append(str(s[i]).strip())
        else:
            u.append(str(s[i], 'utf-8').strip())
    return u


def gapystr_set(s, l=10, n=20):
    return [item.ljust(l) for item in s + [''] * n][:n]


__all__ = ['expro', 'geo', 'vis', 'gapystr_get', 'gapystr_set']
