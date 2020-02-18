from os import path as os_path
from os import remove as os_remove
from os import rename as os_rename
from os import listdir as os_listdir
from os import walk as os_walk
from os import sep as os_sep
from os import mkdir as os_mkdir
from os import makedirs as os_makedirs
from os import rmdir as os_rmdir
from os import startfile as os_startfile
from shutil import copy as shutil_copy
from shutil import rmtree as shutil_rmtree
from ctypes import windll

class file:
	##|
	##| filemanager = hackpy.file
	##| filemanager.getsize('file.txt')               # Return file size in bytes
	##| filemanager.exists('file.txt')                # Return True or False
	##| filemanager.remove('file.txt')                # Remove file
	##| filemanager.rmtree('dir1/dir2/dir3')          # Remove dirs
	##| filemanager.rename('file.txt', 'newfile.txt') # Rename file
	##| filemanager.copy('file.txt', 'C:\\Windows')   # Copy file
	##| filemanager.scan('C:\\')                      # Return all files in directory
	##| filemanager.start('file.txt')                 # Start file 
	##| filemanager.startAsAdmin('file.txt')          # Start file as admin
	##| filemanager.atributeHidden('file.txt')        # Hide file
	##| filemanager.atributeNormal('file.txt')        # Show file

	##| # Get files tree. (You can use tree('.') to get files tree in current directory)
	##| for file in filemanager.tree('C:\\'):
	##|     print(file)

	def exists(file):
		return os_path.exists(file)

	def remove(file):
		return os_remove(file)

	def rename(oldFile, newFile):
		return os_rename(oldFile, newFile)

	def copy(src, dst):
		return shutil_copy(src, dst)

	def scan(path):
		return os_listdir(path)

	def tree(path):
		tree = []
		for root, dirs, files in os_walk(path):
			level = root.replace(path, '').count(os_sep)
			indent = ' ' * 4 * (level)
			print('{}{}/'.format(indent, os_path.basename(root)))
			subindent = ' ' * 4 * (level + 1)
			for f in files:
				tree.append('{}{}'.format(subindent, f))
		return tree

	def mkdir(dir):
		return os_mkdir(dir)

	def rmdir(dir):
		return os_rmdir(dir)

	def mkdirs(dir):
		return os_makedirs(dir)

	def rmtree(dir):
		return shutil_rmtree(dir)

	def isdir(file):
		return os_path.isdir(file)

	def isfile(file):
		return os_path.isfile(file)

	def start(file):
		return os_startfile(file)

	def getsize(file):
		return os_path.getsize(file)

	def startAsAdmin(file):
		file   = os_path.realpath(file)
		status = windll.shell32.ShellExecuteW(None, "runas", file, '', None, 1)
		if (status == 42):
			return True, 'User allowed'
		elif (status == 5):
			return False, 'User denied'
		elif (status == 31):
			return False, 'Invalid file type'
		elif (status == 2):
			return False, 'File not found'
		else:
			return False, status

	def get_drives():
		drives = []
		bitmask = windll.kernel32.GetLogicalDrives()
		letter = ord('A')
		while bitmask > 0:
			if bitmask & 1:
				drives.append(chr(letter) + ':\\')
			bitmask >>= 1
			letter += 1
		return drives

	def atributeNormal(file):
		file   = os_path.realpath(file)
		return windll.kernel32.SetFileAttributesW(file, 1)

	def atributeHidden(file):
		file   = os_path.realpath(file)
		return windll.kernel32.SetFileAttributesW(file, 2)
