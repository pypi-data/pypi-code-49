import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-tweet-queue",
    "version": "1.0.2",
    "description": "Defines an SQS queue with tweet stream from a search",
    "license": "Apache-2.0",
    "url": "https://github.com/eladb/cdk-tweet-queue.git",
    "long_description_content_type": "text/markdown",
    "author": "Elad Ben-Israel<elad.benisrael@gmail.com>",
    "project_urls": {
        "Source": "https://github.com/eladb/cdk-tweet-queue.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_tweet_queue",
        "cdk_tweet_queue._jsii"
    ],
    "package_data": {
        "cdk_tweet_queue._jsii": [
            "cdk-tweet-queue@1.0.2.jsii.tgz"
        ],
        "cdk_tweet_queue": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.22.0",
        "publication>=0.0.3",
        "aws-cdk.aws-dynamodb>=1.24.0, <2.0.0",
        "aws-cdk.aws-events>=1.24.0, <2.0.0",
        "aws-cdk.aws-events-targets>=1.24.0, <2.0.0",
        "aws-cdk.aws-iam>=1.24.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.24.0, <2.0.0",
        "aws-cdk.aws-sqs>=1.24.0, <2.0.0",
        "aws-cdk.core>=1.24.0, <2.0.0"
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
