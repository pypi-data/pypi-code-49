from os.path import join, dirname, abspath

from setuptools import setup, find_packages

from caty import __version__

curdir = abspath(dirname(__file__))
readme = open(join(curdir, 'README.rst')).read()

setup(
    name             = 'caty',
    version          = __version__,
    description      = 'Nice cat.',
    long_description = readme,
    keywords         = ['utility', ],
    url              = 'https://gitlab.com/dugres/caty/tree/stable',
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
    install_requires = [
        'nicely',
        'binview',
    ],
    package_dir = {
        'caty': 'caty',
    },
    packages = [
        'caty',
    ],
    entry_points = dict(
        console_scripts = (
            'caty=caty.cli:main',
        ),
    ),
)
