from setuptools import setup, find_packages

setup(
		name ='trajson',
		version ='0.0.2',
		author ='Ismael Traoré',
		author_email ='proximusexam@gmail.com',
		description ='Translate json files.',
		packages = find_packages(),
        include_package_data = True,
        install_requires=[
            'Click',
        ],
		entry_points ={
			'console_scripts': [
				'trajson = scripts.translation.py:cli'
			]
		},
		classifiers =(
			"Programming Language :: Python :: 3",
		),
)
