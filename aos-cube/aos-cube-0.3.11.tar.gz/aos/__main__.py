import os, sys
import traceback
import click
import errno

from imp import reload
from aos import __version__, __email__
from aos.util import error, ProcessException

class AOSCLI(click.MultiCommand):
    def list_commands(self, ctx):
        cmds = []
        aosdir = os.path.dirname(os.path.abspath(__file__))
        for cmdfile in os.listdir(os.path.join(aosdir, "commands")):
            if cmdfile == "__init__.py":
                continue

            if cmdfile.endswith(".py"):
                valid_cmd = 1

                # ota depends paho-mqtt ...
                if cmdfile == "ota.py":
                    try:
                        import paho.mqtt.client
                    except:
                        valid_cmd = 0

                if valid_cmd:
                    cmds.append(cmdfile[:-3])

        cmds.sort()
        return cmds

    def get_command(self, ctx, cmd_name):
        mod = None
        try:
            mod = __import__("aos.commands." + cmd_name, None, None,
                             ["cli"])
        except ImportError:
            try:
                return self._handle_obsolate_command(cmd_name)
            except AttributeError:
                raise click.UsageError('No such command "%s"' % cmd_name, ctx)

        return mod.cli

    @staticmethod
    def _handle_obsolate_command(name):
        obsolates = ["setup", "new", "ls", "import", "add", "rm", "deploy", "codes", "publish",
                     "update", "sync", "status", "makelib",]

        if name in obsolates:
            raise click.UsageError('Command "%s" is deprecated since 0.3.x ...\n\nIf you still need such command, please install aos-cube 0.2.x with:\n\n  $ pip install aos-cube==0.2.66\n\nAny feedback please contact with: %s\n' % (name, __email__))

        if name == "scons":
            from aos.commands import make
            return make.cli

        raise AttributeError()

@click.command(
    cls=AOSCLI,
    context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("--verbose", "-v", is_flag=True, help="Verbose diagnostic output")
@click.option("--very-verbose", "-vv", is_flag=True, help="Very verbose diagnostic output")
@click.version_option(__version__, message="%(version)s")
@click.pass_context
def cli(ctx, verbose, very_verbose):
    pass

def main():
    try:
        reload(sys)
        sys.setdefaultencoding('UTF8')
    except:
        pass

    # Convert the "\\" to "/" on Windows for AOS_SDK_PATH
    aos_sdk_path = os.environ.get("AOS_SDK_PATH")
    if aos_sdk_path:
        os.environ["AOS_SDK_PATH"] = aos_sdk_path.replace("\\", "/")

    ret = 0
    try:
        cli(None)
    except ProcessException as e:
        error(
            "\"%s\" returned error code %d.\n"
            "Command \"%s\" in \"%s\"" % (e.args[1], e.args[0], e.args[2], e.args[3]), e.args[0])
    except OSError as e:
        traceback.print_exc()
        if e.args[0] == errno.ENOENT:
            error(
                "Could not detect one of the command-line tools.\n"
                "You could retry the last command with \"-v\" flag for verbose output\n", e.args[0])
        else:
            error('OS Error: %s' % e.args[1], e.args[0])
    except KeyboardInterrupt as e:
        info('User aborted!', -1)
        ret = 255
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        error("Unknown Error: %s" % e, 255)

    return ret

if __name__ == "__main__":
    sys.exit(main())
