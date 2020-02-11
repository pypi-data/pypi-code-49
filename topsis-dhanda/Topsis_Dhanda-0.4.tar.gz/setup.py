import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis_Dhanda", # Replace with your own username
    version="0.4",
    author="Nishant Dhanda",
    author_email="dhandanishant012@gmail.com",
    description="A small package that showcases Topsis approach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NishantDhanda/Topsis-Python.git",
    download_url="https://github.com/NishantDhanda/Topsis-Python/archive/0.01.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['Topsis=Topsis_Python.cli:main'],
    },
    python_requires='>=3.6',
)
