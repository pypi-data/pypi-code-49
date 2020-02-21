from setuptools import setup, find_packages
import os

rootDir = os.path.abspath(os.path.dirname(__file__))
reqPath = os.path.join(rootDir, 'requirements.txt')
readmePath = os.path.join(rootDir, 'README.md')

with open(reqPath) as f:
    required = f.read().splitlines()

with open(readmePath, "r") as f:
    long_description = f.read()

setup(
    name='easyreq',
    version='1.1.1',
    license='MIT',
    author='Krzysztof Janiszewski',
    author_email='krzychu.janiszewski@gmail.com',
    description='Test package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://kjaniszewski.pl',
    download_url='https://gitlab.com/Krzysidlo/easyreq',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'easyreq = easyreq.main:main'
        ]
    },
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
