import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ttsDeckMaker-pkg-Biduleman",  # Replace with your own username
    version="0.0.6",
    author="Biduleman",
    author_email="biduleman@gmail.com",
    description="MTG Deck Maker for Tabletop Simulator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['Pillow', 'scrython', 'urllib3', 'requests']
)
