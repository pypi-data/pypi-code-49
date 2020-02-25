from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='hotWater',
      version='1.7',
      description='The program uses a residual deep learning model to predict water hot-spots on the surface of proteins',
      long_description=readme(),
      long_description_content_type='text/x-rst',
      author='Jan Zaucha',
      author_email='trelek2@gmail.com',
      license='MIT',
      packages=['hotWater'],
      include_package_data=True,
      install_requires=['numpy', 'scipy', 'biopython', 'matplotlib', 'scikit-learn', 'tensorflow', 'tensorflow-gpu', 'keras', 'neural_structured_learning'],
      dependency_links=['http://biopython.org/DIST/'],
      zip_safe=False)
