from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()
    
def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(name = 'emsapi',
      version = '0.1.1',
      description = 'A Python EMS RESTful API Client/Wrapper',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
        ],
      url = 'https://github.com/ge-flight-analytics/emsapi-python',
      author = 'GE Flight Analytics',
      author_email = 'AviationAdiSupport@ge.com',
      license = 'MIT',
      packages = find_packages(exclude=("docs","tools")),
      install_requires = requirements(),
      zip_safe = False)
      
