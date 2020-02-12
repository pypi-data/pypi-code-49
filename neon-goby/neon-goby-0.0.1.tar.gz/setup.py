import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as reqs:
    requirements = [req.strip() for req in reqs.readlines()]

setuptools.setup(
    name="neon-goby", # Replace with your own username
    version="0.0.1",
    author="HiiYL",
    author_email="hii@saleswhale.com",
    description="A simple package to clean email bodies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    test_requires=[
        'pytest',
        'pytest-cov',
        'pylint'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
