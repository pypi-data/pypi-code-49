import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(name='runandcliscaffold',
      version='0.2',
      description='Lightweight library for use of defining functions and parameters that can be called from CLI or from other functions',
      url='https://github.com/tylertjburns/runandcliscaffold',
      author='tburns',
      author_email='tyler.tj.burns@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      python_requires=">3.5",
      long_description=README,
      long_description_content_type='text/markdown',
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