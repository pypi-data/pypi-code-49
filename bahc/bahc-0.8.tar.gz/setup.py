from setuptools import setup

setup(	name='bahc',
      	version='0.8',
      	packages=['bahc'],
	install_requires=[	'numpy>=1.14.2',
				'fastcluster>=1.1.24'
				],
	#scripts=['bin/bahc','bin/svhc_benchmark','bin/svhc_plot'],
	author='Christian Bongiorno',
	author_email='pvofeta@gmail.com',
	license='GPL',
	zip_safe=False

      )

