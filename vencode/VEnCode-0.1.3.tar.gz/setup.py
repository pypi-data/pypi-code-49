import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='VEnCode',
    version='0.1.3',
    description='Package to get VEnCodes as in Macedo and Gontijo, 2019',
    author='Andre Macedo and Alisson M. Gontijo',
    author_email='andre.lopes.macedo@gmail.com',
    url='https://github.com/AndreMacedo88/VEnCode',
    packages=setuptools.find_packages(),
    install_requires=[
        "biopython",
        "tqdm",
        "numpy",
        "pandas",
        "matplotlib",
        "scipy"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
