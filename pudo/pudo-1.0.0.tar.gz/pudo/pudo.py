#!/usr/bin/python3
import os
import sys
import subprocess

def run(cmd):
	'''
	Usage:
		user$ python3 # or python2
		>>> import pudo
		>>> (ret, out) = pudo.run(('ls', '/root')) # or pudo.run('ls /root')
		>>> print(ret)
		>>> 0
		>>> print(out)
		>>> b'Desktop\\nDownloads\\nPictures\\nMusic\\n'
	'''
	pudoPath = os.path.join(sys.prefix, 'bin', 'pudo')
	if (not os.access(pudoPath, os.X_OK)):
		raise FileNotFoundError
	cmd = '%s %s' %(pudoPath, cmd)
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	(out, _) = process.communicate()
	ret = process.wait()
	return(ret, out)

if (__name__ == '__main__'):
	(ret, out) = run(' '.join(sys.argv[1:]))
	print(out)
	sys.exit(ret)
