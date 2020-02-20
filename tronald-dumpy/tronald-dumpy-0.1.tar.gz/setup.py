from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name="tronald-dumpy",
    version="0.1",
    description="Python wrapper for the TronaldDump API",
    license="GPLv3",
    long_description_content_type="text/markdown",
    long_description=README,
    packages=find_packages(),
    install_requires=[
        'requests',
        'urllib3',
        ],
    python_requires='>=3.6',
    author="gushka",
    author_email="guskhka@gmail.com",
    url="https://github.com/Gushka/tronalddump-python",
)
