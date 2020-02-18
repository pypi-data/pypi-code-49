from lentach import __author__, __version__, __license__, __url__
from setuptools import setup


with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lentach',
    version=__version__,
    python_requires='>=3.6',
    packages=['lentach'],
    package_dir={'lentach': 'lentach'},
    url=__url__,
    license=__license__,
    author=__author__,
    description='Fully asynchronous API wrapper for lenta.ru',
    long_description=long_description,
    install_requires=[
        'httpx==0.11.1'
    ],
    keywords=['lenta.ru', 'лента', 'lentach', 'api', 'wrapper', 'async'],
    zip_safe=False,
    classifiers=[
            'Development Status :: 1 - Planning',
            'Framework :: AsyncIO',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7'
    ]
)