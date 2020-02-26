import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ezdnac",
    version="0.0.14",
    author="Johan Lahti",
    author_email="ccie60702@gmail.com",
    description="A small module to make it easy to start using the rest-api of Cisco DNA-C",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johan-lahti/ezdnac",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests','tabulate'],
    python_requires='>=3.6',
)
