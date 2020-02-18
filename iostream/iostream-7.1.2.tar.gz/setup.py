from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="iostream",  # Replace with your own username
    version="7.1.2",
    author="CubieLee",
    author_email="liyixiao0608@163.com",
    description="iostream for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.cubie.xyz:1228",
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
