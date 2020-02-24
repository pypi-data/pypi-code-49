from setuptools import setup, find_packages

def get_long_description():
    with open('README.md', 'r') as f:
        long_description = f.read()
    return long_description

setup(
    name = 'mpyll', 
    version = '0.1b1', 
    description = 'A package for easy task parallelization across CPU threads', 
    package_dir = {'': 'src'}, 
    packages = find_packages(where = 'src'), 
    classifiers = [
        'Development Status :: 4 - Beta', 
        'Intended Audience :: Developers', 
        'Intended Audience :: Science/Research', 
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 
        'Programming Language :: Python :: 3', 
        'Operating System :: OS Independent', 
    ], 
    long_description = get_long_description(), 
    long_description_content_type = 'text/markdown', 
    url = 'https://gitlab.com/mhdy/mpyll', 
    author = 'Mehdi', 
    author_email = 'ydhm@protonmail.com', 
    keywords = 'parallel parallelization multiprocessing', 
)
