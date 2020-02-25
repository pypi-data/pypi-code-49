from distutils.core import setup
setup(
    name='githubToolsUcll',
    packages=['githubToolsUcll'],
    version= '0.3.0',
    license='MIT',
    description='A collection of tools to make UCLL assignments easier for both teachers and students.',
    author='De Vogeltjes',
    author_email='joery.mertens@student.ucll.be',
    url='https://github.com/dieterDehaes/github-tools',
    entry_points = {
        'console_scripts': [ 
                                'pullIssues=githubToolsUcll.pullIssues:main',
                                'pushIssues=githubToolsUcll.pushIssues:main',
                                'cloneRepos=githubToolsUcll.cloneRepos:main',
                                'createIssue=githubToolsUcll.createIssue:main',
                                'issuesToFile=githubToolsUcll.pullToFile:main',
                                'fileToIssues=githubToolsUcll.createFromFile:main',
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