import setuptools
with open('js_script_py/README.md', 'r') as md:
    ld = md.read()


setuptools.setup(
    name = "js_script_py",
    version = "0.1",


    author = "Stark.-12x_42",
    author_email = "xsumagravity@gmail.com",


    description = "Turn python code to javascript code",


    long_description = ld,
    long_description_content_type = "text/markdown",


    url = "https://repl.it/@Downey/pythonjavascript",
    packages = setuptools.find_packages(),


    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",   
    ],
    python_requires = '>=3.6',
)