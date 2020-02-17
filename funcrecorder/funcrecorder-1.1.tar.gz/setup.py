from setuptools import setup

#https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi


#python setup.py sdist bdist_wheel

#uploads all the packages in dist directory, watch out!
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

#install_requires=[]
#https://packaging.python.org/discussions/install-requires-vs-requirements/

setup(
    name='funcrecorder',
    version='1.1',
    scripts=['recorder.py'],

)
