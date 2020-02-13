
"""
unit testing wrapper
"""

# pylint: disable=C0103

import sys
import os
import os.path as opath
import inspect
import unittest
import getopt
from collections import OrderedDict
import importlib


import coverage


class Common(object):
    """
    classmethod goes here
    """

    @classmethod
    def setUpClass(cls):
        """setUpClass stub"""

    @classmethod
    def tearDownClass(cls):
        """tearDownClass stub"""


def usage(errno=0, errmsg=None):
    """
    Usage.
    """
    if errmsg:
        sys.stderr.write("ERROR: %s\n" % errmsg)
    print("Usage: choba [-hl] [-s <submodule>] [-f <filter>] <dir>")
    sys.exit(errno)


def load_tests(test_dir):
    """
    Load all modules with eligible tests and their respective
    methods.
    """

    # insert test directory to path
    sys.path.insert(0, test_dir)

    # dynamically import all test modules if applies
    incl = []
    for root, _, files in os.walk(test_dir):
        for fname in files:
            # *.py only
            if not fname.endswith('.py'):
                continue
            base = opath.join(root, fname)
            # remove root path
            base = base[len(test_dir) + 1:][0:-3]
            # slashdot
            base = base.replace('/', '.')
            # skip underscore-prefixed stuff
            if base.startswith('_'):
                continue
            # remove __init__
            if base.endswith('__init__'):
                base = base[0:-9]
            try:
                # dinaymic import
                incl.append(importlib.import_module((base)))
            except (ValueError, ImportError):
                pass

    # filter out modules without tests
    tests = []
    for module in incl:
        mdl = module.__name__
        test = {}
        for clsname, cls in inspect.getmembers(module):
            if not cls or not clsname.startswith('Test'):
                continue
            test[clsname] = {
                'class': cls,
                'methods': [],
            }
            for name, _ in inspect.getmembers(cls):
                if not name.startswith('test_'):
                    continue
                test[clsname]['methods'].append(name)
        if test:
            tests += [(mdl, test)]
    return OrderedDict(tests)


def select_tests(tests, submodule=None):
    """
    Only select a submodule from all available tests.
    """
    if submodule is None:
        return tests
    selected = OrderedDict({})
    if submodule not in tests:
        return usage(1, "Test submodule '%s' not found." % submodule)
    selected[submodule] = tests[submodule]
    return selected


def filter_tests(tests, mfilter=None):
    """
    Filter tests against a string.
    """
    if mfilter is None:
        return tests
    for mdlname, mdl in tests.items():
        for clsname, cls in mdl.items():
            tests[mdlname][clsname]['methods'] = (
                x for x in cls['methods'] if mfilter in x)
    return tests


def list_tests(tests):
    """
    List selected tests.
    """
    for mdlname, mdl in tests.items():
        for clsname, cls in mdl.items():
            for name in cls['methods']:
                print("%s.%s.%s" % (mdlname, clsname, name))


def run_tests(tests, cov):
    """
    Run tests.
    """
    # start coverage
    cov.start()

    # initialize suite
    suite = unittest.TestSuite()

    # add methods to suite
    for mdl in tests.values():
        for clsname, cls in mdl.items():
            # create compound of test class and Common
            compound = type(clsname, (Common, cls['class']), {})
            # add each method associated with test class to suite
            for method in cls['methods']:
                suite.addTest(compound(method))

    # run suite
    run = unittest.TextTestRunner(verbosity=2).run(suite)

    # stop coverage
    cov.stop()
    cov.save()

    # generate HTML report
    cov.html_report()

    # generate cobertura report
    cov.xml_report()

    return run


def main():
    """
    Main.
    """
    # initialize
    is_listing = False
    submodule = None
    mfilter = None
    test_dir = None

    # getopt
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], 'hls:f:',
            ['help', 'list', 'submodule=', 'filter='])
        for opt, val in opts:
            # options
            if opt in ('-h', '--help'):
                return usage(0)
            if opt in ('-l', '--list'):
                is_listing = True
            if opt in ('-s', '--submodule'):
                submodule = val
            if opt in ('-f', '--filter'):
                mfilter = val
        try:
            _dir = opath.abspath(args[0])
            if not opath.isdir(_dir):
                return usage(1, "Invalid test directory: '%s'." % _dir)
            test_dir = opath.abspath(_dir)
        except IndexError:
            pass
    except getopt.GetoptError:
        return usage(1)

    if test_dir is None:
        return usage(1, "Test directory not set.")

    # start coverage before test module imports so that function
    # definitions are included; assumes .coveragerc on curdir;
    # branch coverage is always true
    cov = coverage.Coverage(config_file=True, branch=True)
    cov.start()

    # load modules
    tests = load_tests(test_dir)

    # select a module if applicable
    tests = select_tests(tests, submodule)

    # filter methods if applicable
    tests = filter_tests(tests, mfilter)

    # listing only
    if is_listing:
        return list_tests(tests)

    # run tests
    run = run_tests(tests, cov)

    if not run.wasSuccessful():
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
