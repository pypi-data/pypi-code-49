from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file # Detalhamento do pacote
try:
    with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Ver PEP 426 (name)
    # Iniciar ou terminar com letra ou número
    # Nome do seu pacote
    name='spiderling',

    # Ver PEP 440
    # O formato pode ser assim:

    # 1.2.0.dev1  # Development release
    # 1.2.0a1     Alpha Release
    # 1.2.0b1     Beta Release
    # 1.2.0rc1    Release Candidate
    # 1.2.0       Final Release
    # 1.2.0.post1 Post Release
    # 15.10       Date based release
    # 23          Serial release
    # Versao do pacote
    version='1.0.2',
    # Se a versão ainda é compativel com o Python utilizado
    # Mudanças que tem no programa, mas a versão anterior ainda é compativel
    # Correções de erro e bugs, atualização

    description='Spiderling Analytics',  # Decrição curta que ficará no rótulo quando pesquisar o pacote
    long_description=long_description,  # arquivo DESCRIPTION.rst

    # Detalhes do Autor
    author='Equipe Analytics',
    author_email='analytics@inmetrics.com.br',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='orchestration',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # Se quiser excluir algum pacote que eseteja no seu projeto coloque na lista abaixo
    packages=find_packages(exclude=['logs', 'local']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests>=2.22.0', 'psutil>=5.6.3', 'netifaces>=0.10.9'],
    setup_requires=['wheel'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'data': ['dados.json'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('','')]

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
        # 'console_scripts': [
            # 'sample=sample:main',
        # ],
    # },
)
