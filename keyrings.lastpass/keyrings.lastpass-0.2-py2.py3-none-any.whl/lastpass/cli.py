import shutil
import subprocess
from subprocess import PIPE


class AccountNotFound(Exception):
    pass


def lastpass_installed():
    return bool(shutil.which("lpass"))


def _convert_error(output):
    if "Could not find specified account" in output:
        raise AccountNotFound()
    else:
        print(output)
        raise Exception("unknown output: " + output)


def lpass(*args, input=None):
    cli_args = ["lpass"] + list(args)
    try:
        result = subprocess.run(
            cli_args, check=True, stderr=PIPE, stdout=PIPE, input=input
        )  # noqa
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as exc:
        output = exc.stderr.decode("utf-8")
        return _convert_error(output)
