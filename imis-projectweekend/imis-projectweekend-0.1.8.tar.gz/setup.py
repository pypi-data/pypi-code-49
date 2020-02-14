import setuptools

setuptools.setup(
    name="imis-projectweekend", # Replace with your own username
    version="0.1.8",
    author="Brian Hines",
    author_email="brian@projectweekend.net",
    description="A Python client for the iMIS REST API",
    long_description="A Python client for the iMIS REST API",
    url="https://github.com/projectweekend/imis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ],
    python_requires='>=3.6',
)
