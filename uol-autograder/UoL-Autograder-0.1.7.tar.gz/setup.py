from distutils.core import setup
setup(
  name = 'UoL-Autograder',         # How you named your package folder (MyLib)
  package_dir = {
      "feedback": "feedback",
      "feedback.cpp": "feedback/cpp",
      "feedback.general": "feedback/general",
      "feedback.matlab": "feedback/matlab",
      "feedback.py": "feedback/py",
      "feedback.util": "feedback/util"
  },
  packages = ["feedback",
                "feedback.cpp",
                "feedback.general",
                "feedback.matlab",
                "feedback.py",
                "feedback.util"],   # Chose the same as "name"
  version = '0.1.7',      # Start with a small number and increase it with every change you make
  license='ecl-2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Autograder extension',   # Give a short description about your library
  author = 'Titusz Ban and Dr. Craig A Evans',                   # Type in your name
  author_email = 'el16ttb@leeds.ac.uk',      # Type in your E-Mail
#   data_files=[("lookup", [
#       "feedback/lookup/comment_feedback.json",
#       "feedback/lookup/cpp_compiler_feedback.json",
#       "feedback/lookup/cpp_eval_feedback.json",
#       "feedback/lookup/cpp_static_warnings.json",
#       "feedback/lookup/cpp_style_feedback.json",
#       "feedback/lookup/py_eval_feedback.json",
#       "feedback/lookup/py_runner_feedback.json",
#       ]),
#       ("cpp", [
#           "feedback/cpp/cpp_eval_util.cpp",
#           "feedback/cpp/cpp_eval_util.h",
#           "feedback/cpp/empty_main.cpp",
#           "feedback/cpp/json.hpp"
#       ])],
  include_package_data=True,
  keywords = [],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pylint',
          'pylint',
          'jinja2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Education',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: Free For Educational Use',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)