import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-filemaker-pyodbc",
    version="0.0.9",
    author="Keith John Hutchison - Ceiteach Seán Mac Úistin",
    author_email="keith@bd2l.com.au",
    description="Django Database Engine for Filemaker using pyodbc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/csmu/django-filemaker-pyodbc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)