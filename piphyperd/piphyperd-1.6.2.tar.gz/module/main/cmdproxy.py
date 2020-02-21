"""THIS SOFTWARE IS PROVIDED AS IS.

Released under GNU General Public License:
<https://www.gnu.org/licenses/gpl-3.0.en.html>

USE IT AT YOUR OWN RISK.

Command proxy for the PipHyperd cli.
piphyperd is a wrapper around **pip**; it can provide features like
automation or dependencies control within your workflows.

The module is published on PyPi: <https://pypi.org/project/piphyperd/>.
The code is available on GitLab: <https://gitlab.com/hyperd/piphyperd>.
"""

from typing import Tuple, Any
from .piphyperd import PipHyperd


class CmdProxy:
    """PipHyperd interface class."""

    @staticmethod
    def freeze(instance: PipHyperd) -> Tuple[str, str, int]:
        """Return pip freeze."""
        return instance.freeze()

    @staticmethod
    def list_packages(instance: PipHyperd) -> Tuple[str, str, int]:
        """Return pip list."""
        return instance.list_packages()

    @staticmethod
    def show(instance: PipHyperd, packages: Any) -> Tuple[str, str, int]:
        """Return pip show ${package}."""
        return instance.show(packages[0])

    @staticmethod
    def check(instance: PipHyperd) -> Tuple[str, str, int]:
        """Return pip check."""
        return instance.check()

    @staticmethod
    def install(instance: PipHyperd, packages: Any) -> Tuple[str, str, int]:
        """Return pip install ${packages}."""
        return instance.install(*packages)

    @staticmethod
    def uninstall(instance: PipHyperd, packages: Any) -> Tuple[str, str, int]:
        """Return pip uninstall ${packages}."""
        return instance.uninstall(*packages)

    @staticmethod
    def download(instance: PipHyperd, packages: Any) -> Tuple[str, str, int]:
        """Return pip download ${packages}."""
        return instance.download(*packages)
