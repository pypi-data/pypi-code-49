import setuptools
import kwollect

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kwollect",
    version=kwollect.__version__,
    author="Simon Delamare",
    author_email="simon.delamare@ens-lyon.fr",
    description="Kwollect framework for metrics collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.inria.fr/delamare/kwollect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
    install_requires=["pyonf", "psycopg2", "jwt", "pyyaml", "aiopg", "pysnmp"],
    package_data={"kwollect": ["tools/*"]},
    entry_points={
        "console_scripts": [
            "kwollector = kwollect.kwollector:main",
            "kwollector-wattmetre = kwollect.kwollector_wattmetre:main",
        ]
    },
)
