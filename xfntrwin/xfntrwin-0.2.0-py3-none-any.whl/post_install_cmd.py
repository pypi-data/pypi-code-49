import sys
from subprocess import run

a = run(['pwd'],capture_output=True,text=True)
print(a.stdout)
print(sys.argv[1])
print("\npost_install_cmd.py executed\n")



