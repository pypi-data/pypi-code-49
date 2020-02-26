from setuptools import setup

setup(name='logware',
    version='0.1.4',
    description='Logging middleware for python web services',
    url='https://github.com/Pratilipi-Labs/python-logware',
    author='Giridhar',
    author_email='samanth.giridhar@gmail.com',
    license='MIT',
    packages=['logware'],
    install_requires=[
      'webob'  
    ],
    zip_safe=False)
