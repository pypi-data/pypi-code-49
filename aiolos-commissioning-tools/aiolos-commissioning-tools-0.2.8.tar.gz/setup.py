import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="aiolos-commissioning-tools",
    version="0.2.8",
    url="https://github.com/csooriyakumaran/aiolos-commissioning-tools",
    license='MIT',

    author="Christopher Sooriyakumaran",
    author_email="c.sooriyakumaran@gmail.com",

    description="data reduction tools for general aerodynamic measurements",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    include_package_data=False,

    install_requires=["numpy", "matplotlib","scipy","pandas"],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
