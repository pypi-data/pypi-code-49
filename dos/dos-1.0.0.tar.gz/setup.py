import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dos",
    version="1.0.0",
    author="Peter Richards",
    author_email="prichards@cap-rx.com",
    description="Document and Validate Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pr/dos",
    install_requires=[
        "arrow",
        "flask"
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "json"
    ],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)