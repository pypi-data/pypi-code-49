""" Test suite for navis.

Examples
--------

From terminal:
$ cd folder/to/navis
$ pytest

From shell:
>>> import unittest
>>> from navis.test import test_neurons
>>> suite = unittest.TestLoader().loadTestsFromModule(test_neurons)
>>> unittest.TextTestRunner().run(suite)

"""

import unittest
import warnings

import navis

try:
    import igraph  # type: ignore
except BaseException:
    igraph = None
    warnings.warn('iGraph library not found. Will test only with NetworkX.')

import doctest


class TestNeurons(unittest.TestCase):
    """Test navis.core.neurons. """

    def try_conditions(func):
        """Runs each test under various conditions and asserts that results
        are always the same."""

        def wrapper(self, *args, **kwargs):
            navis.config.use_igraph = False
            res1 = func(self, *args, **kwargs)
            if igraph:
                navis.config.use_igraph = True
                res2 = func(self, *args, **kwargs)
                self.assertEqual(res1, res2)
            return res1
        return wrapper

    @try_conditions
    def test_from_swc(self):
        n = navis.example_neurons(n=1, source='swc')
        self.assertIsInstance(n, navis.TreeNeuron)

    @try_conditions
    def test_from_gml(self):
        n = navis.example_neurons(n=1, source='gml')
        self.assertIsInstance(n, navis.TreeNeuron)

class TestExamples(unittest.TestCase):
    """Test pymaid.tiles """

    def setUp(self):
        self.rm = pymaid.CatmaidInstance(config_test.server_url,
                                         config_test.http_user,
                                         config_test.http_pw,
                                         config_test.token)

    def test_fetch_examples(self):
        for func in pymaid.fetch.__all__:
            # Some functions have dangerous examples!
            f = getattr(pymaid.fetch, func)
            doctest.run_docstring_examples(f, globals(), name=f)

    def test_user_stats_examples(self):
        for func in pymaid.user_stats.__all__:
            f = getattr(pymaid.user_stats, func)
            doctest.run_docstring_examples(f, globals(), name=f)
