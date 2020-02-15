from setuptools import setup, find_packages

requirements = [
    'numpy',
    'opencv-python',
    'flask',
    'tezign',
    'mxnet',
    'sklearn',
    'scenedetect',
    'moviepy',
    'Pillow',
    'torch==1.1.0',
    'torchvision==0.3.0',
]

__version__ = '0.1.15'

setup(
    # Metadata
    name='ai-graphics',
    version=__version__,
    author='CachCheng',
    author_email='tkggpdc2007@163.com',
    url='https://github.com/CachCheng/Python_Cookbook',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    description='AI Graphics Toolkit',
    license='Apache-2.0',
    # Package info
    packages=find_packages(exclude=('docs', 'tests', 'scripts')),
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)
