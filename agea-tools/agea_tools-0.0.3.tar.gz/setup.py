import os.path
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name='agea_tools',
    version='0.0.3',
    description='Paquete para manejar acciones comunes a la hora de utilizar datos.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://bitbucket.org/ageabigdata/agea_tools',
    author='Agea Big Data',
    author_email="bigdata@agea.com.ar",
    license="MIT",
    install_requires=[
        'pandas',
        'numpy',
        'ibis-framework'
    ],
    packages=find_packages(),
)

