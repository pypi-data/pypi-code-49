# coding: utf-8

from __future__ import print_function, absolute_import, division, unicode_literals

_package_data = dict(
    full_package_name='tox-globinterpreter',
    version_info=(0, 4, 0),
    __version__='0.4.0',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='tox plugin to allow specification of interpreter locationspaths to use',  # NOQA
    entry_points=None,
    since=2015,
    license='MIT',
    install_requires=['tox'],
    classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing :: Markup',
    ],
    keywords='test tox',
    #read_the_docs='tox-globinterpreter',
    supported=[(2, 7), (3, 5)],  # minimum
    #tox=dict(
    #    env='*',  # remove 'pn', no longer test narrow Python 2.7 for unicode patterns and PyPy
    #    deps='ruamel.std.pathlib',
    #    fl8excl='_test/lib',
    #),
    universal=True,
    print_allowed=True,
    #rtfd='tox-globinterpreter',
)
