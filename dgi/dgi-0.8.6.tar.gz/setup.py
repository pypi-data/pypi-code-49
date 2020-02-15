import os
from setuptools import setup, find_packages

DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(DIR, "VERSION"), "r") as file:
    VERSION = file.read()

with open(os.path.join(DIR, "README.md"), "r") as file:
    LONG_DESCRIPTION = file.read()

setup(
    name="dgi",
    version=VERSION,
    author="Laboratório de Instrumentação de Sistemas Aquáticos (LabISA)",
    author_email="felipe.carlos@fatec.sp.gov.br",
    packages=find_packages(exclude=("testes",)),
    include_package_data = True,
    description="Ferramenta para facilitar o acesso aos dados disponibilizados pelo DGI/INPE.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/labisa/catalogo-de-imagens/dgi-dumps',
    install_requires=[
        'loguru',
        'pandas',
        'beautifulsoup4',
        'pymongo',
        'daemonize',
        'requests'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ]
)
