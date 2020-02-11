import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-prb",
    "version": "0.2.0",
    "description": "cdk-pull-request-builder",
    "license": "MIT",
    "url": "https://github.com/dheffx/cdk-pull-request-builder.git",
    "long_description_content_type": "text/markdown",
    "author": "Daniel Heffner",
    "project_urls": {
        "Source": "https://github.com/dheffx/cdk-pull-request-builder.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_prb",
        "cdk_prb._jsii"
    ],
    "package_data": {
        "cdk_prb._jsii": [
            "cdk-pull-request-builder@0.2.0.jsii.tgz"
        ],
        "cdk_prb": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.20.11",
        "publication>=0.0.3",
        "aws-cdk.aws-codebuild~=1.19,>=1.19.0",
        "aws-cdk.aws-codecommit~=1.19,>=1.19.0",
        "aws-cdk.aws-events~=1.19,>=1.19.0",
        "aws-cdk.aws-events-targets~=1.19,>=1.19.0",
        "aws-cdk.aws-iam~=1.19,>=1.19.0",
        "aws-cdk.aws-lambda~=1.19,>=1.19.0",
        "aws-cdk.core~=1.19,>=1.19.0"
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
