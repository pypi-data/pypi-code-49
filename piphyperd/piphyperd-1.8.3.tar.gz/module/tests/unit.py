"""THIS SOFTWARE IS PROVIDED AS IS.

Released under GNU General Public License:
<https://www.gnu.org/licenses/gpl-3.0.en.html>

USE IT AT YOUR OWN RISK.

PipHyperd unit testing.

The module is published on PyPi: <https://pypi.org/project/piphyperd/>.
The code is available on GitLab: <https://gitlab.com/hyperd/piphyperd>.
"""

import unittest
import os
import shutil
from pathlib import Path
import subprocess
from ..main.piphyperd import PipHyperd


class TestMethods(unittest.TestCase):
    """PipHyperd unit testing class."""

    def setUp(self) -> None:
        """Test setup."""
        self.piphyperd = PipHyperd()
        self.venv_path = "{}/python-venv".format(os.path.dirname(__file__))

        process = subprocess.run(
            ["virtualenv",
             self.venv_path], check=True,
            capture_output=True)

        process.check_returncode()

    def tearDown(self) -> None:
        """Remove venv after testing."""
        self.wiper(self.venv_path)

    def test_a_is_not_none(self) -> None:
        """Assert that PipHyperd is not None."""
        self.assertIsNotNone(self.piphyperd)

    def test_b_wrong_python_path(self) -> None:
        """Raise a FileNotFoundError when python path does not exist."""
        with self.assertRaises(FileNotFoundError):
            PipHyperd(python_path=Path("/path/to/nothing")).check()

    def test_c_install(self) -> None:
        """Assert that after installing is in the output."""
        self.piphyperd = PipHyperd(
            python_path=Path("{}/bin/python3".format(self.venv_path)))

        self.piphyperd.install("ansible")

        output, _, _ = self.piphyperd.list_packages()

        self.assertIn("ansible", output)

    def test_d_uninstall(self) -> None:
        """Assert that after installing is in the output."""
        self.piphyperd = PipHyperd(
            python_path=Path("{}/bin/python3".format(self.venv_path)))

        self.piphyperd.uninstall("ansible")

        output, _, _ = self.piphyperd.list_packages()

        self.assertNotIn("ansible", output)

    def test_e_list_outdated(self) -> None:
        """Assert that "Latest" is in the output."""
        self.piphyperd = PipHyperd(
            python_path=Path("{}/bin/python3".format(self.venv_path)))

        # install an outdated version of yarl
        self.piphyperd.install("yarl==1.1.0")

        output, _, _ = self.piphyperd.list_packages(True)

        self.assertIn("Latest", output)

    @staticmethod
    def wiper(folder: str) -> None:
        """Clean up folders."""
        if os.path.isdir(folder):
            shutil.rmtree(folder)


if __name__ == '__main__':
    unittest.main()
