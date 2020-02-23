from setuptools import setup, find_packages
from glob import glob


def find_scripts(pkgs):
    ret = []
    for pkgname in pkgs:
        ret.extend(glob(pkgname + '/scripts/*.py'))
    return ret


pkgs = find_packages()
scripts = find_scripts(pkgs)


setup(
    name='matplotlibaux',
    packages=find_packages(),
    include_package_data=True,
    version='20.02.23.0',
    license='GNU GPLv3',
    platforms='any',
    description='matplotlib auxiliary stuff',
    author='Julio Trevisan',
    author_email='juliotrevisan@gmail.com',
    url='https://github.com/trevisanj/matplotlibaux',
    keywords= ['matplotlib', ],
    install_requires=[],
    scripts=scripts
)


# TODO later install_requires=['numpy', 'matplotlib', 'pyqt5'],  # matplotlib never gets installed correctly by pip, but anyway...
