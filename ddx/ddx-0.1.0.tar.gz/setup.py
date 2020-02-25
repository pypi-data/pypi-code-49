import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ddx",
    version="0.1.0",
    py_modules=['ddx'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        ddx=ddx:cli
    ''',
    author="ChanMo",
    author_email="chan.mo@outlook.com",
    description="快速搭建基于Docker的Django项目",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChanMo/ddx",
)
