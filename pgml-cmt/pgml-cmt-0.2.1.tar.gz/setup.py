from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pgml-cmt',
      version='0.2.1',
      description='Navigating the Generalization Landscape of Neural Networks using Physics: A Case Study in Quantum Mechanics',
      url='http://shorturl.at/tCZ05',
      author='Anonymous Author',
      author_email='pgml_cmt@yahoo.com',
      license='MIT',
      packages=['cmt'],
      package_dir={'cmt': 'cmt'},
      long_description=long_description,
      install_requires=[
#           'numpy',
#           'pandas',
#           'tqdm',
#           'matplotlib',
#           'seaborn',
#           'Pillow',
#           'fastprogress',
#           'torch',
#           'torchvision',
#           'scikit-learn',
#           'scipy',
#           'jupyterlab'
      ],
      zip_safe=False)
