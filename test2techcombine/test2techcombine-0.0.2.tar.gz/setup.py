from setuptools import find_packages, setup

DISTNAME = "test2techcombine"
VERSION = "0.0.2"
DESCRIPTION = "Techcombine frameworl for ecommerce"
LICENSE = "MIT"
AUTHOR = "Techcombine developer team"
EMAIL = "kittipat.phongsak@gmail.com"
URL = "https://github.com/chinnawatp/techcombine-framework"
DOWNLOAD_URL = ""
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",      #Specify which pyhton versions that you want to support
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
]

INSTALL_REQUIRES = [
    "django==2.1.7",
    "djangorestframework==3.9.2",
    "Unidecode==1.0.23",
]

with open('README.md', 'r') as fp:
    LONG_DESCRIPTION = fp.read()

setup(
    name=DISTNAME,
    version=VERSION,
    license=LICENSE,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,
    packages=find_packages(include=["techcombine", "techcombine.*"]),
    python_requires=">=3.6.1",
    install_requires=INSTALL_REQUIRES,
    platforms="any",

)