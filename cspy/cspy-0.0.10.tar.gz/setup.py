from setuptools import setup, find_packages

setup(
    name="cspy",
    version="0.0.10",
    description=
    "A collection of algorithms for the (Resource) Constrained Shortest Path Problem",
    license="MIT",
    author="David Torres",
    author_email="d.torressanchez@lancs.ac.uk",
    keywords=[
        "shortest path", "resource constrained shortest path",
        "bidirectional algorithm", "tabu search"
    ],
    long_description_content_type="text/markdown",
    long_description=open("README.rst", "r").read(),
    url="https://github.com/torressa/cspy",
    packages=find_packages(),
    install_requires=['networkx', 'numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
