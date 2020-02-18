#!/usr/bin/env python3

import pylineblocks
import shutil

def reindentFile(filePath, inTabSymbol, outTabSymbol, cleanTrailingTabsAndSpaces=False, backupPostfix=None, outputOverride=None):
	newBlocks = []
	with open(filePath, 'r') as pyfile:
		try:
			for block in pylineblocks.splitIntoBlocks(pyfile, cleanTrailingTabsAndSpaces=cleanTrailingTabsAndSpaces):
				newBlocks.append(pylineblocks.reindentBlock(block, inTabSymbol, outTabSymbol))
		except ValueError as verr:
			raise ValueError(f'while processing file {filePath}:\n{verr}')
	if not outputOverride and backupPostfix:
		shutil.move(filePath, str(filePath) + backupPostfix)
	outPath = outputOverride if outputOverride else filePath
	with open(outPath, 'w') as pyfile:
		for line in sum(newBlocks, []):
			pyfile.write(line + '\n')

if __name__ == '__main__':
	import argparse, sys
	from pathlib import Path

	# Parsing the arguments
	parser = argparse.ArgumentParser(description='Freely switch between Python indentation styles')

	parser.add_argument('input_path', type=str,
	                    help='Location of the input')

	req_grp = parser.add_argument_group(title='required flags')
	req_grp.add_argument('-f', '--from-tabs', choices=['hard', 'soft4', 'soft2'], required=True,
	                    help='Style of indentation to convert from')
	req_grp.add_argument('-t', '--to-tabs', choices=['hard', 'soft4', 'soft2'], required=True,
	                    help='Style of indentation to convert to')

	parser.add_argument('-r', '--recursive', action='store_true',
	                    help='Recursively find all .py files in the input path and convert them')
	parser.add_argument('-b', '--backup-postfix', type=str, default='~', metavar='postfix',
	                    help='Back up unmodified input file(s) under their original name(s) with ' \
	                         'this postfix. Set to an empty string to suppress backups. Default: ~')
	parser.add_argument('-rt', '--remove-trailing', action='store_true',
	                    help='Remove any trailing tabs or spaces, leaving multiline string literals intact')
	parser.add_argument('-q', '--quiet', action='store_true',
	                    help='Suppress all messages and prompts except for errors')
	parser.add_argument('-o', '--output', type=str, default=None, metavar='output_file',
	                    help='Output file name. Default: overwrite the original file. Note: does not work with the -r option')

	args = parser.parse_args()

	# Printing a short summary of what we're going to do, display prompt
	def printMessage(msg):
		if not args.quiet:
			print(msg)

	def prompt(msg):
		if not args.quiet:
			sys.stdout.write(f'{msg} (y/n) ')
			return input() == 'y'
		else:
			return True

	inPath = Path(args.input_path)
	if args.recursive:
		if args.output:
			sys.stderr.write('Error: cannot use --output and --recursive at the same time!\n')
			sys.exit(1)
		if not inPath.is_dir():
			sys.stderr.write(f'Error: pyreindent used with --recursive and input path {inPath} is not a directory\n')
			sys.exit(1)
		files = list(inPath.rglob('*.py'))
		if len(files) == 0:
			sys.stderr.write(f'Error: input directory {inPath} contains no .py files\n')
			sys.exit(1)
	else:
		if not inPath.is_file():
			sys.stderr.write(f'Error: input path is not a file\n')
			sys.exit(1)
		files = [ inPath ]

	if args.output:
		printMessage(f'A version of the file\n\n{files[0]}\n\nindented with {args.to_tabs} tabs instead of {args.from_tabs} tabs will be written to\n\n{args.output}\n')
	else:
		printMessage(f'Indentation will be changed from {args.from_tabs} tabs to {args.to_tabs} tabs in the following files:\n')
		for fn in files:
			printMessage(fn)
		printMessage('')
		if args.backup_postfix:
			printMessage(f'The original files will be backed up under their original names with {args.backup_postfix} appended at the end.')
		else:
			printMessage('The original files will not be preserved.')
	if args.remove_trailing:
		printMessage('Any trailing tabs or spaces outside of multiline string literals will be removed.')

	if not prompt('Proceed?'):
		printMessage('Exiting')
		sys.exit(0)

	# Do the convertion itself
	tabSymbolsDict = { 'hard' : '\t',
	                   'soft4' : '    ',
	                   'soft2' : '  ' }
	fromTabsSymb = tabSymbolsDict[args.from_tabs]
	toTabsSymb = tabSymbolsDict[args.to_tabs]

	if args.output:
		reindentFile(files[0], fromTabsSymb, toTabsSymb, cleanTrailingTabsAndSpaces=args.remove_trailing, outputOverride=args.output)
	else:
		for file in files:
			reindentFile(file, fromTabsSymb, toTabsSymb, cleanTrailingTabsAndSpaces=args.remove_trailing, backupPostfix=args.backup_postfix)
