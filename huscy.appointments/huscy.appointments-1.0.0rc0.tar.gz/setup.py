from setuptools import find_namespace_packages, setup

from huscy.appointments import __version__


extras_require = {
    'development': [
        'wheel',
    ],
    "docs": [
        "django-extensions",
        'pydot',
    ],
    'release': [
        'twine',
    ],
    'testing': [
        'tox',
        'watchdog==0.9',
    ],
}


install_requires = [
    "django>=2.1",
    "djangorestframework>=3.10",
    "django-filter>=2",
    "django-ical>=1.6",
]


setup(
    name='huscy.appointments',
    version=__version__,
    license='AGPLv3+',

    author='Alexander Tyapkov, Mathias Goldau, Stefan Bunde',
    author_email='tyapkov@cbs.mpg.de, goldau@cbs.mpg.de, stefanbunde+git@gmail.com',

    packages=find_namespace_packages(),

    install_requires=install_requires,

    extras_require=extras_require,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
    ],
)
