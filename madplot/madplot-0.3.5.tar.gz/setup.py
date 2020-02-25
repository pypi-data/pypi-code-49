import os.path
import re
from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open(os.path.join('madplot', '__init__.py')) as f:
    version = re.match(r"version = '([0-9]+[.][0-9]+([.][0-9]+)?)'", f.readline()).group(1)

setup(
    name='madplot',
    version=version,
    description='Plot MAD output (and more).',
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords=['MAD', 'MADX', 'accelerator', 'design', 'interface', 'plot', 'simulation', 'visualization'],
    url='https://gitlab.com/Dominik1123/madplot',
    author='Dominik Vilsmeier',
    author_email='d.vilsmeier@gsi.de',
    license='MIT',
    packages=[
        'madplot',
        'madplot.madx',
    ],
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False
)
