import re
from os.path import dirname, join

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'markdownserver', '__init__.py')) as f:
    version = re.match(r'.*__version__ = \'(.*)\'', f.read(), re.S).group(1)


dependencies = [
    'easycli',
    'yhttp >= 2.9.1, < 3',
    'markdown2',
    'mako'
]


setup(
    name='markdownserver',
    version=version,
    url='https://github.com/babakhani/markdownserver',
    author='Reza Babakhani',
    author_email='babakhani.reza@gmail.com',
    description='markdown http server',
    packages=find_packages(exclude=['tests']),
    install_requires=dependencies,
    license='MIT',
    include_package_data=True,
    long_description_content_type='text/markdown',  # This is important!
    package_data={'markdownserver': [
        'markdownserver/master.mako',
        'static/*.css'
    ]},
    entry_points={
        'console_scripts': [
            'markdownserver = markdownserver:app.climain',
        ]
    }
)
