import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [line.strip()
                    for line in open("requirements.txt").readlines()]

setuptools.setup(
    name='wallet_lib',
    version='1.2.2',
    author="Bitcoin.com",
    author_email="gamesbot@bitcoin.com",
    description="Package to work with hot wallet for different cryptocurrency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bitcoin-com/wallet_lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    python_requires='>=3.6'
)
