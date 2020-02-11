from setuptools import setup

setup(
    name="hello_world_gnits",
    version="0.0.4",
    description="Hello world",
    author="Tang Jiawei",
    author_email="tang@o1labs.org",
    url="https://github.com/ghost-not-in-the-shell/hello-world-gnits",
    packages=["hello_world"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
    ],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "helloworld=hello_world.__main__:main",
        ]
    }
)
