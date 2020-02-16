import setuptools

with open('README.rst') as file:

    readme = file.read()

name = 'vessel'

version = '2.1.0'

author = 'Exahilosys'

url = f'https://github.com/{author}/{name}'

setuptools.setup(
    name = name,
    version = version,
    author = author,
    url = url,
    packages = setuptools.find_packages(),
    license = 'MIT',
    description = 'Cache and contain utilities.',
    long_description = readme,
    install_requires = [
        'pathing'
    ],
    extras_require = {
        'docs': [
            'sphinx'
        ]
    }
)
