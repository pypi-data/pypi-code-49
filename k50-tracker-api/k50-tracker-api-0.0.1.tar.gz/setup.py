from setuptools import setup, find_packages
from k50_tracker import __version__


setup(
    name='k50-tracker-api',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'requests>=2.18.2',
    ],
    description='K50 tracker api wrapper',
    author='bzdvdn',
    author_email='bzdv.dn@gmail.com',
    url='https://github.com/bzdvdn/comagic-sdk',
    license='MIT',
    python_requires=">=3.6",
)