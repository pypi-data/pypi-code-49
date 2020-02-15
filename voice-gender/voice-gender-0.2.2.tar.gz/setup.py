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
    name='voice-gender',
    version='0.2.2',
    packages=['voice_gender'],
    install_requires=["numpy==1.15.2",
                      "python-speech-features==0.5",
                      "scikit-learn==0.19.2",
                      "scipy==1.1.0"],
    package_data={'': package_files('voice_gender')},
    include_package_data=True,
    url='https://github.com/JarbasAl/voice-gender',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='recognize gender'
)
