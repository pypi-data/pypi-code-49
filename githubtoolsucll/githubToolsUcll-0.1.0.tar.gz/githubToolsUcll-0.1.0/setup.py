from distutils.core import setup
setup(
    name='githubToolsUcll',
    packages=['githubToolsUcll'],
    version= '0.1.0',
    license='MIT',
    description='A collection of tools to make UCLL assignments easier for both teachers and students.',
    author='De Vogeltjes',
    author_email='joery.mertens@student.ucll.be',
    url='https://github.com/dieterDehaes/github-tools',
    entry_points = {
        'console_scripts': [ 
                                'pullIssues=githubtoolsucll.src.pullIssues:main',
                                'pushIssues=githubtoolsucll.src.pushIssues:main',
                                'cloneRepos=githubtoolsucll.src.cloneRepos:main',
                                'createIssue=githubtoolsucll.src.createIssue:main',
                                'issuesToFile=githubtoolsucll.src.pullToFile:main',
                                'fileToIssues=githubtoolsucll.src.createFromFile:main',
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