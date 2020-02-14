__all__ = ["test_internals"]
import unittest


def test_internals_(verbosity=2):
    from VEnCode.tests import test_internals

    suite = unittest.TestLoader().loadTestsFromModule(test_internals)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)