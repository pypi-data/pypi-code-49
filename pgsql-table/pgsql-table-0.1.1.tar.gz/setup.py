from setuptools import setup

setup(name='pgsql-table',
      description='Generate SQL clauses based on table JSON definitions, Create objects of your class from selected rows',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      author='Vakhtang Zardiashvili',
      author_email='hazardland@gmail.com',
      license='MIT',
      version='0.1.1',
      keywords='orm, pgsql',
      packages=["sql"],
      url='https://github.com/hazardland/sql.py',
      python_requires='>=3.6',
     )
