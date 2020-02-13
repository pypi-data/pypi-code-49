# This Python file uses the following encoding: utf-8
from setuptools import setup, find_packages
import platform

settings = dict(name='waters',
                packages=find_packages(),
                version='0.0.3',
                description='Parsing MS data from Waters.',
                long_description='Parsing MS data from Waters.',
                author='Mateusz Krzysztof Łącki',
                author_email='matteo.lacki@gmail.com',
                url='https://github.com/MatteoLacki/waters/',
                keywords=['Mass Spectrometry',
                          'Waters'],
                classifiers=[
                    'Development Status :: 1 - Planning',
                    'License :: OSI Approved :: BSD License',
                    'Intended Audience :: Science/Research',
                    'Topic :: Scientific/Engineering :: Chemistry',
                    'Programming Language :: Python :: 3.7'],
                install_requires=['pandas', 'fs_ops'])

if platform.system() == 'Windows':
    settings['scripts'] = ["bin/iadbs2stats.py", "bin/iadbs2csv.py", "bin/create_waters_shortcuts.py"]
else:
    settings['scripts'] = ["bin/iadbs2stats", "bin/iadbs2csv"]

setup(**settings)