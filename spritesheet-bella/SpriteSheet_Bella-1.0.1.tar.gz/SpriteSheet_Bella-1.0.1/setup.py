from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

__name__ = "SpriteSheet_Bella"
__author__ = "Nhung LAI"
__email__ = "nhungbella0511@gmail.com"
__version__ = "1.0.1"
__copyright__ = "Copyright (C) 2019, Intek Institute"
__credits__ = "Intek Institute"
__maintainer__ = "Nhung LAI"

setup(
    extras_require={
        "dev": [
            "appdirs==1.4.3",
            "attrs==19.3.0",
            "black==19.10b0; python_version >= '3.6'",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2019.11.28",
            "chardet==3.0.4",
            "click==7.0",
            "colorama==0.4.3",
            "distlib==0.3.0",
            "first==2.0.2",
            "idna==2.8",
            "importlib-metadata==1.5.0; python_version < '3.8'",
            "orderedmultidict==1.0.1",
            "packaging==19.2",
            "pathspec==0.7.0",
            "pep517==0.8.1",
            "pip-shims==0.5.0",
            "pipenv-setup==3.0.1",
            "pipfile==0.0.2",
            "plette[validation]==0.2.3",
            "pyparsing==2.4.6",
            "regex==2020.2.18",
            "requests==2.22.0",
            "requirementslib==1.5.3",
            "six==1.14.0",
            "toml==0.10.0",
            "tomlkit==0.5.8",
            "typed-ast==1.4.1",
            "typing==3.7.4.1",
            "urllib3==1.25.8",
            "vistir==0.5.0",
            "wheel==0.34.2",
            "zipp==3.0.0",
        ]
    },
    name=__name__,
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    version=__version__,
    copyright=__copyright__,
    credits=__credits__,
    long_description=long_description,
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "bleach==3.1.1",
        "certifi==2019.11.28",
        "cffi==1.14.0",
        "chardet==3.0.4",
        "cryptography==2.8",
        "docutils==0.16",
        "idna==2.8",
        "importlib-metadata==1.5.0; python_version < '3.8'",
        "jeepney==0.4.2; sys_platform == 'linux'",
        "keyring==21.1.0",
        "numpy==1.18.1",
        "pillow==7.0.0",
        "pkginfo==1.5.0.1",
        "pycparser==2.19",
        "pygments==2.5.2",
        "readme-renderer==24.0",
        "requests==2.22.0",
        "requests-toolbelt==0.9.1",
        "secretstorage==3.1.2; sys_platform == 'linux'",
        "six==1.14.0",
        "tqdm==4.43.0",
        "twine==3.1.1",
        "urllib3==1.25.8",
        "webencodings==0.5.1",
        "wheel==0.34.2",
        "zipp==3.0.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    dependency_links=[],
)
