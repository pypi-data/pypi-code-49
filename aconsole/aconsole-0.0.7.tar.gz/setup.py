import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='aconsole',
    version='0.0.7',
    author='Minad',
    author_email='steameetu@gmail.com',
    description='Async console like GUI built top of tkinter and asyncio.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/theminad/aconsole',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
