#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

""" Test units """

import functools 
import bob.extension
import nose.tools
import nose.plugins.skip
from .query import Database

protocols = ['default_od','default_cup']


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


def _make_samples(protocol, split=None):
    db = Database(protocol)
    return db.samples(split)


def _test_protocol_consitency(protocol):
    """ Test size of training and test set """
    nose.tools.eq_(len(_make_samples(protocol,'train')), 400)
    nose.tools.eq_(len(_make_samples(protocol,'test')), 400)
    nose.tools.eq_(len(_make_samples(protocol)), 800)

def test_consitency():
    for p in protocols:
        _test_protocol_consitency(p)


def _test_paths(protocol):
    """ Sense check for sample file names """
    samples = _make_samples(protocol)
    for s in samples:
        assert 'jpg' in s.img.path
        assert 'bmp' in s.gt.path

def test_path():
    for p in protocols:
        _test_paths(p)


@rc_variable_set('bob.db.refuge.datadir') 
def _test_pils(protocol):
    """ Test Pillow image size and modes """
    train_samples = _make_samples(protocol,'train')
    test_samples = _make_samples(protocol,'test')

    for s in train_samples:
        # check size
        nose.tools.eq_(s.img.size,(2124,2056))
        nose.tools.eq_(s.gt.size,(2124,2056))
        # check modes
        nose.tools.eq_(s.img.pil_image().mode,'RGB')
        nose.tools.eq_(s.gt.pil_image().mode,'1')

    for s in test_samples:
        # check size
        nose.tools.eq_(s.img.size,(1634, 1634))
        nose.tools.eq_(s.gt.size,(1634, 1634))
        # check modes
        nose.tools.eq_(s.img.pil_image().mode,'RGB')
        nose.tools.eq_(s.gt.pil_image().mode,'1')


@rc_variable_set('bob.db.refuge.datadir') 
def test_pils():
    """ Test Pillow image size and modes for all protocols """
    for p in protocols:
        _test_pils(p)


@rc_variable_set('bob.db.refuge.datadir') 
def test_checkfiles():
    """ Test bob_dbmanage.py refuge checkfiles command """

    from bob.db.base.script.dbmanage import main
    nose.tools.eq_(main('refuge checkfiles --self-test'.split()), 0)


@rc_variable_set('bob.db.refuge.datadir') 
def test_create():
    """ Test bob_dbmanage.py refuge create command """

    from bob.db.base.script.dbmanage import main
    nose.tools.eq_(main('refuge create --self-test'.split()), 0)