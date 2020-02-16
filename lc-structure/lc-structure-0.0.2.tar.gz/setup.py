import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='lc-structure',
    version='0.0.2',
    author='Singwai Chan',
    author_email='c.singwai@gmail.com',
    description='A tool to create linked list, binary tree and graph from array or dictionary for the ease of local test',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/singwai/lc-structure',
    packages=setuptools.find_packages(),
    keywords="LeetCode",
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
