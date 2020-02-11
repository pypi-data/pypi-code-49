from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="remove-outliers",
    version="1.0.1",
    description="Removing outliers using IQR Interquartile range.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Kartikey Tiwari",
    author_email="kartikeytiwari37@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
    ],
    packages=["remove_outliers"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "remove-outliers=remove_outliers.remove:main",
        ]
    },
)