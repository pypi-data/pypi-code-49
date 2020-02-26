"""pytest magic
"""


import os

import pytest
import yaml


def pytest_addoption(parser):
    parser.addoption(
        "--testsuite",
        help="testsuite.yaml file, see example matrix.yaml",
        default="matrix.yaml",
    )


def pytest_report_header(config):
    filename = os.path.abspath(config.option.testsuite)
    config.option.testsuite = filename
    return f"Tests from {filename}"


def pytest_generate_tests(metafunc):
    filename = metafunc.config.option.testsuite
    if "exetest" in metafunc.fixturenames:
        with open(filename, "rb") as yamlfd:

            testsuite = yaml.load(yamlfd, Loader=yaml.Loader)
            suite_config = testsuite.get("config", {})

            markers = suite_config.get("markers", [])
            for marker in markers:
                metafunc.config.addinivalue_line("markers", marker)
            general_timeout = int(suite_config.get("timeout", 1))

            alltests = testsuite["tests"]
            prepared_tests = []

            for testitem in alltests:
                testitem.setdefault("timeout", general_timeout)

                markers = testitem.get("markers", [])
                prepared = pytest.param(
                    testitem,
                    id=testitem.get("name", testitem["exe"]),
                    marks=[getattr(pytest.mark, marker) for marker in markers],
                )
                prepared_tests.append(prepared)

            metafunc.parametrize("exetest", prepared_tests)
