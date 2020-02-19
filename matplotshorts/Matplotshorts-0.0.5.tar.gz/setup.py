import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Matplotshorts",
	license='MIT',
    version="0.0.5",
    author="Dennis Maier",
    author_email="dennis@dennis-maier.de",
    description="Usefull wrapper methods for matplot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
	install_requires=[            # I get to this in a second
          'matplotlib',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)