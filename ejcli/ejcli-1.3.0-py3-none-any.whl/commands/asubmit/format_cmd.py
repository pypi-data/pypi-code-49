import subprocess
from ejcli.error import EJError

def check_exists(file, options=set()):
    return True

def read_file(path, options=set()):
    p = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE)
    data = p.stdout.read()
    if p.wait():
        raise EJError("Process terminated with exit code %d"%p.wait())
    return data
