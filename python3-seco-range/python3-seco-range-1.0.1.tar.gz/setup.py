import setuptools
from os import path

readme_path = path.join(path.abspath(path.dirname(__file__)), 'README.md')
with open(readme_path, encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='python3-seco-range',
    version = '1.0.1',
    author='ytoolshed',
    description='A Python 3 version of the library to interact with Range from ytoolshed',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xadrnd/range/tree/master/python_seco_range/source',
    project_urls={
        'Original Project': 'https://github.com/ytoolshed/range'
    },
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'argparse',
        'BeautifulSoup4',
        'GitPython',
        'PyYaml',
        'requests'
    ],
    python_requires='>=3.6'
)

