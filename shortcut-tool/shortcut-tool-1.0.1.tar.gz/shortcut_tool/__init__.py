import os, sys, argparse, shutil, re, textwrap

parser = argparse.ArgumentParser()

parser.add_argument(
  '-v', '--version', 
  help = 'Print the version of the program', 
  action = 'version', 
  version = '%(prog)s v0.1 develop 2020-02-22 14:04')
parser.add_argument(
  '--verbose', 
  default = False, 
  help = 'Verbose output', 
  action = 'store_true')

command_parser = parser.add_subparsers(
  title = 'operations', 
  description = 'Valid operations')

rmexe_parser = command_parser.add_parser('rmexe')
rmexe_parser.add_argument(
  '-i', '--input', '--from', 
  dest = 'input', 
  nargs = '?', 
  default = '.' + os.sep, 
  metavar = 'work-dir', 
  help = 'Directory. Specify where to find the shortcut files. Default: .' + os.sep, 
  action = 'store')
rmexe_parser.add_argument(
  '-o', '--output', '--to', 
  dest = 'output', 
  nargs = '?', 
  default = '.' + os.sep, 
  metavar = 'output-dir', 
  help = 'Directory. Specify where to store the processed files. Default: .' + os.sep, 
  action = 'store')
rmexe_parser.add_argument(
  '-d', '--auto-delete', 
  dest = 'autodelete', 
  default = False, 
  help = 'Bool. Determine whether to delete the original shortcuts. Default: False', 
  action = 'store_true')
rmexe_parser.add_argument(
  '-f', '--force', '--overwrite', 
  dest = 'overwrite', 
  default = False, 
  help = 'Bool. Determine whether to overwrite the existing files if the file is existing. Default: False', 
  action = 'store_true')
rmexe_parser.add_argument(
  '-r', '--recursive', 
  dest = 'recursive', 
  default = False, 
  help = 'Bool. Determine whether to apply the operation on shortcuts inside subdirectories. Default: False', 
  action = 'store_true')
rmexe_parser.add_argument(
  '--verbose', 
  default = False, 
  help = 'Verbose output', 
  action = 'store_true'
  )

args = parser.parse_args()

PROGAM_ERROR  = 'PROGAM_ERROR'
FILE_EXIST    = 'FILE_EXIST'
DIR_NOFOUND   = 'DIR_NOFOUND'

INFO_PROGRESS = 'INFO_PROGRESS'
INFO_VAR      = 'INFO_VAR'

def printerr(what, item, value = ''):
  if what == PROGAM_ERROR:
    print(textwrap.dedent('''\
      [ERROR] Something wrong with the program, got {0} for {1}.
      
      You may want to report this bug in https://github.com/li-zyang/zTools/issues
      ''').format(str(item), repr(value)), file = sys.stderr)
  elif what == FILE_EXIST:
    print(textwrap.dedent('''\
      [ERROR] File {0} is already existing. 
      
      Call this command with -f option if you want to overwrite the existing file.
      ''').format(str(item)), file = sys.stderr)
  elif what == DIR_NOFOUND:
    print(textwrap.dedent('''\
      [ERROR] Directory no found: {0}
      ''').format(str(item)), file = sys.stderr)
  else:
    printerr(PROGAM_ERROR, 'printerr::what', what)
  exit(1)

def printinfo(what, item, value = ''):
  if not args.verbose:
    return
  if what == INFO_PROGRESS:
    print(textwrap.dedent('''\
      [INFO]  {0}{1}''').format(str(item), (': ' + repr(value)) if (value != '') else ''))
  elif what == INFO_VAR:
    print(textwrap.dedent('''\
      [INFO]  {0} = {1}''').format(str(item), repr(value)))
  else:
    printerr(PROGAM_ERROR, 'printinfo::what', what)

target_ext = re.compile(r'\.exe\.lnk$')
printinfo(INFO_PROGRESS, 'Program started', vars(args))
for dircontent in os.walk(args.input):
  printinfo(INFO_PROGRESS, 'Searching under', dircontent[0])
  for fname in dircontent[2]:
    printinfo(INFO_PROGRESS, 'Checking', fname)
    if target_ext.search(fname):
      printinfo(INFO_PROGRESS, 'File name matched', fname)
      inp = dircontent[0] + (os.sep if not dircontent[0].endswith(os.sep) else '') + fname
      outp = args.output + (os.sep if not args.output.endswith(os.sep) else '') + target_ext.sub('.lnk', fname)
      printinfo(INFO_VAR, 'inp', inp)
      printinfo(INFO_VAR, 'outp', outp)
      printinfo(INFO_PROGRESS, 'Checking output directory', args.output)
      printinfo(INFO_VAR, 'os.listdir(args.output)', os.listdir(args.output))
      if target_ext.sub('.lnk', fname) in os.listdir(args.output) and not args.overwrite:
        printerr(FILE_EXIST, outp)
      if args.autodelete:
        # move file
        printinfo(INFO_PROGRESS, 'Current working directory', os.getcwd())
        print('- ' + inp + ' ===> + ' + outp)
        shutil.move(inp, outp)
      else:
        # copy file
        printinfo(INFO_PROGRESS, 'Current working directory', os.getcwd())
        print('  ' + inp + ' ===> + ' + outp)
        shutil.copy2(inp, outp)
  printinfo(INFO_PROGRESS, 'Work done under', dircontent[0])
  if not args.recursive:
    printinfo(INFO_PROGRESS, 'No-recursive, quited')
    break

printinfo(INFO_PROGRESS, 'Done!')