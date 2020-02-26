import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk-dynamodb-seeder",
    "version": "1.3.2",
    "description": "A simple CDK JSON seeder for DynamoDB",
    "license": "Apache-2.0",
    "url": "https://github.com/elegantdevelopment/aws-cdk-dynamodb-seeder#readme",
    "long_description_content_type": "text/markdown",
    "author": "Justin Taylor<jtaylor@elegantdevelopment.co.uk>",
    "project_urls": {
        "Source": "https://github.com/elegantdevelopment/aws-cdk-dynamodb-seeder.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "ElegantDevelopment.AWSCDKDynamoDBSeeder",
        "ElegantDevelopment.AWSCDKDynamoDBSeeder._jsii"
    ],
    "package_data": {
        "ElegantDevelopment.AWSCDKDynamoDBSeeder._jsii": [
            "aws-cdk-dynamodb-seeder@1.3.2.jsii.tgz"
        ],
        "ElegantDevelopment.AWSCDKDynamoDBSeeder": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=1.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-dynamodb>=1.26.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.26.0, <2.0.0",
        "aws-cdk.aws-s3>=1.26.0, <2.0.0",
        "aws-cdk.aws-s3-deployment>=1.26.0, <2.0.0",
        "aws-cdk.core>=1.26.0, <2.0.0",
        "aws-cdk.custom-resources>=1.26.0, <2.0.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
