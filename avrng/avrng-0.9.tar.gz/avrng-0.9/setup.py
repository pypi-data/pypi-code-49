import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="avrng",
    version="0.9",
    author="Emilie Ma",
    author_email="kewbish@gmail.com",
    description="An AVRNG implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kewbish/csrng",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        'pydub==0.23.1',
        'pyskein==1.0',
        'scenedetect==0.5.1.1',
    ],
)
