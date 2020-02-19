import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

with open('requirements.txt') as f:
    install_reqs = f.readlines()
    reqs = [str(ir) for ir in install_reqs]

with open('test_requirements.txt') as f:
    install_test_reqs = f.readlines()
    test_reqs = [str(ir) for ir in install_test_reqs]

setuptools.setup(
    name="sixgill-clients",
    version="0.1.2",
    author="Sixgill",
    author_email="Support@cybersixgill.com",
    description="Sixgill clients package",
    install_requires=reqs,
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/Sterenson/sixgill-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    tests_require=test_reqs,
    test_suite="tests",
)
