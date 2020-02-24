import hein_utilities
from setuptools import setup, find_packages

NAME = 'hein_utilities'
AUTHOR = 'Lars Yunker / Hein Group'

PACKAGES = find_packages()
# KEYWORDS = ', '.join([
# ])

with open('LICENSE') as f:
    lic = f.read()
    lic.replace('\n', ' ')

with open('README.MD', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=hein_utilities.__version__,
    description='Methods and Classes used in a variety of Hein projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    url='https://gitlab.com/heingroup/hein_utilities',
    packages=PACKAGES,
    license=lic,
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Operating System :: Microsoft :: Windows',
        'Natural Language :: English'
    ],
    # keywords=KEYWORDS,
    install_requires=[
        'numpy',
        'slackclient'
    ],
)
