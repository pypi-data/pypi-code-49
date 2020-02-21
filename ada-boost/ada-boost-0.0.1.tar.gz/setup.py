from setuptools import setup, find_packages
import re

with open('ada-boost/__init__.py') as f:
    versionString = re.search(r"__version__ = '(.+)'", f.read()).group(1)

if __name__ == '__main__':
    setup(name='ada-boost',
        version = versionString,
        author="Reid McIlroy-Young",
        author_email="reidmcy@cs.toronto.edu",
        packages = find_packages(),
        install_requires = [
                #'numpy',
                #'matplotlib',
                #'pandas',
                'pytz',
        ]
    )
