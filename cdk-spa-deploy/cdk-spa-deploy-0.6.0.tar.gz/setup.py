import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-spa-deploy",
    "version": "0.6.0",
    "description": "cdk-spa-deploy",
    "license": "MIT",
    "url": "https://github.com/nideveloper/CDK-SPA-Deploy.git",
    "long_description_content_type": "text/markdown",
    "author": "matt@vs-software.co.uk",
    "project_urls": {
        "Source": "https://github.com/nideveloper/CDK-SPA-Deploy.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "spa_deploy",
        "spa_deploy._jsii"
    ],
    "package_data": {
        "spa_deploy._jsii": [
            "cdk-spa-deploy@0.6.0.jsii.tgz"
        ],
        "spa_deploy": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.21.1",
        "publication>=0.0.3",
        "aws-cdk.aws-certificatemanager==1.24.0",
        "aws-cdk.aws-cloudfront==1.24.0",
        "aws-cdk.aws-route53-patterns==1.24.0",
        "aws-cdk.aws-route53-targets==1.24.0",
        "aws-cdk.aws-s3==1.24.0",
        "aws-cdk.aws-s3-deployment==1.24.0",
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
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
