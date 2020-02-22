import json
import setuptools

kwargs = json.loads("""
{
    "name": "mbonig.aws_lambda_nodejs.NodejsFunctionPlus",
    "version": "0.0.1",
    "description": "The NodejsFunction from the @aws-cdk/aws-lambda-nodejs package but with the AWS_NODEJS_CONNECTION_REUSE_ENABLED automatically set.",
    "license": "MIT",
    "url": "https://github.com/mbonig/nodejsfunction-plus.git",
    "long_description_content_type": "text/markdown",
    "author": "Matthew Bonig<matthew.bonig@gmail.com>",
    "project_urls": {
        "Source": "https://github.com/mbonig/nodejsfunction-plus.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "mbonig.aws_lambda_nodejs",
        "mbonig.aws_lambda_nodejs._jsii"
    ],
    "package_data": {
        "mbonig.aws_lambda_nodejs._jsii": [
            "nodejsfunction-plus@0.0.1.jsii.tgz"
        ],
        "mbonig.aws_lambda_nodejs": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=1.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-lambda>=1.25.0, <2.0.0",
        "aws-cdk.aws-lambda-nodejs>=1.25.0, <2.0.0",
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
