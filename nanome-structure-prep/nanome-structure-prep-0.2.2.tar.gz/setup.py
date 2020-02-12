import pathlib
from setuptools import find_packages, setup

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
	name = 'nanome-structure-prep',
	packages=find_packages(),
	version = '0.2.2',
	license='MIT',
	description = 'A Nanome plugin to clean up selected structures.',
	long_description = README,
    long_description_content_type = "text/markdown",
	author = 'astrovicis',
	author_email = 'max@nanome.ai',
	url = 'https://github.com/nanome-ai/plugin-structure-prep',
	platforms="any",
	keywords = ['virtual-reality', 'chemistry', 'python', 'api', 'plugin'],
	install_requires=['nanome'],
	entry_points={"console_scripts": ["nanome-structure-prep = nanome_structure_prep.StructurePrep:main"]},
	classifiers=[
		'Development Status :: 3 - Alpha',

		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Chemistry',

		'License :: OSI Approved :: MIT License',

		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],
	package_data={
        "nanome_structure_prep": 
				[
					"assets/*",
					"json/*",
				]
	},
)