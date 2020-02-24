import setuptools

with open("README.md", "r") as file_handler:
    long_description = file_handler.read()

setuptools.setup(
    name='easy-ansi',
    version='0.2',
    author='Joey Rockhold',
    author_email='joey@joeysbytes.net',
    description='Easy ANSI is a terminal framework API to give you an easy way to use colors, cursor control movements, and line/box drawing.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://gitlab.com/joeysbytes/easy-ansi',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: Terminals"
    ],
    python_requires='>=3.6'
)
