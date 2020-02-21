import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zsp",
    version="0.0.1",
    author="Szymon Woźniak",
    author_email="s@zymon.org",
    description="zsp",
    url="https://github.com/lab-zymon/zsp",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
