import setuptools

with open('README.md', 'r') as fh:
      long_description = fh.read()

setuptools.setup(
      name="roman_nums",
      version="0.0.1",
      author="Kovalenko Nikolay",
      author_email="kovalenko.n.r-g@yandex.ru",
      description="",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/kovalenkong/roman-nums",
      packages=setuptools.find_packages(),
      python_requires='>=3.6',
)
