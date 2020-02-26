from setuptools import setup, find_packages
import os

version = os.environ.get('CI_COMMIT_TAG', "0.0.0").replace("-", "")
print(version)

setup(
  name = 'UoL-Autograder',         # How you named your package folder (MyLib)
  package_dir = {
      "feedback": "feedback",
      "feedback.cpp": "feedback/cpp",
      "feedback.general": "feedback/general",
      "feedback.py": "feedback/py",
      "feedback.util": "feedback/util"
  },
  packages = ["feedback",
                "feedback.cpp",
                "feedback.general",
                "feedback.py",
                "feedback.util"],
  version = version,
  license='ecl-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'General testing and feedback',
  author = 'Titusz Ban, Craig Evans & Sam Wilson @ Leeds Institute for Teaching Excellence',
  author_email = 'el16ttb@leeds.ac.uk',
  package_data={
      "": [
        "*.json",
        "*.cpp",
        "*.h",
        "*.hpp",
      ]
  },
  include_package_data=True,
  keywords = [],
  install_requires=[
          'numpy',
          'pylint',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Education',
    'Topic :: Software Development :: Build Tools',
    'License :: Free For Educational Use',   
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)