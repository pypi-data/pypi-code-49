from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vaknl-gcp',
    description='Vakanties.nl pypi package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.1.1',
    url='https://github.com/vakantiesnl/vaknl-PyPi.git',
    author='Wytze Bruinsma',
    author_email='wytze.bruinsma@vakanties.nl',
    keywords=['vaknl', 'pip'],
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=['google-cloud-bigquery', 'google-cloud-storage', 'google-cloud-secret-manager', 'newlinejson']
)
