r"""Command-line tool to pypublish

Usage::

    $ pypublish_publish

"""
import sys
import os
import shutil

def main():
  args = []
  for i in range(2, len(sys.argv)):
    args.append(sys.argv[i])

  getattr(sys.modules[__name__], sys.argv[1])(args)

#args: path
def publish (args):
  print("Executing publish ... " + str(args))
  
  if len(args) > 0:
    path = args[0]
    path = os.path.join(os.getcwd(), path) if not path.startswith(os.path.sep) else path
  else:
    path = os.getcwd()
  if path.endswith(os.path.sep):
    path = path[0:-1]
  
  facade = pypublish.Publisher(path)
  facade.publish()

#args: type
def help (args):
  print("Executing help ... " + str(args))
  _show_help(*args)

def _show_help (type=None):
  print("options: base, inheritance, class, data, test.")
  print("- base: Show a template to learn the main stuffs.")
  print("- inheritance: Show some templates to learn the inheritance.")
  print("- class: Show an example of class object.")
  print("- css: Show css files.")
  print("- data: Show an example of data file.")
  print("- test: Download templates to use in learning.")
  print("")

if __name__ == '__main__':
    main()
