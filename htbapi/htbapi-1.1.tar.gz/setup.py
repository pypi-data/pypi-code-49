from setuptools import setup

setup(
        name="htbapi",
        version="1.1",
        description="An unofficial API Wrapper for Hackthebox.",
        long_description=open("README.md", "r").read(),
        long_description_content_type="text/markdown",
        license="GPL",
        author="sw1tchbl4d3",
        author_email="jsimeze@pm.me",
        url="https://github.com/sw1tchbl4d3-github/htbapi",
        packages=["htbapi"],
        install_requires=["requests"]
)
