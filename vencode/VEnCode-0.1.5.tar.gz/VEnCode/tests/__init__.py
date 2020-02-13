__all__ = ["test_internals"]
import unittest


def test_internals_():
    from VEnCode.tests import test_internals

    suite = unittest.TestLoader().loadTestsFromModule(test_internals)
    unittest.TextTestRunner(verbosity=2).run(suite)