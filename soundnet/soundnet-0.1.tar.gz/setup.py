from setuptools import setup
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


BASEDIR = os.path.abspath(os.path.dirname(__file__))

setup(
    name='soundnet',
    version='0.1',
    packages=['soundnet'],
    install_requires=["numpy",
                      "keras",
                      "tensorflow<=1.15.2",
                      "librosa"],
    package_data={'': package_files('soundnet')},
    include_package_data=True,
    url='https://github.com/JarbasAl/soundnet',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='sound classification with SoundNet'
)
