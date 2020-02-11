from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-l10n-extensions-django-3',
    version='1.0.7',
    author=u'Cees van Wieringen',
    author_email='ceesvw@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    include_package_data=True,
    install_requires=['GitPython==1.0.1', 'Django>=3', 'polib>=1.0'],
    url='https://github.com/ceasaro/django-l10n-extensions',
    license='',
    description="Extend Django 3 with L10N features",
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    key_words=['django', 'l10n', ]
)
