from os.path import exists
from string import Template
from subprocess import run
from sys import argv

from pyfsnotif import Watcher, MODIFY


usage = f'''Usage:
    on_change {{path}} {{cmd}}

    Use % in {{cmd}} as a placeholder for {{path}}.

    ex : on_change readme.txt cat %

    Use ^C to stop.
'''


def on_change_run(path, cmd):

    command = Template(cmd.replace('%','$path')).substitute(path=path).split(' ')

    def do_cmd(_evt):
        try:
            run(command)
        except Exception as x:
            print(f' ! {" ".join(command)} ! {x}')

    do_cmd(None)

    with Watcher() as w:
        w.add(path, MODIFY, do_cmd)


def on_change():
    path, *cmd = argv[1:]
    cmd = ' '.join(cmd)
    if exists(path):
        on_change_run(path, cmd)
    else:
        print(usage)
