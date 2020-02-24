from setuptools import setup

setup(
    name='hisak-idtools',
    version='0.1',
    packages=['hisak.idtools'],
    package_dir={'hisak.idtools': 'src'},
    url='https://gitlab.com/HiSakDev/idtools',
    license='MIT',
    author='HiSakDev',
    author_email='sak.devac@gmail.com',
    description='Identifier generator tools often used privately',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
