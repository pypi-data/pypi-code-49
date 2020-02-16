'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="hyper_status",
    version="1.3",
    author="Xithrius",
    author_email="xithrius@example.com",
    description="A status indicator that you can modify.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xithrius/hyper-status",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
