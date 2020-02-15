""" mlrose_reborn setup file."""

# Author: Genevieve Hayes
# Modified: Andrew Rollings
# License: BSD 3 clause

from setuptools import setup


def readme():
    """
    Function to read the long description for the mlrose_reborn package.
    """
    with open('README.md') as _file:
        return _file.read()


setup(name='mlrose_reborn',
      version='2.0.0',
      description="mlrose_reborn: Machine Learning, Randomized Optimization and"
      + " Search",
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/ryanmcdermott/mlrose',
      author='Genevieve Hayes (modifed by Andrew Rollings, forked by Ryan McDermott)',
      license='BSD',
      classifiers=[
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          "Natural Language :: English",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Software Development :: Libraries",
          "Topic :: Software Development :: Libraries :: Python Modules"],
      packages=['mlrose_reborn','mlrose_reborn.runners','mlrose_reborn.generators', 'mlrose_reborn.algorithms',
                'mlrose_reborn.algorithms.decay', 'mlrose_reborn.algorithms.crossovers',
                'mlrose_reborn.opt_probs', 'mlrose_reborn.fitness', 'mlrose_reborn.algorithms.mutators',
                'mlrose_reborn.neural', 'mlrose_reborn.neural.activation', 'mlrose_reborn.neural.fitness',
                'mlrose_reborn.neural.utils', 'mlrose_reborn.decorators',
                'mlrose_reborn.gridsearch'],
      install_requires=['numpy', 'scipy', 'scikit-learn', 'pandas', 'networkx', 'joblib'],
      python_requires='>=3',
      zip_safe=False)
