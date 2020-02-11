# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['numpoly',
 'numpoly.array_function',
 'numpoly.construct',
 'numpoly.poly_function']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16,<2.0']

setup_kwargs = {
    'name': 'numpoly',
    'version': '0.1.7',
    'description': 'Polynomials as a numpy datatype',
    'long_description': '.. image:: doc/.static/numpoly_logo.svg\n   :height: 300 px\n   :width: 300 px\n   :align: center\n\n|circleci| |codecov| |pypi| |readthedocs|\n\n.. |circleci| image:: https://circleci.com/gh/jonathf/numpoly/tree/master.svg?style=shield\n    :target: https://circleci.com/gh/jonathf/numpoly/tree/master\n.. |codecov| image:: https://codecov.io/gh/jonathf/numpoly/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/jonathf/numpoly\n.. |pypi| image:: https://badge.fury.io/py/numpoly.svg\n    :target: https://badge.fury.io/py/numpoly\n.. |readthedocs| image:: https://readthedocs.org/projects/numpoly/badge/?version=master\n    :target: http://numpoly.readthedocs.io/en/master/?badge=master\n\nNumpoly is a generic library for creating, manipulating and evaluating\narrays of polynomials.\n\nThe polynomial base class ``numpoly.ndpoly`` is a subclass of ``numpy.ndarray``\nimplemented to represent polynomials as array element. This makes the library\nvery fast with the respect of the size of the coefficients. It is also adds\ncompatibility with ``numpy`` functions and methods, where that makes sense,\nmaking the interface more intuitive.\n\nMany numerical analysis, polynomial approximations as proxy predictors for real\npredictors to do analysis on. These models are often solutions to non-linear\nproblems discretized with high mesh. As such, the corresponding polynomial\napproximation consist of high number of dimensions and large multi-dimensional\npolynomial coefficients. For these kind of problems ``numpoly`` is a good fit.\n\nOne example where ``numpoly`` is used as the backend is the uncertainty\nquantification library `chaospy <https://github.com/jonathf/chaospy>`_.\n\n.. contents:: Table of Contents:\n\nInstallation\n------------\n\nInstallation should be straight forward:\n\n.. code-block:: bash\n\n    pip install numpoly\n\nAnd you should be ready to go.\n\nExample usage\n-------------\n\nConstructing polynomial is typically done using one of the available\nconstructors:\n\n.. code-block:: python\n\n   >>> numpoly.monomial(start=0, stop=4, names=("x", "y"))\n   polynomial([1, y, x, y**2, x*y, x**2, y**3, x*y**2, x**2*y, x**3])\n\nIt is also possible to construct your own from symbols:\n\n.. code-block:: python\n\n   >>> x, y = numpoly.symbols("x y")\n   >>> numpoly.polynomial([1, x**2-1, x*y, y**2-1])\n   polynomial([1, -1+x**2, x*y, -1+y**2])\n\nOr in combination with numpy objects using various arithmetics:\n\n.. code-block:: python\n\n   >>> x**numpy.arange(4)-y**numpy.arange(3, -1, -1)\n   polynomial([1-y**3, x-y**2, x**2-y, -1+x**3])\n\nThe constructed polynomials can be evaluated as needed:\n\n.. code-block:: python\n\n   >>> poly = 3*x+2*y+1\n   >>> poly(x=y, y=[1, 2, 3])\n   polynomial([3+3*y, 5+3*y, 7+3*y])\n\nOr manipulated using various numpy functions:\n\n.. code-block:: python\n\n   >>> numpy.reshape(x**numpy.arange(4), (2, 2))\n   polynomial([[1, x],\n               [x**2, x**3]])\n   >>> numpy.sum(numpoly.monomial(13, names="z")[::3])\n   polynomial(1+z**3+z**6+z**9+z**12)\n\nIn addition there are also several operators specific to the polynomial:\n\n.. code-block:: python\n\n   >>> numpoly.diff([1, x, x**2], x)\n   polynomial([0, 1, 2*x])\n   >>> numpoly.gradient([x*y, x+y])\n   polynomial([[y, 1],\n               [x, 1]])\n\nDevelopment\n-----------\n\nDevelopment is done using `Poetry <https://poetry.eustace.io/>`_ manager.\nInside the repository directory, install and create a virtual environment with:\n\n.. code-block:: bash\n\n   poetry install\n\nTo run tests, run:\n\n.. code-block:: bash\n\n   poentry run pytest numpoly test doc --doctest-modules\n\nQuestions & Troubleshooting\n---------------------------\n\nFor any problems and questions you might have related to ``numpoly``, please\nfeel free to file an `issue <https://github.com/jonathf/numpoly/issues>`_.\n',
    'author': 'Jonathan Feinberg',
    'author_email': 'jonathf@gmail.com',
    'url': 'https://github.com/jonathf/numpoly',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
