from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='zpcheckresource',         # How you named your package folder (MyLib)
    packages=['zpcheckresource'],   # Chose the same as "name"
    version='0.5',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='ZaloPay support check resource CDN',
    long_description=readme(),
    author='eris mabu',                   # Type in your name
    author_email='phucpv89@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/phucpv89',
    # I explain this later on
    download_url='https://github.com/phucpv89/zalopay-svn-upload/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['ZaloPay', 'CDN'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
