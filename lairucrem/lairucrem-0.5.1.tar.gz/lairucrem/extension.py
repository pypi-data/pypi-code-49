#! /usr/bin/env python
# Copyright (C) 2016 Alain Leufroy
#
# Author: Alain Leufroy <alain@leufroy.fr>
# Licence: WTFPL, grab your copy here: http://sam.zoy.org/wtfpl/
"""Mercurial extension for lairucrem.

This extension provides utilities that are executed in the repository
side.
"""

import itertools
import re

from mercurial import graphmod, i18n, scmutil, templatekw
from mercurial.__version__ import version as hgversion

hgversion = tuple(int(v) for v in re.split(br'\D', hgversion) if v)

try:
    from mercurial.registrar import command as register_command
except ImportError:
    # hg < 4.6
    from mercurial.cmdutil import command as register_command

try:
    from mercurial.logcmdutil import getrevs
except ImportError:
    try:
        from mercurial.cmdutil import getlogrevs as getrevs
    except ImportError:
        from mercurial.cmdutil import getgraphlogrevs

try:
    from mercurial.logcmdutil import changesetdisplayer
except ImportError:
    from mercurial.cmdutil import show_changeset as changesetdisplayer

try:
    from mercurial.logcmdutil import displaygraph
except ImportError:
    from mercurial.cmdutil import displaygraph



try:
    from mercurial import color
    from mercurial.color import valideffect, _render_effects
    colorext = False
except ImportError:
    from hgext import color
    colorext = True


testedwith = '4.0 4.1 4.2 4.3 4.4. 4.5 5.1'


def monkeypatch(cls, methodname=None):
    """patch a class with decorated method"""
    def decorator(func):
        """decorated"""
        name = methodname or func.__name__
        if not func.__doc__:
            func.__doc__ = getattr(cls, name).__doc__
        setattr(cls, name, func)
        return func
    return decorator


if colorext:
    @monkeypatch(color.colorui)
    def showlabel(self, msg, label):
        ""
        if label and msg:
            if msg[-1] in (b'\n', ord(b'\n')):
                msg = b"\x01" + label + b"\x02" + msg[:-1] + b"\x03\n"
            else:
                msg = b"\x01" + label + b"\x02" + msg + b"\x03"
        return msg

else:
    @monkeypatch(color)
    def colorlabel(ui, msg, label):
        """add color control code according to the mode"""
        if label and msg:
            if msg[-1] in (b'\n', ord(b'\n')):
                msg = b"\x01" + label + b"\x02" + msg[:-1] + b"\x03\n"
            else:
                msg = b"\x01" + label + b"\x02" + msg + b"\x03"
        return msg

cmdtable = {}
command = register_command(cmdtable)


def dagwalker(repo, revs):
    return itertools.chain(
        [(None, 'C', repo[None], [('P', c.rev()) for c in repo[None].parents()])], # workingctx
        graphmod.dagwalker(repo, revs),
    )


@command(b'debuglairucremgraphlog', [
    (b'r', b'rev', [], i18n._('show the specified revision or range'), i18n._('REV')),
    (b'T', b'template', b'', i18n._('display with template'), i18n._('TEMPLATE')),
], inferrepo=True)
def debuglairucremgraphlog(ui, repo, *pats, **opts):
    # Parameters are identical to log command ones
    for key in list(opts.keys()):
        if isinstance(key, str):
            opts[key.encode('utf-8')] = opts.pop(key)
    opts[b'graph'] = True
    revs, filematcher = getrevs(repo, pats, opts)[:2]
    revdag = dagwalker(repo, revs)

    getrenamed = None
    if opts.get('copies'):
        endrev = None
        if opts.get('rev'):
            endrev = scmutil.revrange(repo, opts.get('rev')).max() + 1
        getrenamed = templatekw.getrenamedfn(repo, endrev=endrev)
    displayer = changesetdisplayer(ui, repo, opts, buffered=True)
    if hgversion > (4, 5):
        displaygraph(ui, repo, revdag, displayer, graphmod.asciiedges, getrenamed)
    else:
        displaygraph(ui, repo, revdag, displayer, graphmod.asciiedges, getrenamed,
        filematcher)
