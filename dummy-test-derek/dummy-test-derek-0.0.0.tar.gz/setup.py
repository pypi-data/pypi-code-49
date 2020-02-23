import setuptools as st

st.setup(
  version = "0.0.0",
  name = "dummy-test-derek",
  description = "A dummy module to test",
  keywords = "dummy test",
  url = "https://github.com/derek-ye/pip3-class", # github repo url
  download_url = "https://github.com/derek-ye/pip3-class/tarball/0.0.0",
  author = "derek-ye",
  license = "MIT",
  # namespace_packges
  packages = st.find_packages(exclude=["tests"]),
  install_requires = [
    # "package-name>=3.0.0"
  ],
  python_requires = ">=3.3",
  classifiers = [
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
  ]
)