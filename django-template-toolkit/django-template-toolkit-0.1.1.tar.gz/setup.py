from setuptools import setup, find_packages
from toolkit import __version__


def read(file):
    with open(file, 'r') as f:
        return f.read()


setup(
    name='django-template-toolkit',
    version='.'.join(str(x) for x in __version__),
    description='A collection of useful templates & tags for the Django web framework',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=2.2',
    ],
    python_requires='>=3.6',
    author='Gerard Krijgsman',
    author_email='python@visei.com',
    url='https://github.com/ghdpro/django-template-toolkit',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
