from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="cloudfiles-light",
    version="0.1",
    description="Lightweight helper for using rackspace cloudfiles",
    long_description=readme(),
    license="MIT",
    url="https://github.com/davidszotten/cloudfiles-light",
    py_modules=["cloudfiles_light"],
    install_requires=["requests"],
    author="David Szotten",
    author_email="davidszotten@gmail.com",
    extras_require={
        "dev": [
            "pytest",
            "responses",
            "pytest-responses",
            "coverage",
            "pytest-cov",
            "flake8",
            "black",
        ]
    },
)
