import subprocess
from ejcli.http import task_list, task_ids, download_file
from ejcli.error import EJError

def do_getfile(self, cmd):
    """
    usage: getfile <prob_id> <file> <shell command>

    Retrieve a file attached to a task.
    """
    id, file, cmd = (cmd.strip()+'  ').split(' ', 2)
    tasks = task_list(self.url, self.cookie)
    if not id or not file:
        return self.do_help('getfile')
    try: task_id = task_ids(self.url, self.cookie)[tasks.index(id)]
    except (ValueError, IndexError):
        raise EJError("No such task.")
    data = download_file(self.url, self.cookie, task_id, file)
    p = subprocess.Popen('cat '+cmd, stdin=subprocess.PIPE, shell=True)
    p.stdin.write(data)
    p.stdin.close()
    p.wait()
