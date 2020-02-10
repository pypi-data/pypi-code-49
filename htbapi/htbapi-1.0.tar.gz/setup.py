from setuptools import setup

setup(
        name="htbapi",
        version="1.0",
        desription="An unofficial API Wrapper for Hackthebox (and more!)",
        long_description=open("README.md", "r").read(),
        license="GPL",
        author="sw1tchbl4d3",
        author_email="jsimeze@pm.me",
        url="https://github.com/sw1tchbl4d3-github/htbapi",
        packages=["htbapi"],
        install_requires=["requests"]
)
