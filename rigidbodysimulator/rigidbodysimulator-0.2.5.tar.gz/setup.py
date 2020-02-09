import setuptools
import os
import versioneer
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

with open("README.md", "r") as fh:
    long_description = fh.read()


directory = os.path.dirname(os.path.abspath(__file__))
requirements_path = (os.path.join(directory,'requirements.txt'))
with open(requirements_path,mode = 'r') as file:
    requirements = file.readlines()

extras = {
    'dev': [
        'wheel','versioneer'
    ]
}

test_requirements = ['pytest']

setuptools.setup(
    name="rigidbodysimulator",
    version=versioneer.get_version(),
    author="SSPA",
    author_email="maa@sspa.se",
    description="rigidbodysimulator simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/martinlarsalbert/motion-to-acceleration",
    packages=['rigidbodysimulator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',

    install_requires=requirements,
    tests_require = test_requirements,
    extras_require=extras,

    package_data={
        'rigidbodysimulator': [],
      },
    scripts=[]

)