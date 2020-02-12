import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="medianasms",
    version="1.1.0",
    author="Asghar Dadashzadeh",
    author_email="a.dadashzadeh@mediana.ir",
    description="medianasms sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/medianasms/python-rest-sdk",
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.4.1'],
    license='BSD-2-Clause',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
