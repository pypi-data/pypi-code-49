from setuptools import setup, find_packages
import platform


setup(
    name='spotify-videos',
    version='1.8.1',
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
    entry_points={
        'console_scripts': ['spotify-videos = spotify_videos.__main__:main']
    }
)
