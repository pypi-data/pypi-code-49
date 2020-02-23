from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pyhost',
    version='0.1.0',
    author='Javier Poremski',
    author_email='javier@poremski.se',
    description='DNS Lookup',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url='https://gitlab.com/drewito/pyhost',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
    ],
    python_requires='>=3.7',
    packages=['pyhost'],
)
