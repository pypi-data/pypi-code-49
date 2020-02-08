"""
THIS SOFTWARE IS PROVIDED AS IS
and under GNU General Public License. <https://www.gnu.org/licenses/gpl-3.0.en.html>
USE IT AT YOUR OWN RISK.

Command proxy for the PipHyperd cli.
piphyperd is a wrapper around **pip**; it can provide features like
automation or dependencies control within your workflows.

The module is published on PyPi <https://pypi.org/project/piphyperd/>.

The code is available on GitLab <https://gitlab.com/hyperd/piphyperd>.
"""


class CmdProxy:
    """
    PipHyperd interface class.
    """

    @staticmethod
    def freeze(instance):
        """ return pip freeze """
        return instance.freeze()

    @staticmethod
    def list_packages(instance):
        """ return pip list """
        return instance.list()

    @staticmethod
    def show(instance, packages):
        """ return pip show ${package} """
        return instance.show(packages[0])

    @staticmethod
    def check(instance):
        """ return pip check """
        return instance.check()

    @staticmethod
    def install(instance, packages):
        """ return pip install ${packages} """
        return instance.install(*packages)

    @staticmethod
    def uninstall(instance, packages):
        """ return pip uninstall ${packages} """
        return instance.uninstall(*packages)

    @staticmethod
    def download(instance, packages):
        """ return pip download ${packages} """
        return instance.download(*packages)
