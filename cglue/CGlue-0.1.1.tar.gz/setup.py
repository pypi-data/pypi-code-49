from setuptools import setup

setup(
    name='CGlue',
    version='0.1.1',
    packages=['cglue', 'cglue/plugins', 'cglue/utils'],
    package_dir={'cglue': 'cglue'},
    url='https://github.com/RevolutionRobotics/CGlue',
    license='MIT',
    author='Dániel Buga',
    author_email='daniel@revoltuionrobotics.org',
    description='Framework for C software',
    test_suite='nose2.collector.collector'
)
