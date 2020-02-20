from setuptools import setup, find_packages
 
setup(name='easierai_common_functions',
      version='1.8.4',
      url='https://gitlab.atosresearch.eu/ari/ioe-ai/common-python-helper-functions',
      license='ATOS',
      author='IoE Lab',
      author_email='juan.carrascoa@atos.net',
      description='This library contains reusable code for various projects',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      packages=find_packages(),
      install_requires =[
            'schedule',
            'joblib',
            'pydash',
            'tensorflow',
            'phased_lstm_keras',
            'scikit-learn',
            'python-logstash'
      ],
      zip_safe=False)
