from setuptools import setup, find_packages


setup(
    name = 'libflip',
    version = '2.0.0',
    description = 'Fivelines instructional game development platform',
    url = 'http://fivelines.io',
    author = 'Fivelines Interactive',
    author_email = 'support@fivelines.io',
    packages = find_packages(),
    install_requires = ['pygame', 'pillow', 'astar==0.9', 'bresenham==0.2'],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'flip = libflip:bootstrap'
        ]
    }
)
