import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-registrable-choices",
    version="0.0.1-alpha",
    author="Sidnei Pereira",
    author_email="sidnei@hprs.com.br",
    description="Django Registrable Lazy Choices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hyper-coding/dj-choices",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
