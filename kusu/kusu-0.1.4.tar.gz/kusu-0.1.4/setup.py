import setuptools

# Code originally from https://github.com/aegirhall/console-menu/blob/develop/setup.py

import io
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)



long_description = read("README.md")



setuptools.setup(
    name="kusu",
    version="0.1.4",
    author="Kieran Wood",
    author_email="kieran@canadiancoding.com",
    description="DEPRECATED",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Descent098/kusu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 7 - Inactive",
    ],
) 