from os.path import exists
from string import Template
from subprocess import run
from sys import argv

from pyfsnotif import Watcher, MODIFY


def on_change_run(path, cmd):

    command = Template(cmd.replace('%','$path')).substitute(path=path).split(' ')

    def do_cmd(event):
        run(command)

    with Watcher() as w:
        w.add(path, MODIFY, do_cmd)


def on_change():
    path, *cmd = argv[1:]
    cmd = ' '.join(cmd)
    if exists(path):
        if '%' in cmd:
            on_change_run(path, cmd)
            return
    print(f'''Usage:
    on_change {{path}} {{cmd}}

    Use % in {{cmd}} as a placeholder for {{path}}.

    ex : on_change readme.txt cat %

    Use ^C to stop.
    ''')
