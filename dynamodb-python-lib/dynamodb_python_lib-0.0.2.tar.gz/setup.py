from setuptools import find_packages, setup

setup(
    name="dynamodb_python_lib",
    version="0.0.2",
    author="DI Matrix",
    author_email="DCIMatrix@expedia.com",
    description="Brokers access to CP NLU data in DynamoDB.",
    url="https://github.expedia.biz/ECP/dynamodb-python-lib",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "python-dateutil==2.8.0",
        "boto3==1.11.14",
        "pandas==0.25.3",
        "requests==2.22.0",
        "language-check==1.1",
        "gingerit==0.8.0",
        "textblob==0.15.3"
    ]
)
