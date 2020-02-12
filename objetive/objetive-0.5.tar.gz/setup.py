import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='objetive', 
    version='0.5',
    author="Julio Lira",
    author_email="jul10l1r4@disroot.org",
    description="A mini-crawler that aims to grab some text parts from some website or ip that responds http* ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jul10l1r4/objetive",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        ],
    )
