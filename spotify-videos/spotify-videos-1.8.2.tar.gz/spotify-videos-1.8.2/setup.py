from setuptools import setup, find_packages
import warnings

warnings.warn("\n================================\n"
    "spotify-videos has been renamed to vidify. Please refer to"
    " that repository from now on:\n"
    "PyPi: https://pypi.org/project/vidify\n"
    "GitHub: https://github.com/vidify/vidify\n"
    "================================\n",
    DeprecationWarning)


setup(
    name='spotify-videos',
    version='1.8.2',
    packages='',
    description='Old repository for Vidify',
    url='https://github.com/vidify/vidify',
    license='LGPL',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Mario O.M.',
    author_email='marioortizmanero@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='spotify music video videos lyrics',
    python_requires='>=3.6',
    install_requires=['vidify'],
)
