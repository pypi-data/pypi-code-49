from distutils.core import setup

setup(
    name='pybbucket',
    packages=['pybbucket'],
    version='1.0',
    license='MIT',
    description='A Python wrapper for the Bitbucket Cloud REST API 2.0 version.',
    author='Akshay Maldhure',
    author_email='akshaymaldhure@gmail.com',
    url='https://github.com/akshayamaldhure',
    download_url='https://github.com/akshayamaldhure/pybbucket/archive/v1.0.tar.gz',
    keywords=['bitbucket', 'bitbucketapi', 'pybitbucket'],
    install_requires=[
        'pybbucket',
        'requests'
    ],
    classifiers=[],
)
