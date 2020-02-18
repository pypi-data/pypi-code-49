import json
import setuptools

kwargs = json.loads("""
{
    "name": "jsii-sample",
    "version": "1.5.7",
    "description": "hello, world",
    "url": "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/jsii-sample",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "project_urls": {
        "Source": "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/jsii-sample"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "jsii_sample",
        "jsii_sample._jsii"
    ],
    "package_data": {
        "jsii_sample._jsii": [
            "jsii-sample@1.5.7.jsii.tgz"
        ],
        "jsii_sample": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.20.2",
        "publication>=0.0.3"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
