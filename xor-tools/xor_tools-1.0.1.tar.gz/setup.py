import os
import setuptools


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="xor_tools",
    version="1.0.1",
    python_requires='>3.5.2',
    url='https://github.com/lukaskuzmiak/xor_tools',
    author="Lukas Kuzmiak, nshadov",
    author_email="lukash@backstep.net",
    description="XOR Tools",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="xor key recovery encrypt decrypt",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'xor_key_recovery=xor_tools.xor_key_recovery:main',
            'xor_encrypt_file=xor_tools.xor_encrypt_file:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
