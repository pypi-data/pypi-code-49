from distutils.core import setup
setup(
    name='GITHUB-TOOLS-UCLL',
    packages=['GITHUB-TOOLS-UCLL'],
    version= '0.3.0',
    license='MIT',
    description='A collection of tools to make UCLL assignments easier for both teachers and students.',
    author='De Vogeltjes',
    author_email='joery.mertens@student.ucll.be',
    url='https://github.com/dieterDehaes/github-tools',
    entry_points = {
        'console_scripts': [ 
                                'pullIssues=GITHUB-TOOLS-UCLL.src.pullIssues:main',
                                'pushIssues=GITHUB-TOOLS-UCLL.src.pushIssues:main',
                                'cloneRepos=GITHUB-TOOLS-UCLL.src.cloneRepos:main',
                                'createIssue=GITHUB-TOOLS-UCLL.src.createIssue:main',
                                'issuesToFile=GITHUB-TOOLS-UCLL.src.pullToFile:main',
                                'fileToIssues=GITHUB-TOOLS-UCLL.src.createFromFile:main',
                            ]
    },
    install_requires = [
        'pyyaml',
        'gitpython',
        'xlwt',
        'xlrd',
        'requests'
    ],
    zip_safe=False
)