from distutils.core import setup
setup(
    name='githubToolsUcll',
    packages=['githubToolsUcll'],
    version= '0.2.0',
    license='MIT',
    description='A collection of tools to make UCLL assignments easier for both teachers and students.',
    author='De Vogeltjes',
    author_email='joery.mertens@student.ucll.be',
    url='https://github.com/dieterDehaes/github-tools',
    entry_points = {
        'console_scripts': [ 
                                'pullIssues=githubToolsUcll.src.pullIssues:main',
                                'pushIssues=githubToolsUcll.src.pushIssues:main',
                                'cloneRepos=githubToolsUcll.src.cloneRepos:main',
                                'createIssue=githubToolsUcll.src.createIssue:main',
                                'issuesToFile=githubToolsUcll.src.pullToFile:main',
                                'fileToIssues=githubToolsUcll.src.createFromFile:main',
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