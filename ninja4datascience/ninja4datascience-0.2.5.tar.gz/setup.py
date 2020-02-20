from distutils.core import setup

with open("README.txt", "r") as fh:
    long_description = fh.read()

setup(
    name='ninja4datascience',
    version='0.2.5',
    # scripts=['ninja4datascience'],
    author="Divyesh Vaghani",
    author_email="divyeshvaghani96@gmail.com",
    description="Data Science Ninja to help you to make your coding part easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/divyeshvaghani",
    license="MIT",
    # packages=setuptools.find_packages(),
    packages=['ninja4datascience'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=False
)
