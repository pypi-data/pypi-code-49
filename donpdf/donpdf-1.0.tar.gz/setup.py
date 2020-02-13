import setuptools
from pathlib import Path
setuptools.setup(
    name="donpdf",
    version=1.0,
    long_description=Path(r"C:\Users\dkrau\codewithmosh\TheCompletePythonCourse\PythonPackageIndex-10\HELLOWORLD\donPdf\README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)