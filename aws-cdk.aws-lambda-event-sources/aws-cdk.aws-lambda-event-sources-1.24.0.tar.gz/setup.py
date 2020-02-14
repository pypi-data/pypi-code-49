import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-lambda-event-sources",
    "version": "1.24.0",
    "description": "Event sources for AWS Lambda",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_lambda_event_sources",
        "aws_cdk.aws_lambda_event_sources._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_lambda_event_sources._jsii": [
            "aws-lambda-event-sources@1.24.0.jsii.tgz"
        ],
        "aws_cdk.aws_lambda_event_sources": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.22.0",
        "publication>=0.0.3",
        "aws-cdk.aws-apigateway==1.24.0",
        "aws-cdk.aws-dynamodb==1.24.0",
        "aws-cdk.aws-events==1.24.0",
        "aws-cdk.aws-iam==1.24.0",
        "aws-cdk.aws-kinesis==1.24.0",
        "aws-cdk.aws-lambda==1.24.0",
        "aws-cdk.aws-s3==1.24.0",
        "aws-cdk.aws-s3-notifications==1.24.0",
        "aws-cdk.aws-sns==1.24.0",
        "aws-cdk.aws-sns-subscriptions==1.24.0",
        "aws-cdk.aws-sqs==1.24.0",
        "aws-cdk.core==1.24.0"
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
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
