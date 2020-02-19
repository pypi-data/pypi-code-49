import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timework",
    version="0.2.4",
    author="bugstop",
    author_email="pypi@isaacx.com",
    description="Cross-platform python module to set run time limits "
                "(timer, timeout and iterative deepening) as decorators.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bugstop/timework-timeout-decorator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)