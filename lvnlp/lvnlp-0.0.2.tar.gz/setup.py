import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='lvnlp',
    packages=['lvnlp'],
    version='0.0.2',
    license='gpl-3.0',
    description='Latvian NLP Tools',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/ailab/lvnlp',
    keywords=['nlp', 'lv'],
    install_requires=[
        'allennlp==0.9.0',
        'flask==1.1.1',
        'requests==2.22.0'
    ],
)
