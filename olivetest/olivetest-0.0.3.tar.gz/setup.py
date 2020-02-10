import setuptools

setuptools.setup(
                 name='olivetest',
                 version='0.0.3',
                 description='a python wrapper for an AIS Database API',
                 install_requires=[
                     'requests',
                     'python-dotenv'
                 ],
                 url='',
                 author='Elizabeth Golden',
                 author_email='elizabeth.golden@digitalglobe.com',
                 license='',
                 packages=setuptools.find_packages(),
                 python_requires='>=3')


# up the version
# python3 setup.py sdist bdist_wheel
# delete old dist files
# python3 -m twine upload dist/*
# @pypi
# conda info --envs
# conda remove --name olivetest --all
# conda create -n olivetest python=3.5
# conda activate olivetest
# pip install olivetest