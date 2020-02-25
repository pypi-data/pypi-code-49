import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='gfk-models',
    version='0.0.19',
    packages=[
        'gfk_models',
        'gfk_models.gfk_base',
        'gfk_models.gfk_base.templatetags',
        'gfk_models.gfk_helpers',
        'gfk_models.gfk_helpers.functions',
        'gfk_models.vote',

        'gfk_models.like',
        'gfk_models.like.migrations',

        'gfk_models.qna',
        'gfk_models.qna.migrations',

        'gfk_models.review',
        'gfk_models.review.migrations',

        'gfk_models.screenshot',
        'gfk_models.screenshot.migrations',
    ],
    include_package_data=True,
    license='BSD License',  # example license
    description='Set of GenericForeignKey models.',
    # long_description=README,
    # long_description_content_type="text/markdown",
    # variant="CommonMark",
    author='Alexander Temchenko',
    author_email='ksanderer@gmail.com',
    install_requires=[
        "django >=2.2",
        'bleach >=1.4.2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)