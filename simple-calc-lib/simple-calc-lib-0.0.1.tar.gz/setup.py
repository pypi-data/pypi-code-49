from distutils.core import setup
setup(
  name='simple-calc-lib',
  packages=['simple-calc-lib'],
  version='0.0.1',
  license='MIT',
  description='Simple test calc library',
  author='Artem Osadchiy',
  author_email='warashilow@gmail.com',
  url='https://gitlab.com/warashilow/simple-calc-lib',
  download_url='https://gitlab.com/warashilow/simple-calc-lib/-/archive/v0.0.1/simple-calc-lib-v0.0.1.tar.gz',
  keywords=['test', 'package', 'calc'],
  install_requires=[
          'flake8',
          'pytest',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
