from setuptools import setup
import pathlib
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
	name='oled_text',
	version='1.1',
	packages=['oled_text'],
	url='https://bitbucket.org/bachi76/oled-ssd1306-text/src',
	license='Apache 2.0',
	author='Martin Bachmann',
	author_email='m.bachmann@insign.ch',
	description='Easily display text on an SSD1306 oled display connected to a Raspberry Pi',
	long_description=README,
    long_description_content_type="text/markdown",
	python_requires='>=3.5',
	install_requires=["adafruit-circuitpython-ssd1306"],
	include_package_data=True,
	keywords=['OLED', 'SSD1306', 'Raspberry Pi'],
)
