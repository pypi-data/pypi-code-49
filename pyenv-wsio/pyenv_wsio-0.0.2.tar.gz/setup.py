import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyenv_wsio",
    version="0.0.2",
    author="beanjs",
    author_email="502554248@qq.com",
    description="VirtualPyEnv websocket library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT Licence',
    url="https://github.com/graphisoft-python/pyenv_wsio",
    packages=['pyenv_wsio'],
    install_requires=['websocket_client'],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
)