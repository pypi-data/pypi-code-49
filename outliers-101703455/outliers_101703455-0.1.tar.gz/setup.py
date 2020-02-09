from distutils.core import setup
setup(
  name = 'outliers_101703455',
  packages = ['outliers_101703455'],
  version = '0.1',
  license='MIT',
  description = 'You can find the outliers in your dataset with the hep of this library.',
  author = 'Rohit Kumar',
  author_email = 'krrohit1224@gmail.com',
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)