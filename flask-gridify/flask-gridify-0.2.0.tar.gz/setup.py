"""
flask-gridify
-------------


"""
from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and (not line.startswith("#") and not line.startswith("-"))]


_REPO_URL = 'https://github.com/michaelsobczak/flask-gridify'

_LONG_DESCRIPTION = """flask-gridify
=============

flask extension for making editable grids from sqlalchemy models. In the
``example`` directory of the repo you can find a mimimal flask app
demonstrating features and usage of the extension. The code snippets
below are all from the example.

Usage
-----

Like other flask extensions, you’ll initialize it with the app. Below is
from the “example” application in the repo.

::

   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_gridify import FlaskGridify

   app = Flask(__name__)
   db = SQLAlchemy(app)

   # initialize the FlaskGridify extension
   grid = FlaskGridify(app, flask_sqlalchemy_db=db, root_url_prefix='/grids')

Then for each model class you want grids for you’ll call the ``gridify``
function of the ``grid`` object above and pass in the SQLAlchemy model
**class**

::

   from .models import User, Note
   grid.gridify(User)
   grid.gridify(Note)

When you run the app, you’ll have the following URL routes:

-  /

   -  This route demonstrates useage of the Jinja macros that allow for
      creation of grids inside of your application templates

-  /grids/note

   -  This is the grid page created for the Note model

-  /grids/user

   -  This is the grid page created for the User model

Additionally, the extension will create and use a REST API for each
gridified model class that can be used by your application. It uses the
`FlaskRestless <https://flask-restless.readthedocs.io/en/stable/>`__
extension so information on the formatting and URLs can be found there

Using FlaskGridify in Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The extension also exposes Jinja template macros you can use to embed
the editable grids for models in your pages. In the
``example/templates/index.html.jinja`` template file we create grids for
the User and Note model classes like so:

::

       <div id="user-grid"></div>
       <div id="note-grid"></div>
       {{ macros.create_grid("user-grid", "user", GRID_REGISTRY["user"]) }}
       {{ macros.create_grid("note-grid", "note", GRID_REGISTRY["note"]) }}

Developer information
---------------------

This project uses a Makefile to build, upload and run example app.
You’ll need to have installed your ``pipenv`` with ``--dev`` to ensure
you have the necessary packages for development.

-  ``make build``

   -  this will build a source distribution of the package

-  ``make upload``

   -  this will build the package and upload it to pypi

-  ``make run``

   -  this runs the example app in the repo

TODO
----

-  Add Enum field support
-  Add relationship field support

   -  many to one
   -  many to many

-  Clean up the exposed macros to avoid reference to ``GRID_REGISTRY``

Dependencies
------------

-  Server side

   -  `Flask-SQLAlchemy <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>`__
   -  `Flask-Restless <https://flask-restless.readthedocs.io/en/stable/>`__

-  Client side

   -  `jsgrid <http://js-grid.com/>`__
"""

setup(
    name='flask-gridify',
    version='0.2.0',
    url=_REPO_URL,
    download_url='https://github.com/michaelsobczak/flask-gridify/archive/0.1.0.tar.gz',
    license='MIT',
    author='Michael Sobczak',
    author_email='mikesobczak.code@gmail.com',
    description='Automatically create editable grids in browser from SQLAlchemy models',
    long_description=_LONG_DESCRIPTION,
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