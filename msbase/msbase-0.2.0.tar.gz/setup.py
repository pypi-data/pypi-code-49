import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="msbase",
    version="0.2.0",
    author="Zhen Zhang",
    author_email="pip@zhen-zhang.com",
    description="Base Library for Python for MySelf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/izgzhen/msbase.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required
)
