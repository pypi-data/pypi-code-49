from collections import OrderedDict

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="config-client3",
    version="1.0.0",
    author="Jeff M",
    author_email="quicksh0t12@gmail.com",
    description="config service client for pcf config-server3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache-2.0',
    url="https://github.com/thedonutz/config-client",
    packages=setuptools.find_packages(),
    python_requires='>=3.6.0',
    project_urls=OrderedDict((
        ('Documentation', 'https://github.com/thedonutz/config-client'),
        ('Code', 'https://github.com/thedonutz/config-client'),
        ('Issue tracker', 'https://github.com/thedonutz/config-client/issues')
    )),
    install_requires=[
        'attrs>=19.1.0',
        'glom>=19.2.0',
        'requests>=2.22.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: AsyncIO",
        "Framework :: Flask",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Java Libraries",
    ],
)
