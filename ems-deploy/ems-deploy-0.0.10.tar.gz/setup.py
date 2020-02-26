from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name='ems-deploy',
    author="Jesper Halkjær Jensen",
    author_email="gedemagt@gmail.com",
    description="A small deploy utility package",
    version='0.0.10',
    url='https://github.com/',
    packages=['deploy'],
    entry_points={
        'console_scripts': [
            'deploy=deploy.deploy:run'
        ]
    },
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires='>=3.6'
)
