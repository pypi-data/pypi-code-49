#!/usr/bin/env python

"""
Run all tests of the project.
"""

import unittest

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015, 2018, 2019, 2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"


if __name__ == "__main__":
    loader = unittest.TestLoader()

    print(r"""
Classic Recurrence Plot Tests
=============================
""")

    recurrence_plot_suite = unittest.TestSuite()
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.TestRPFixedRadiusClassic'))
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.TestRPRadiusCorridorClassic'))

    unittest.TextTestRunner(verbosity=2).run(recurrence_plot_suite)

    print(r"""
Cross Recurrence Plot Tests
===========================
""")

    recurrence_plot_suite = unittest.TestSuite()
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.TestRPFixedRadiusCross'))
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.TestRPRadiusCorridorCross'))

    unittest.TextTestRunner(verbosity=2).run(recurrence_plot_suite)

    print("""
Classic RQA Tests
=================
""")

    rqa_suite = unittest.TestSuite()
    rqa_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.TestRQAFixedRadiusClassic'))
    rqa_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.TestRQARadiusCorridorClassic'))

    unittest.TextTestRunner(verbosity=2).run(rqa_suite)

    print("""
Cross RQA Tests
===============
""")

    rqa_suite = unittest.TestSuite()
    rqa_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.TestRQAFixedRadiusCross'))
    rqa_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.TestRQARadiusCorridorCross'))

    unittest.TextTestRunner(verbosity=2).run(rqa_suite)
