# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('graphene_ai/graphene.py').read(),
    re.M
    ).group(1)

setup(
    name = "graphene_ai",
    packages = ["graphene_ai"],
    entry_points = {
        "console_scripts": ['graphene = graphene.graphene:main']
        },
    version = '0.1',
    description = "Graphene AI API.",
    author = "Francis Bautista",
    author_email = "francis.bautista07@gmail.com",
    keywords = ['GRAPHENE', 'AI', 'NATURAL LANGUAGE PROCESSING', 'MULTILINGUAL'],
    url = "https://github.com/graphene-ai/python-graphene-ai",
    install_requires=[
        'argparse',
        'urllib'
    ]
)