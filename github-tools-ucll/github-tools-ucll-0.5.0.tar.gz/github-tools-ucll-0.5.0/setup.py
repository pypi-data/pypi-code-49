from distutils.core import setup
setup(
    name='github-tools-ucll',
    packages=['github-tools-ucll'],
    version= '0.5.0',
    license='MIT',
    description='A collection of tools to make UCLL assignments easier for both teachers and students.',
    author='De Vogeltjes',
    author_email='joery.mertens@student.ucll.be',
    url='https://github.com/dieterDehaes/github-tools',
    entry_points = {
        'console_scripts': [ 
                                'pullIssues=github-tools-ucll.src.pullIssues:pulling',
                                'pushIssues=github-tools-ucll.src.pushIssues:main',
                                'cloneRepos=github-tools-ucll.src.cloneRepos:main',
                                'createIssue=github-tools-ucll.src.createIssue:main',
                                'issuesToFile=github-tools-ucll.src.pullToFile:main',
                                'fileToIssues=github-tools-ucll.src.createFromFile:main',
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