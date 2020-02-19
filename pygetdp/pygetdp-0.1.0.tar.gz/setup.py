import codecs
import os

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "pygetdp", "__about__.py"), "rb") as f:
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()


with open("requirements.txt") as f:
    required = f.read().splitlines()
setup(
    name="pygetdp",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=find_packages(),
    description=about["__description__"],
    long_description=read("README.rst"),
    url=about["__website__"],
    project_urls={"Documentation": about["__webdoc__"]},
    license=about["__license__"],
    python_requires=">=3",
    install_requires=["pygments", "pillow"],
    extras_require={"test": ["pytest-cov"], "doc": ["matplotlib"]},
    platforms="any",
    entry_points="""[pygments.styles]
                    prostyle = pygetdp.rendering:ProStyle
                    [pygments.lexers]
                    prolexer = pygetdp.rendering:CustomLexer
                    """,
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
