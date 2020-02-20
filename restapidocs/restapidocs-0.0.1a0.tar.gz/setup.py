from setuptools import setup
import os

def get_version(path):
    fn = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        path, "__init__.py")
    with open(fn) as f:
        for line in f:
            if '__version__' in line:
                parts = line.split("=")
                return parts[1].split("'")[1]

setup(
    name="restapidocs",
    description="Decorator for Flask end point to add OpenAPI documentation to end point using classes that generate a YAML documentation",
    url="https://github.com/jordsti/restapidocs",
    version=get_version("restapidocs"),
    maintainer="Jordsti",
    maintainer_email="jord52@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python"] + [
            "Programming Language :: Python :: %s" % x
            for x in "3.7".split()],
    install_requires=['flasgger>=0.9.0'],
    include_package_data=True,
    zip_safe=False,
    packages=['restapidocs'],
    py_modules=['restapidocs'],
)