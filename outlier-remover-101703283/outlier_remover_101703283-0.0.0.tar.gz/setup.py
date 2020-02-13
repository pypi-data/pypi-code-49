from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name="outlier_remover_101703283",
	version='0.0.0',
	author='Katinder Kaur',
	author_email='katinder08@gmail.com',
	description='python package for removing outliers from multi-variate data',
	long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.python.org/pypi/outlier_remover_101703283",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'outlier_remover=outlier_remover.outlier_remover:main'
        ]
    },
    install_requires=["numpy", "pandas","argparse"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	)