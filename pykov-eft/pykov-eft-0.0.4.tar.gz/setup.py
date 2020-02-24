import setuptools

with open("pykov/README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pykov-eft",
    version="0.0.4",
    author="Xpheriono",
    author_email="",
    description="A Python API for Escape From Tarkov",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xpheriono/pykov",
    packages=setuptools.find_packages(exclude=['example.*', '.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)