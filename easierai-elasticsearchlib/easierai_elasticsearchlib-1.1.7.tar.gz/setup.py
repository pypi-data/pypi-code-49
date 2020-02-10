from setuptools import setup, find_packages
 
setup(name='easierai_elasticsearchlib',
      version='1.1.7',
      url='https://gitlab.atosresearch.eu/ari/ioe-ai/data-elasticsearch_python',
      license='ATOS',
      author='IoE Lab',
      author_email='juan.carrascoa.external@atos.net',
      description='This library manages the communication between python programs and elasticsearch database',
      long_description=open('README.md').read(),
      packages=find_packages(),
      install_requires =[
            'elasticsearch',
            'pydash'
      ],
      zip_safe=False)
