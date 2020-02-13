import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="srcsrv",
    version="1.1.0",
    author="Uri Mann",
    author_email="abba.mann@gmail.com",
    description="Source indexing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 4 - Beta"
    ],
    install_requires=[
        'GitPython', 'svn'
    ],
    python_requires='>=3.6',
    packages=['srcsrv', 'srcsrv.plugins'],
    package_dir={'srcsrv': 'srcsrv'}
)