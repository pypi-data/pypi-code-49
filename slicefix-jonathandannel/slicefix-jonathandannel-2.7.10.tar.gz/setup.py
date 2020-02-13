import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slicefix-jonathandannel", # Replace with your own username
    version="2.7.10",
    author="Jonathan Dannel",
    author_email="usixjad@gmail.com",
    description="A simple script for formatting Photoshop HTML generated from image slicing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonathandannel/slicefixx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
    'bs4',
    'datetime'
    ],
    scripts=[
      'bin/slicefix.py'
    ],
    entry_points={
        "console_scripts": [
            "slicefix = slicefix:fix_and_save",
        ]
    } 
)