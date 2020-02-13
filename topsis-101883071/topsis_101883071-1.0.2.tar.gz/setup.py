from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis_101883071",
    version="1.0.2",
    description="Python package to implement TOPSIS",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/",
    author="Yogesh",
    author_email="ysingla001@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["topsis_101883071"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis_101883071=topsis_101883071.__init__:main",
        ]
    },
)
