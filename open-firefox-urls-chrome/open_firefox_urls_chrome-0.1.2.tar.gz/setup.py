from setuptools import setup
from os import path


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()

setup(
    name='open_firefox_urls_chrome',
    version='0.1.2',
    url='https://github.com/robmcelhinney/open-firefox-urls-chrome',
    download_url='https://github.com/robmcelhinney/open-firefox-urls-chrome/archive/0.1.2.tar.gz',
    license='MIT',
    author='Robert McElhinney',
    author_email='robmcelhinney@hotmail.com',
    description='Utility to get URLs currently open in Firefox and open them in Chrome',
    long_description=open('README.md').read(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='firefox chrome util commandline',
    install_requires=['lz4', 'psutil'],
    py_modules=['open_firefox_urls_chrome'],
    entry_points={
        'console_scripts': [
            'open-firefox-urls-chrome=open_firefox_urls_chrome:main',
        ],
    },
    scripts=['bin/open_firefox_urls_chrome'],
)
