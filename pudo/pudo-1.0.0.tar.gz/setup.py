#!/usr/bin/python3
import setuptools
from setuptools.command.install import install
import pudo


srcCode = '''\
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>
#include <string.h>

int main(int argc, char **argv)
{
	int rootUid, rootGid;
	int ret;
	/* args validation */
	if (argc < 2) {
		printf("Usage: %s <cmd> <args> ..\\n", argv[0]);
		exit(1);
	}
	/* gain root user privilege */
	rootUid = geteuid();
	rootGid = getegid();
	if (setuid(rootUid) != 0) {
		perror("setuid");
		return(1);
	}
	if (setgid(rootGid) != 0) {
		perror("setgid");
		return(1);
	}
	/* execute the command with root privilege */
	ret = execvp(argv[1], &(argv[1]));
	if (ret < 0) {
		if (errno == ENOENT) {
			fprintf(stderr, "pudo: %s: command not found\\n", argv[1]);
		} else {
			char msg[128] = {0};
			sprintf(msg, "pudo: %s", argv[1]);
			perror(msg);
		}
	}
	return(1);
}
'''
class PudoCmdInstall(install):
	def run(self):
		import os
		import sys
		import subprocess
		import tempfile
		import distutils.spawn
		# check or install gcc
		if (not distutils.spawn.find_executable('gcc')):
			import pip
			if hasattr(pip, 'main'):
				pip.main(['install', 'gcc7'])
			else:
				pip._internal.main(['install', 'gcc7'])
		# compile and install pudo
		srcFile = tempfile.mktemp(suffix='.c', prefix='pudo')
		fd = open(srcFile, 'w')
		fd.write(srcCode)
		fd.close()
		binFile = os.path.join(sys.prefix, 'local', 'bin', 'pudo')
		subprocess.check_call(('gcc', srcFile, '-o', binFile))
		subprocess.check_call(('chmod', 'u+s', binFile))
		os.unlink(srcFile)
		install.run(self)


setuptools.setup(
    name='pudo', 
    version=pudo.VERSION,
    author='Madhusudhan Kasula',
    author_email='kasula.madhusudhan@gmail.com',
    description='Python version of linux sudo command without password prompt',
    long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/kasulamadhusudhan/pudo',
	data_files=[('bin', ['/usr/local/bin/pudo'])],
	cmdclass={'install': PudoCmdInstall},
	packages=setuptools.find_packages(),
	use_2to3=True,
	classifiers=[
		'Programming Language :: C',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 2',
		'Operating System :: POSIX :: Linux',
		'Environment :: Console',
		'Intended Audience :: Developers',
	],
)
