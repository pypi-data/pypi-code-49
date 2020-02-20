import os
from distutils.spawn import find_executable

from setuptools import setup, find_packages

from pdfconfig import __version__


def include_readme():
    try:
        import pandoc
    except ImportError:
        return ''
    pandoc.core.PANDOC_PATH = find_executable('pandoc')
    readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
    doc = pandoc.Document()
    with open(readme_file, 'r') as rf:
        doc.markdown = rf.read()
        return doc.rst


setup(
    name='pdf-config',
    version=__version__,
    packages=find_packages(),
    install_requires=['fire', 'PyPDF4', 'PyYAML'],
    url='https://github.com/merll/pdf-config',
    license='MIT',
    author='Matthias Erll',
    author_email='matthias@erll.de',
    description='Merges PDF files into one using a YAML configuration file.',
    long_description=include_readme(),
    platforms=['OS Independent'],
    keywords=['pdf', 'yaml'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        "console_scripts": [
            "pdfconfig = pdfconfig.main:run",
        ],
    }
)
