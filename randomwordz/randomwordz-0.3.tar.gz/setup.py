from distutils.core import setup
setup(
    name='randomwordz',         # How you named your package folder (MyLib)
    packages=['randomwordz'],   # Chose the same as "name"
    version='0.3',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='bsd-3-clause',
    # Give a short description about your library
    description='A utility to get some random words, by part of speech',
    author='Noah Yoshida',                   # Type in your name
    author_email='nyoshida@nd.edu',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/noyoshi/randomwordz',
    # I explain this later on
    download_url='https://github.com/noyoshi/randomwordz/archive/0.3.tar.gz',
    # Keywords that define your package best
    keywords=['random', 'words', 'NLP'],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        # Again, pick a license
        'License :: OSI Approved :: BSD License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
