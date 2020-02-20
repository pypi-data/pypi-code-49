import sys

if '--bash' in sys.argv or '--zsh' in sys.argv:
    import ejcli.bashhelper
    ejcli.bashhelper.main()
    exit(0)

from ejcli.cmd import BruteCMD
import cmd, builtins

def input(prompt = ''):
    while True:
        try: return builtins.input(prompt)
        except KeyboardInterrupt: pass

cmd.input = input

BruteCMD().cmdloop()
