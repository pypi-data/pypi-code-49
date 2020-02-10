#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import _4quila
import os
import tempfile
import fcntl
import contextlib

@contextlib.contextmanager
def lock(lock_id):
    basename = '%s.lock' % lock_id
    lockfile = os.path.normpath(tempfile.gettempdir() + '/' + basename)
    fp = open(lockfile, 'w')
    fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)

    yield

    fcntl.lockf(fp, fcntl.LOCK_UN)
    if os.path.isfile(lockfile):
        os.unlink(lockfile)
