from ejcli.http import do_action
from ejcli.error import EJError

def do_control(self, cmd):
    """
    usage: do_control <action> [args]

    `action` can be one of:
        start-virtual
        Start virtual contest.

        stop-virtual
        Stop virtual contest.
    """
    cmd = cmd.strip()
    if cmd == 'start-virtual':
        if not do_action(self.url, self.cookie, 'start_virtual', 302):
            raise EJError("Failed to start virtual contest")
    elif cmd == 'stop-virtual':
        if not do_action(self.url, self.cookie, 'stop_virtual', 302):
            raise EJError("Failed to stop virtual contest")
    else:
        return self.do_help('control')
