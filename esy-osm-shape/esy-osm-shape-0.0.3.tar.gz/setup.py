import setuptools

setuptools.setup(
    name='esy-osm-shape',
    description='Convert OpenStreetMap objects to shapely objects.',
    version='0.0.3',
    license='GPLv3',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Ontje Lünsdorf',
    author_email='ontje.luensdorf@dlr.de',
    package_dir={'': 'src'},
    packages=setuptools.find_namespace_packages(where='src'),
    python_requires='>= 3.5',
    install_requires=['shapely >= 1.6, < 2', 'esy-osm-pbf == 0.0.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        (
            'License :: OSI Approved :: '
            'GNU General Public License v3 or later (GPLv3+)'
        ),
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
)
