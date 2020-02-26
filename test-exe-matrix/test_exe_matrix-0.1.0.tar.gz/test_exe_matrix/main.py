import argparse
import os

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

import pytest


__version__ = importlib_metadata.version("test_exe_matrix")


DEFAULT_TESTSUITE_NAME = "example_testsuites"


class PytestArg(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        pytest_args = getattr(namespace, self.dest, [])
        if pytest_args is None:
            pytest_args = []
        pytest_args.append(option_string)
        pytest_args += values
        setattr(namespace, self.dest, pytest_args)


def _run_one_suite(args, codedir, testsuite):
    fullargs = [codedir, "--testsuite", testsuite]
    if args.pytest_args:
        fullargs += args.pytest_args
    pytest.main(fullargs)


def entrypoint():

    parser = argparse.ArgumentParser(
        description="Test command lines listed in yaml files.",
        epilog="%(prog)s is mainly a Py.test wrapper",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    parser.add_argument(
        "--collect-only",
        action=PytestArg,
        dest="pytest_args",
        nargs=0,
        help="Only collect tests, without running them.",
    )
    parser.add_argument(
        "-v", action=PytestArg, dest="pytest_args", nargs=0, help="Increase verbosity."
    )
    parser.add_argument(
        "--markers",
        action=PytestArg,
        dest="pytest_args",
        nargs=0,
        help="Lists registered test markers.",
    )
    parser.add_argument(
        "-m",
        action=PytestArg,
        dest="pytest_args",
        nargs=1,
        help="""Only run tests that match selection expression, """
        """ie. '-m "not internet"'""",
    )
    codedir = os.path.dirname(os.path.realpath(__file__))
    default_file = os.path.join(codedir, DEFAULT_TESTSUITE_NAME)
    parser.add_argument(
        "testsuite",
        nargs="*",
        help=f"testsuite yaml file -see example {default_file}. Argument can "
        "be specified multiple times. Argument can be a directory containing"
        "test suites.",
        default=[default_file],
    )
    args = parser.parse_args()

    for testsuite in args.testsuite:
        if not os.path.exists(testsuite):
            raise OSError("No such file or directory: {}".format(testsuite))
        if not os.path.isdir(testsuite):
            _run_one_suite(args, codedir, testsuite)
            continue
        for suite_in_dir in os.listdir(testsuite):
            if not os.path.splitext(suite_in_dir)[1] in (".yml", ".yaml"):
                continue
            _run_one_suite(args, codedir, os.path.join(testsuite, suite_in_dir))
