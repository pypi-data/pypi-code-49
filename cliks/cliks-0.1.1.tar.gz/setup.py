from setuptools import setup, find_packages


with open("README.md", "r") as file:
    long_description = file.read()


with open("VERSION", "r") as file:
    version = file.read()


setup(
    name='cliks',
    packages=find_packages(),
    version=version,
    description='CLI for facilitate and standardize commit message.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Carlos Neto',
    author_email='carlos.santos110@fatec.sp.gov.br',
    url='https://github.com/augustoliks/cliks',
    keywords=['cli', 'git', 'commit'],
    install_requires=['PyInquirer', 'gitpython'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'cliks = src.app:main'
        ]
    }
)
