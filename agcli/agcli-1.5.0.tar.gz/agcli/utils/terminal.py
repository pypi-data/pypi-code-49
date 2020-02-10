import shlex, subprocess, os
from subprocess import TimeoutExpired


error_message = """The command \"{}\" didn't terminate in the allotted {} seconds.
Please consider using the \'Run in Terminal\' button to have full power on your command execution."""

def to_cli(instruction, pipe=True, timeout=2):
    """
    Execute the 'instruction' in a shell. If 'pipe' is True, the results of this
    instruction is returned in the 'proc' object (proc.stdout or proc.stderr
    allows the user to access results). If 'pipe' is False, the result is printed
    on the current CLI.
    """
    instruction_ = ' '.join(shlex.split(instruction))
    my_env = os.environ.copy()
    # Change langage to default (english) in order to avoid errors due to
    # in the help message of the command
    my_env["LANG"] = "C"
    if pipe:
        proc = subprocess.Popen(instruction_, stdout=subprocess.PIPE,
         stderr=subprocess.PIPE, universal_newlines=True, shell=True, env=my_env)
    else:
        proc = subprocess.Popen(instruction_, universal_newlines=True, shell=True, env=my_env)
    try:
        outs, errs = proc.communicate(timeout=timeout)
    except TimeoutExpired:
        proc.kill()
        outs, errs = '', error_message.format(instruction, timeout)
    return proc.returncode, outs, errs
