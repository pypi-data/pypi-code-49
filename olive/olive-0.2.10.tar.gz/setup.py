import setuptools

setuptools.setup(
                 name='olive',
                 version='0.2.10',
                 description='a python wrapper for an AIS Database API',
                 install_requires=[
                     'requests',
                     'python-dotenv'
                 ],
                 url='https://github.com/GeoBigData/AISDatabase',
                 author='Elizabeth Golden',
                 author_email='elizabeth.golden@digitalglobe.com',
                 license='',
                 packages=setuptools.find_packages(),
                 python_requires='>=3')
