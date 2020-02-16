import setuptools

setuptools.setup(
    name="pylogpresso",
    version="0.1.1",
    license='Apache Software License 2',
    author="Logpresso",
    author_email="support@logpresso.com",
    description="Python client library for logpresso",
    long_description=open('README.md').read(),
    url="https://github.com/logpresso/pylogpresso",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)