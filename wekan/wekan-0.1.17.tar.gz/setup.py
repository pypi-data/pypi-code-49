import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wekan",
    version="0.1.17",
    author="Sanchan Moses",
    author_email="sanchanm@wekan.company",
    description="Project generator for wekan's python framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/We-Kan-Code/python-backend-framework-generators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires='>=3.6',
    install_requires=[
        "astroid==2.3.3",
        "autopep8==1.5",
        "colorama==0.4.3",
        "isort==4.3.21",
        "lazy-object-proxy==1.4.3",
        "mccabe==0.6.1",
        "prompt-toolkit==1.0.14",
        "pycodestyle==2.5.0",
        "Pygments==2.5.2",
        "PyInquirer==1.0.3",
        "pylint==2.4.4",
        "regex==2020.1.8",
        "six==1.14.0",
        "typed-ast==1.4.1",
        "wcwidth==0.1.8",
        "wrapt==1.11.2",
    ],
    entry_points={
        'console_scripts': [
            'wekan = wekan.generate:main',
        ],
    },
)
