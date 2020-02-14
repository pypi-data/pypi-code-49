import setuptools
from texercise import __version__
from pathlib import Path

texercise_folder = Path('texercise')
echo_exercise_files = texercise_folder.glob('echo_exercise/**/*')

setuptools.setup(
    name='texercise',
    version=__version__,
    author='Rasmus Laurvig Haugaard',
    author_email='rasmus.l.haugaard@gmail.com',
    description='command line interface for exercises',
    url='https://github.com/RasmusHaugaard/texercise-cli',
    scripts=[
        'bin/texercise',
    ],
    packages=setuptools.find_packages(),
    package_data={
        'texercise': [str(p.relative_to(texercise_folder)) for p in echo_exercise_files]
    },
    install_requires=[
        'request',
        'click',
        'tabulate',
    ],
    python_requires='>=3.6',
)
