#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

""" Test units """

import functools 
import bob.extension
import nose.tools
import nose.plugins.skip
from .query import Database
protocols = ['default_vessel','default_od']


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

    nose.tools.eq_(len(_make_samples(protocol,'train')), 20)
    nose.tools.eq_(len(_make_samples(protocol,'test')), 10)
    # None should return train + test
    nose.tools.eq_(len(_make_samples(protocol)), 30)


def test_consitency():
    for p in protocols:
        _test_protocol_consitency(p)

def test_paths_vessel():
    """ Sense check for sample file names """
    samples = _make_samples(protocols[0])
    for s in samples:
        assert 'image' in s.img.path
        assert 'GT' in s.gt.path
        assert 'Mask' in s.mask.path

def test_paths_od():
    """ Sense check for sample file names """
    samples = _make_samples(protocols[1])
    for s in samples:
        assert 'image' in s.img.path
        assert 'ODMask' in s.gt.path
        assert 'Mask' in s.mask.path


def _test_pils(protocol):
    """ Test Pillow image size and modes """
    samples = _make_samples(protocol)
    for s in samples:
        # check size
        nose.tools.eq_(s.img.size,(1024, 1024))
        nose.tools.eq_(s.gt.size,(1024, 1024))
        nose.tools.eq_(s.mask.size,(1024, 1024))
        # check modes
        nose.tools.eq_(s.img.pil_image().mode,'RGB')
        nose.tools.eq_(s.gt.pil_image().mode,'1')
        nose.tools.eq_(s.mask.pil_image().mode,'1')  

@rc_variable_set('bob.db.iostar.datadir') 
def test_pils():
    """ Test Pillow image size and modes for all protocols """
    for p in protocols:
        _test_pils(p)


@rc_variable_set('bob.db.iostar.datadir') 
def test_checkfiles():
    """ Test bob_dbmanage.py iostar checkfiles command """

    from bob.db.base.script.dbmanage import main
    nose.tools.eq_(main('iostar checkfiles --self-test'.split()), 0)


@rc_variable_set('bob.db.iostar.datadir') 
def test_create():
    """ Test bob_dbmanage.py iostar create command """

    from bob.db.base.script.dbmanage import main
    nose.tools.eq_(main('iostar create --self-test'.split()), 0)