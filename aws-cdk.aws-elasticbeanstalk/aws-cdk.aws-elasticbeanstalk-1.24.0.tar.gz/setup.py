import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-elasticbeanstalk",
    "version": "1.24.0",
    "description": "The CDK Construct Library for AWS::ElasticBeanstalk",
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
        "aws_cdk.aws_elasticbeanstalk",
        "aws_cdk.aws_elasticbeanstalk._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_elasticbeanstalk._jsii": [
            "aws-elasticbeanstalk@1.24.0.jsii.tgz"
        ],
        "aws_cdk.aws_elasticbeanstalk": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.22.0",
        "publication>=0.0.3",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
