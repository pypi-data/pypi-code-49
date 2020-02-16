# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfixm']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.5.0,<5.0.0', 'six>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'pyfixm',
    'version': '0.1.2',
    'description': 'Parses FIXM data into Python datastructures',
    'long_description': 'About\n=====\npyfixm is a library that contains Python wrappers for the FIXM_ XML Schemas,\nplus the `US NAS extension`_ for the FAA. Currently the library is built for\nFIXM v3.0, as this is what the FAA uses to publish data through SWIM_.\n\nUsage\n=====\n\n.. code-block:: python3\n\n    import pyfixm\n    xml = pyfixm.parse("./fixm_file.xml")\n\nBuilding pyfixm manually\n========================\nTo build ``pyfixm`` either use the suppled ``build-pyfixm`` PyCharm run\nconfiguration or by manually running ``scripts/build.py``. Both methods build\nthe library within a Docker image and then extract the built library to\n``./pyfixm`` on the host computer. Reminder to install Docker if you haven\'t\nalready.\n\nLicense\n=======\nThis project has two licenses. Because really what this repository creates is a\ntranspilation of the FIXM XSD files, the generated library is treated as a\ndistribution of the upstream and not a novel codebase and assumes no further\ncopyright with the built library. Both components are licensed under the BSD\n3-Clause, but the copyright holder is different.\n\nSource Repo\n-----------\nThe ``pyfixm`` library-generating source code is licensed under the BSD 3-Clause\nlicense.\n\nGenerated Library\n-----------------\nThe generated library (the part that gets published to PyPI) is licensed under\nthe same license as the upstream FIXM XSD files. Note that the copyright is\nattributed to the FIXM copyright holders to avoid any copyright complexities.\n\n.. _SWIM: https://www.faa.gov/air_traffic/technology/swim/overview/\n.. _US NAS extension: https://www.fixm.aero/content/extensions.pl\n.. _FIXM: https://www.fixm.aero/\n',
    'author': 'Bryce Beagle',
    'author_email': None,
    'maintainer': 'Tyler Compton',
    'maintainer_email': None,
    'url': 'https://github.com/sync-or-swim/pyfixm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
