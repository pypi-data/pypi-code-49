from setuptools import setup, find_packages


DEV_REQ = ['pytest', 'pytest-cov', 'pylint', 'mypy', 'flake8']
INSTALL_REQ = ['typeguard', 'click']

with open('README.md') as f:
    README = f.read()

setup(
    name='click-path',
    version='0.0.2',
    description='A library of path-like types for the Click command-line library',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Eugene Kovalev',
    author_email='eugene@kovalev.systems',
    url='https://gitlab.com/abraxos/click-path',
    project_urls={
        "Documentation": "https://gitlab.com/abraxos/click-path",
        "Code": "https://gitlab.com/abraxos/click-path",
        "Issue tracker": "https://gitlab.com/abraxos/click-path/issues",
    },
    license="GPL",
    keywords = ['click', 'path', 'glob', 'type', 'validation'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=INSTALL_REQ,
    extras_require={'dev': DEV_REQ}
)
