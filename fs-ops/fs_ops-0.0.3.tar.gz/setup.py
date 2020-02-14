from setuptools import setup, find_packages
import platform

settings = dict(name='fs_ops',
        packages=find_packages(),
        version='0.0.3',
        description='Description.',
        long_description='Long description.',
        author='MatteoLacki',
        author_email='matteo.lacki@gmail.com',
        url='https://github.com/MatteoLacki/fs_ops.git',
        keywords=['Great module', 'Devel Inside'],
        classifiers=['Development Status :: 1 - Planning',
                     'License :: OSI Approved :: BSD License',
                     'Intended Audience :: Science/Research',
                     'Topic :: Scientific/Engineering :: Chemistry',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7'],
        install_requires=[],
        scripts = ["bin/grep_paths"])

if platform.system() == 'Windows':
    settings['scripts'] = ["bin/grep_paths.py"]
else:
    settings['scripts'] = ["bin/grep_paths"]

setup(**settings)