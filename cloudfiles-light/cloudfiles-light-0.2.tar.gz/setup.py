from setuptools import find_packages, setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="cloudfiles-light",
    version="0.2",
    description="Lightweight helper for using rackspace cloudfiles",
    long_description=readme(),
    license="MIT",
    url="https://github.com/davidszotten/cloudfiles-light",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["requests"],
    include_package_data=True,
    package_data={"cloudfiles_light": ["py.typed"]},
    zip_safe=False,
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
