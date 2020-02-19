"""
CLI for Plasma
"""
from setuptools import find_packages, setup

dependencies = ['click','PyYAML','requests','xxhash']

description = 'CLI for Plasma, a simple ML workflow management tool. Visit docs.s20.ai to read the docs.'

setup(
    name='plasma-cli',
    version='0.1.4',
    url='https://github.com/tabishimran/plasma-cli',
    license='BSD',
    author='Tabish Imran',
    author_email='vector@s20.ai',
    description=description,
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'plasma = plasmacli.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
