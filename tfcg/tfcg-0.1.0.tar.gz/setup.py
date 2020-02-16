import os
import re
import setuptools
from pathlib import Path

p = Path(__file__)

setup_requires = [
    'numpy',
    'pytest-runner'
]

install_requires = [
    'networkx',
    'google'
]
test_require = [
    'pytest-cov',
    'pytest-html',
    'pytest'
]

setuptools.setup(
    name="tfcg",
    version='0.1.0',
    python_requires='>3.5',
    author="Koji Ono",
    author_email="kbu94982@gmail.com",
    description="tf_conceptual_graph",
    url='https://github.com/0h-n0/tfcg',
    # long_description=(p.parent / 'README.md').open(encoding='utf-8').read(),
    long_description="Tf_Conceptual_Graph",
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=test_require,
    extras_require={
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme']},
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
