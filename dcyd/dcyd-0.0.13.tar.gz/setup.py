from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dcyd",
    version="0.0.13",
    author="Tim Eller",
    author_email="tim@dcyd.io",
    description="dcyd model performance monitoring client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dcyd-inc/dcyd-mpm-client-python",
    entry_points={
        'console_scripts': [
            'dcyd-config = dcyd.config:main',
        ],
    },
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'google-cloud-logging',
        'google-cloud-pubsub',
        'pkg_resources',
        'requests',
    ],
    tests_require=[
        'pytest',
    ],
    python_requires='>=3.5',
)
