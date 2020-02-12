import setuptools

with open("README.md", "r") as file_obj:
    long_description = file_obj.read()

packages = setuptools.find_packages()

setuptools.setup(
    name='nubium-utils',
    version='0.5.5',
    author="Edward Brennan",
    author_email="ebrennan@redhat.com",
    description="Some Kafka utility functions and patterns for the nubium project",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.corp.redhat.com/mkt-ops-de/nubium-utils.git",
    packages=packages,
    install_requires=["requests", "prometheus_client"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
