"""
Backport infrastructure to ensure older situations work correctly.

It turns out that older subprocess modules did not have the 'run'
function.  So, in effect, this is a backport of the run routine
which will work in older systems.  I'm modifying the package so that
calls elsewhere to subprocess.run() don't choke.

"""

import subprocess

if not hasattr(subprocess, 'run'):

    class CompletedProcess(object):
        """Emulating process class from the future for older pythons

        """
        def __init__(self, args, retcode, stdout, stderr):
            self.args = args
            self.returncode = retcode
            self.stdout = stdout
            self.stderr = stderr

        def check_returncode(self):
            if self.returncode:
                raise subprocess.CalledProcessError(self.returncode, self.args,
                                                    self.stdout, self.stderr)


    def run(*popenargs, input=None, timeout=None, check=False, **kwargs):
        """Emulating the run routine found in future subprocess modules
        """
        if input is not None:
            if 'stdin' in kwargs:
                raise ValueError('stdin and input args may not both be used.')
            kwargs['stdin'] = subprocess.PIPE

        with subprocess.Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate()
                raise subprocess.TimeoutExpired(
                    process.args, timeout, output=stdout, stderr=stderr)
            except:
                process.kill()
                process.wait()
                raise
            retcode = process.poll()
            if check and retcode:
                raise subprocess.CalledProcessError(
                    retcode, process.args, output=stdout + stderr)
        return CompletedProcess(process.args, retcode, stdout, stderr)

    # basically hack it in
    subprocess.run = run
