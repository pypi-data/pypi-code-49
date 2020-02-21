import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplematrixlib",
    version="0.4.0",
    author="Tim Stahel",
    author_email="simplematrixlib@swedneck.xyz",
    description="A simple python library for using \
                 the matrix client-server API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Swedneck/simplematrixlib",
    packages=setuptools.find_packages(),
    install_requires=[
        'configargparse',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
