from distutils.core import setup

setup(
    name='Pressdict',
    version='1.0.0',
    author='Tobias Guenther',
    author_email='pressdict@tobigue.de',
    packages=['pressdict', 'pressdict.test'],
    scripts=[],
    url='https://github.com/tobigue/pressdict',
    license='LICENSE.txt',
    classifiers=["Programming Language :: Python :: 3"],
    description=('Pressdict is a compressed key-value store '
                 'for JSON-serializable objects.'),
    long_description=open('README.rst').read()
)
