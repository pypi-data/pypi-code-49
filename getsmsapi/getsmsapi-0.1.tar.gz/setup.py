from distutils.core import setup


setup(
  name='getsmsapi',
  packages=['getsmsapi'],
  version='0.1',
  license='MIT',
  description='Allow you to receive virtual numbers and sms in services like sim-sms and sms-active',
  author='Gazizov Ruslan',
  author_email='almetfly@gmail.com',
  url='https://github.com/RuslanGR1/getsmsapi',
  download_url='https://github.com/RuslanGR1/getsmsapi/archive/0.1.tar.gz',
  keywords=['sms', 'activate', 'virtual number'],
  install_requires=[
    'pydash',
    'requests'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
