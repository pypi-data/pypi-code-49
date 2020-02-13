from setuptools import setup, find_packages


# with open('README.rst', 'r') as file:
#     long_description = file.read()

project = 'shakti'

setup(url='',
      name=project,
      author='STEALTH',
      version='0.0.0',
      packages=find_packages(),
      description='...',
      python_requires='>=3.6',
      long_description='TODO',
      long_description_content_type="text/x-rst",
      # Info: https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['License :: Other/Proprietary License',
                   'Development Status :: 1 - Planning',
                   # 'Development Status :: 2 - Pre-Alpha',
                   # 'Development Status :: 3 - Alpha',
                   # 'Development Status :: 4 - Beta',
                   # 'Development Status :: 5 - Production/Stable',
                   # 'Development Status :: 6 - Mature',
                   # 'Development Status :: 7 - Inactive',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Topic :: Software Development :: Libraries :: Python Modules'])
