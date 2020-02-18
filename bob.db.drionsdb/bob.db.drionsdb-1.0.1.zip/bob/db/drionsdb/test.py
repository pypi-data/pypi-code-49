#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

""" Test units """

import functools 
import bob.extension
import nose.tools
import nose.plugins.skip
from .query import Database


def rc_variable_set(name):
    """
    Decorator that checks if a given bobrc variable is set before running
    """

    def wrapped_function(test):
        @functools.wraps(test)
        def wrapper(*args, **kwargs):
            if bob.extension.rc[name]:
                return test(*args, **kwargs)
            else:
                raise nose.plugins.skip.SkipTest("bobrc variable '%s' is not set" % name)

        return wrapper

    return wrapped_function


def _make_samples(split=None):
    db = Database()
    return db.samples(split)


def test_protocol_consitency():
    """ Test size of training and test set """

    nose.tools.eq_(len(_make_samples('train')), 60)
    nose.tools.eq_(len(_make_samples('test')), 50)
    # None should return train + test
    nose.tools.eq_(len(_make_samples()),110)

    
def test_paths():
    """ Sense check for sample file names """

    samples = _make_samples()
    for s in samples:
        assert 'image' in s.img.path
        assert 'Expert1' in s.gt.path


@rc_variable_set('bob.db.drionsdb.datadir') 
def test_pils():
    """Test Pillow image size and modes"""
    
    samples = _make_samples()
    for s in samples:
        # check size
        nose.tools.eq_(s.img.size,(600, 400))
        nose.tools.eq_(s.gt.size,(600, 400))
        # check modes
        nose.tools.eq_(s.img.pil_image().mode,'RGB')
        nose.tools.eq_(s.gt.pil_image().mode,'1') 


@rc_variable_set('bob.db.drionsdb.datadir') 
def test_checkfiles():
    """ Test bob_dbmanage.py drionsdb checkfiles command """

    from bob.db.base.script.dbmanage import main
    nose.tools.eq_(main('drionsdb checkfiles --self-test'.split()), 0)


@rc_variable_set('bob.db.drionsdb.datadir') 
def test_create():
    """ Test bob_dbmanage.py drionsdb create command """

    from bob.db.base.script.dbmanage import main
    nose.tools.eq_(main('drionsdb create --self-test'.split()), 0)