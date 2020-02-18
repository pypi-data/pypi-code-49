"""
flask-gridify
-------------


"""
from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and (not line.startswith("#") and not line.startswith("-"))]


def load_readme():
    import pypandoc
    try:
        readme_rst = pypandoc.convert_file('README.md', 'rst')
        return readme_rst
    except OSError:
        print('pandoc installation not found, installing it...')
        from pypandoc.pandoc_download import download_pandoc
        download_pandoc()
        print('pandoc installed, retrying README.md conversion...')
        readme_rst = pypandoc.convert_file('README.md', 'rst')
        return readme_rst


setup(
    name='flask-gridify',
    version='0.1.1',
    url='https://github.com/michaelsobczak/flask-gridify',
    download_url='https://github.com/michaelsobczak/flask-gridify/archive/0.1.0.tar.gz',
    license='MIT',
    author='Michael Sobczak',
    author_email='mikesobczak.code@gmail.com',
    description='Automatically create editable grids in browser from SQLAlchemy models',
    long_description=load_readme(),
    packages=['flask_gridify'],
    keywords=['Flask', 'FlaskSQLAlchemy', 'FlaskRestless', 'jsgrid', 'data table'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)