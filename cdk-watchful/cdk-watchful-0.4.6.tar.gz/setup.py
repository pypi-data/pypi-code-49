import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-watchful",
    "version": "0.4.6",
    "description": "Watching your CDK apps since 2019",
    "license": "Apache-2.0",
    "url": "https://github.com/eladb/cdk-watchful",
    "long_description_content_type": "text/markdown",
    "author": "Elad Ben-Israel<elad.benisrael@gmail.com>",
    "project_urls": {
        "Source": "https://github.com/eladb/cdk-watchful"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_watchful",
        "cdk_watchful._jsii"
    ],
    "package_data": {
        "cdk_watchful._jsii": [
            "cdk-watchful@0.4.6.jsii.tgz"
        ],
        "cdk_watchful": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.22.0",
        "publication>=0.0.3",
        "aws-cdk.aws-apigateway>=1.25.0, <2.0.0",
        "aws-cdk.aws-cloudwatch>=1.25.0, <2.0.0",
        "aws-cdk.aws-cloudwatch-actions==1.25.0",
        "aws-cdk.aws-dynamodb>=1.25.0, <2.0.0",
        "aws-cdk.aws-events>=1.25.0, <2.0.0",
        "aws-cdk.aws-events-targets==1.25.0",
        "aws-cdk.aws-lambda>=1.25.0, <2.0.0",
        "aws-cdk.aws-sns>=1.25.0, <2.0.0",
        "aws-cdk.aws-sns-subscriptions>=1.25.0, <2.0.0",
        "aws-cdk.aws-sqs>=1.25.0, <2.0.0",
        "aws-cdk.core>=1.25.0, <2.0.0"
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
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
