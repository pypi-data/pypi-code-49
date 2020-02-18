from setuptools import setup
from os import path

BASE_DIR = path.abspath(path.dirname(__file__))

with open(path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='ipython-dawet-sql',
    version='0.1b6',
    packages=['dawetsql'],
    url='https://gitlab.com/wakataw/ipython-dawet-sql',
    license='MIT',
    author='Agung Pratama',
    author_email='agungpratama1001@gmail.com',
    description='Ipython ODBC SQL Magic for Dawet',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Natural Language :: Indonesian',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License'
    ],
    install_requires=[
        'pandas',
        'pypyodbc',
        'ipython',
        'ipywidgets',
        'cryptography',
        'xlsxwriter'
    ],
    python_requires='>=3.5',
)
