from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pytimeset',
    version='0.5.9',
    packages=['timeset'],
    url='https://github.com/GFlorio/pytimeset',
    license='MIT',
    author='Gabriel Florio',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='gabriel@gabrielflorio.com',
    description='Defines sets and intervals to work with time, and provides arithmetic operations '
                'for them. Uses Cython extensions for performance.',
    ext_modules=[Extension('timeset.timeset', ['timeset/timeset.c'])],
    package_data={'timeset': ['timeset.pyi', 'py.typed']},
)
