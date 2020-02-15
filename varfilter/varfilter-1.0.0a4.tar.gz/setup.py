import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="varfilter",
    version="1.0.0a4",
    author="Esteban Barón",
    author_email="esteban@gominet.net",
    description="filtra variables de distintas fuentes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gomibaya/pyVarfilter/",
    packages=setuptools.find_packages(),
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
