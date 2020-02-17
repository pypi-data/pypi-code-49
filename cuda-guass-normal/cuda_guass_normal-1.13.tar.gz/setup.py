from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='cuda_guass_normal',
      version='1.13',
      author='shuzhouz',
      author_email='shuzhouz@umich.edu',
      license='MIT',
      description='A package used in DNN trainning in ATLAS analysis',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['cuda_guass_normal'],
      zip_safe=False,
      python_requires='>=3.6',
)

