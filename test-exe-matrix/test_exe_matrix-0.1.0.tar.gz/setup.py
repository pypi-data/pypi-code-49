# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_exe_matrix']

package_data = \
{'': ['*'], 'test_exe_matrix': ['example_testsuites/*']}

install_requires = \
['PyYAML>=5.2', 'pytest==5.3.1']

entry_points = \
{'console_scripts': ['test_exe_matrix = test_exe_matrix.main:entrypoint']}

setup_kwargs = {
    'name': 'test-exe-matrix',
    'version': '0.1.0',
    'description': 'Toy project to test executables defined in a yaml file',
    'long_description': '=======================================================\nToy project to test executables defined in a yaml file\n=======================================================\n\nA wrapper around py.test to run your things selectively.\n\nInstallation and running\n-------------------------\n\nMain requirements\n.................\n\n- UNIX like\n- Python 3.6, 3.7 or 3.8\n\nFrom PyPA (pip install)\n........................\n\nHopefully soon. Once I\'m confident that test_exe_matrix is not too trivial anymore.\n\nFrom source with poetry\n........................\n\n.. code-block:: console\n    \n    git clone https://framagit.org/feth/test_exe_matrix.git\n    cd test_exe_matrix\n    poetry install\n\nRun\n\nNote on poetry: you cannot install it from pip, you need to follow\n`the instructions <https://python-poetry.org/docs/>` _\non the `official Web site <https://python-poetry.org/>`_.\n\n--------\n\nIf you installed from source with poetry:\n\n.. code-block:: console\n    \n    poetry run test_exe_matrix [arguments...]\n\nIf you installed from package (see instructions at the end) or ran "pip install <package>" in a virtualenv (unlikely as of today).\n\n.. code-block:: console\n    \n    test_exe_matrix [arguments...]\n\nCommand line options\n.....................\n\nTypical use:\n\n.. code-block:: console\n\n    [poetry run] test_exe_matrix \n\nSynopsys:\n\n.. code-block:: console\n\n    usage: test_exe_matrix [-h] [-V] [--collect-only] [-v] [--markers]\n                           [-m PYTEST_ARGS]\n                           [testsuite [testsuite ...]]\n    \n    Test command lines listed in yaml files.\n    \n    positional arguments:\n      testsuite       testsuite yaml file -see example\n                      test_exe_matrix/matrix.yaml.\n                      Argument can be specified multiple times\n    \n    optional arguments:\n      -h, --help      show this help message and exit\n      -V, --version   show program\'s version number and exit\n      --collect-only  Only collect tests, without running them.\n      -v              Increase verbosity.\n      --markers       Lists registered test markers.\n      -m PYTEST_ARGS  Only run tests that match selection expression, ie. \'-m "not\n                      internet"\'\n    \n    test_exe_matrix is mainly a Py.test wrapper\n\n\n-v adds very nice colors, thanks to py.test.\n\nParametrizing tests\n-------------------\n\nPut your test suites in a yaml, like matrix.yaml (provided), or in several. Every yaml file will have a separate global config (markers declaration and general timeout).\n\nMinimum viable test\n....................\n\n.. code-block:: console\n\n    - exe: /path/to/exe\n\nThe test will succeed if default values are met: see below (optional values).\n\nOptional values\n...............\n\n*timeout*\n  Allowed running time in seconds. Program will be killed after this delay. Default to config/timeout or 1.\n*retcode*\n  Expected return code.\n*stdout*\n  Expected standard output (full match)\n*stderr*\n  Expected standard error (full match)\n*partstdout*\n  Substring expected in standard output.\n*partstderr*\n  Substring expected in standard error.\n*args*\n  List of arguments to your program.\n*name*\n  Description of the test being made.\n*expect_too_long*\n  Boolean: whether the program is expected to run over the time limit.\n*markers*\n  List of markers for the test. You can use standard py.test markers (especially \'xfail\': indicating \'expected failure\') or custom markers, that _must_ be declared in the config section.\n\nExample\n---------\n\nA complete (hopefully) example file is provided as "matrix.yaml".\n\nGiven the examples, you may run \n\n.. code-block:: console\n\n    test_exe_matrix matrix.yaml --collect-only\n\nto list the tests, and\n\n.. code-block:: console\n\n    test_exe_matrix matrix.yaml -v -m "not internet and not slow"\n\nto deselect all tests requiring Internet and slow tests.\n\n.. image:: doc/Screenshot_markers.png\n    :alt: screenshot of the above command and output.\n\nDev: Build the package\n-----------------------\n\nThe project uses poetry. Do\n\n.. code-block:: console\n\n    poetry build\n\nAnd a pip installable wheel package will appear under dist/. For\ninstance, you can install with:\n\n.. code-block:: console\n\n     pip3 install dist/test_exe_matrix-0.0.18-py3-none-any.whl\n\n\nLicence\n-------\n\nCeCILL 2.1 and GPL 2.1, see files LICENSE_CeCILL_2.1.txt and LICENSE_GPL_2.1.txt.\n\nThank you\n----------\n\nSt\xc3\xa9phane Bortzmeyer, who once asked if a simple tool testing the result of commands existed, and then reported bugs/wrote helpful tickets on framagit/gitlab to guide the development.\n',
    'author': 'Feth AREZKI',
    'author_email': 'text_exe_matrix@tuttu.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://framagit.org/feth/test_exe_matrix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
