import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
     name='autoenrich',
     version='2.1.1',
     scripts=['bin/autoenrich', 'bin/impression', 'bin/ae_utils'] ,
     author="Will Gerrard",
     author_email="will.gerrard@bristol.ac.uk",
     description="Computational NMR Library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/wg12385/autoenrich_public",
     packages=setuptools.find_namespace_packages(exclude=['_site/*', 'bin/*', 'build/*', 'dist/*', 'tests/*', '*test*', 'dockerfiles/*', 'setup.py']),
	 classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
         "Operating System :: OS Independent",
     ]
 )
