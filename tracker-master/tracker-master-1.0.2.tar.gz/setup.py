from setuptools import setup

setup(
    name='tracker-master',
    version='1.0.2',
    packages=['tracker_master', 'tracker_master.model', 'tracker_master.app_master', 'tracker_master.app_server'],
    url='',
    license='',
    author='Mikhail Astafurov',
    author_email='',
    package_data={'': ['conf/app_master_config.yaml']},
    include_package_data=True,
    description=''
)
