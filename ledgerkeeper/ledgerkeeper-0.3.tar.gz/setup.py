import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(name='ledgerkeeper',
      version='0.3',
      description='Lightweight library for use of posting ledger entries to a specified mongoDB collection with access utils',
      url='https://github.com/tylertjburns/ledgerkeeper',
      author='tburns',
      author_email='tyler.tj.burns@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      python_requires=">3.5",
      install_requires=['click', 'pymongo'],
      long_description=README,
      zip_safe=False,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
      ])