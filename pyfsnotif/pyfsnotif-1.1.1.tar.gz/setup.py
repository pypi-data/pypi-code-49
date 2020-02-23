from os.path import join, dirname, abspath

from setuptools import setup, find_packages

from pyfsnotif import __version__


curdir = abspath(dirname(__file__))
readme = open(join(curdir, 'README.rst')).read()

setup(
    name             = 'pyfsnotif',
    version          = __version__,
    description      = 'inotifier',
    long_description = readme,
    keywords         = ['utility', ],
    url              = 'https://gitlab.com/dugres/pyfsnotif/tree/stable',
    author           = 'Louis RIVIERE',
    author_email     = 'louis@riviere.xyz',
    license          = 'MIT',
    classifiers      = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    package_dir = {
        'pyfsnotif': 'pyfsnotif',
    },
    packages = [
        'pyfsnotif',
    ],
    entry_points = dict(
        console_scripts = (
            'on_change=pyfsnotif.command:on_change',
        ),
    ),
)
