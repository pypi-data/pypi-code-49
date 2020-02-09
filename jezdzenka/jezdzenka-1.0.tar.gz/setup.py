from setuptools import setup

setup(
    name='jezdzenka',
    version='1.0',
    packages=['jezdzenka', 'jezdzenka.classes', 'jezdzenka.console', 'jezdzenka.database', ],
    package_data={"": ["*.mo", "*.po"]},
    url='https://naruciakk.eu/okucha/jezdzenka',
    license='CC0 1.0 Universal',
    author='Robert von Oliva (naruciakk)',
    entry_points={
        'console_scripts': [
            'jezdzenka = jezdzenka.__main__:main'
        ]
    },
    install_requires=[
        'prettytable', 'PyInquirer', 'tinydb', 'tinydb_serialization', 'python-magic', 'mo_installer',
    ],
    locale_src="locale",
    description='Handy wallet in your terminal, no strings attached.'
)
