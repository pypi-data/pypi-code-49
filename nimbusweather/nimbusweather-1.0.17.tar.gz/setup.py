#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'nimbusweather',
        version = '1.0.17',
        description = 'weather software',
        long_description = 'nimbus weather talks to a variety of weather stations and publishes the data to (currently) weather underground. Nimbus is a fork of the very popular weewx weather software.',
        author = 'Garret Hayes',
        author_email = 'glhayes81@gmail.com',
        license = 'GPLv3',
        url = '',
        scripts = [
            'scripts/nimbus_config',
            'scripts/nimbus'
        ],
        packages = [
            'nimbusdrivers',
            'nimbuscfg',
            'nimbusmain'
        ],
        namespace_packages = [],
        py_modules = [],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {
            'nimbuscfg': ['nimbus.conf', 'init.d/*']
        },
        install_requires = [
            'configobj',
            'pyserial',
            'pyusb',
            'requests',
            'sentry_sdk',
            'setuptools',
            'urllib3==1.22'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
