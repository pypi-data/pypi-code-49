import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drhttp",
    version="0.2.0",
    author="Pierre-Olivier Marec",
    author_email="contact@drhttp.com",
    description="Dr. Ashtetepe (drhttp) agent for python application servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://drhttp.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.22.*',
    ],
)