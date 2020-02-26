from setuptools import setup, find_packages

setup(
    name='BaseballSimulator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pint',
        'torch==1.3.0',
        'plotly',
        'pyyaml',
        'numpy',
        'scipy',
    ],
)
