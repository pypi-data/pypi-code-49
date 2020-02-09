import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws_lambda_cors",
    version="0.0.3",
    author="Adrian Pina",
    author_email="adrian@quesadillalab.mx",
    description="An AWS Lambda response package utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/adrian-pina/aws-lambda-cors",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)