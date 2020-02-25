from distutils.core import setup
setup(
    name='GITHUB-TOOLS-UCLL',
    packages=['GITHUB-TOOLS-UCLL'],
    version= '0.2.0',
    license='MIT',
    description='A collection of tools to make UCLL assignments easier for both teachers and students.',
    author='De Vogeltjes',
    author_email='joery.mertens@student.ucll.be',
    url='https://github.com/dieterDehaes/github-tools',
    entry_points = {
        'console_scripts': [ 
                                'pullIssues=GITHUB-TOOLS-UCLL.pullIssues:main',
                                'pushIssues=GITHUB-TOOLS-UCLL.pushIssues:main',
                                'cloneRepos=GITHUB-TOOLS-UCLL.cloneRepos:main',
                                'createIssue=GITHUB-TOOLS-UCLL.createIssue:main',
                                'issuesToFile=GITHUB-TOOLS-UCLL.pullToFile:main',
                                'fileToIssues=GITHUB-TOOLS-UCLL.createFromFile:main',
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