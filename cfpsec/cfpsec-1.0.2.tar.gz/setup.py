import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cfpsec',
    version='1.0.2',
    packages=['cfpsec'],
    scripts=['cfpsec/cfpsec.py'],
    author="Alexandre Borges",
    author_email="alexandreborges@blackstormsecurity.com",
    description="CFPsec lists Call For Papers or upcoming Hacking/Security Conferences based on cfptime.org website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexandreborges/cfpsec",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    python_requires='>=3.7',
    install_requires = [
        "colorama >= 0.4.3",
        "simplejson >= 3.17.0",
        "requests >= 2.22.0",
        "argparse >= 1.4.0",
    ],
)
