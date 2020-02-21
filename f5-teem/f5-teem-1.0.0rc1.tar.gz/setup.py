""" setup.py: see public setuptools docs for more detail """
import setuptools

# This should be a list of dependencies required for production use only
DEPENDENCIES = []

def get_description():
    """ Get project description """
    with open('./README.md', 'r') as readme:
        return readme.read()

setuptools.setup(
    name='f5-teem',
    version='1.0.0rc1',
    description='F5 TEEM Library',
    long_description=get_description(),
    long_description_content_type="text/markdown",
    author='F5 Ecosystems Group',
    author_email='solutionsfeedback@f5.com',
    license='Apache License 2.0',
    url="",
    packages=setuptools.find_packages(
        exclude=["test*", "tests*", "test_*", "test.*", "*.test"]
    ),
    install_requires=DEPENDENCIES,
    package_data={
        '': ['*.json', '*.yaml', '*.md', '*.rst']
    }
)
