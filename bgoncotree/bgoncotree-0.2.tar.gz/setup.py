from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

# Get the long description from the README file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bgoncotree',
    version='0.2',
    description='BBGLab interface for an OncoTree',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url="https://bitbucket.org/bgframework/bgoncotree",
    author="Barcelona Biomedical Genomics Lab",
    author_email="bbglab@irbbarcelona.org",
    license="Apache Software License 2.0",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'bgoncotree = bgoncotree.cli:cli',
        ]
    }
)
