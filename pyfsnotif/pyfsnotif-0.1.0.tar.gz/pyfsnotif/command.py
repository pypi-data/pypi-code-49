from string import template
from sunprocess import run

from pyfsnotif import Watcher, MODIFY


def on_change(path, cmd):

    command = template(cmd).subtitute(path=path)

    def do_cmd(event):
        run(command)

    with Watcher() as w:
        w.add(path, MODIFY, do_cmd)


