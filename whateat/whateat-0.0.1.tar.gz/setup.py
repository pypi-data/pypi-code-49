import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whateat",
    version="0.0.1",
    author="Alex Ye",
    author_email="alexzye1@gmail.com",
    description="what should i eat?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/azye/whateat",
    scripts=['./scripts/whateat'],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
