import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='filepaths',
    version="0.0.7",
    author='Hunter Feiss',
    author_email='hfeiss@gmail.com',
    description='Root-agnostic filepath generation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hfeiss/filepaths',
    packages=setuptools.find_packages(),
    install_requires=['addict'],
    license='MIT',
    keywords='filepath files directories',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)