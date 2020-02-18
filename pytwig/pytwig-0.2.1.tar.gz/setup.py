from setuptools import setup

setup(
	name='pytwig',
	version='0.2.1',
	description='Library for modifying and creating Bitwig files. (Not affiliated with Bitwig at all. Something something trademark of Bitwig GmbH etc.)',
	url='https://gitlab.com/jaxter184/pytwig',
	author='jaxter184',
	author_email='jaxter184@gmail.com',
	license='MIT',
	packages=['pytwig'],
	keywords="Bitwig music",
#	install_requires=[ # not sure how this field works yet
#		'json',
#	],
	zip_safe=False
)

# python setup.py sdist upload
