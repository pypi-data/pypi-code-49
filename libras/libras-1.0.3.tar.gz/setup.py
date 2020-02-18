import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='libras',
                 version='1.0.3',
                 description='Based on the flask web framework',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author='barleyawn',
                 author_email='barleyawn@qq.com',
                 url='https://github.com/barleyawn/libras',
                 keywords='flask web restful',
                 packages=setuptools.find_packages(),
                 zip_safe=False,
                 include_package_data=True,
                 classifiers=(
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: Apache Software License",
                     "Framework :: Flask"
                 ))
