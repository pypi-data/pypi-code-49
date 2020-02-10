"""
Plugin that allows you to release a python package to pypi

## Requirements

`pip install twine`
"""

from __future__ import absolute_import, division, print_function

import os.path
import subprocess

import ctl
import ctl.config
import select
import confu.schema

from ctl.auth import expose
from ctl.plugins import release
from ctl.exceptions import UsageError
from ctl.docs import pymdgen_confu_types

PYPI_TEST_REPO = "https://test.pypi.org/legacy/"
PYPY_LIVE_REPO = ""

try:
    from twine.commands.upload import upload as twine_upload
    from twine.commands.check import check as twine_check
    from twine.settings import Settings
except ImportError:
    pass


@pymdgen_confu_types()
class PyPIPluginConfig(release.ReleasePluginConfig):

    """
    Configuration schema for `PyPIPlugin`
    """

    # dont set a default for this since it determines
    # which user will be used to upload the package, so we
    # want to ensure this is alsways consciously set in
    # the plugin config
    config_file = confu.schema.Str(help="path to pypi config file (e.g. ~/.pypirc)")

    # PyPI repository name, needs to exist in your pypi config file
    pypi_repository = confu.schema.Str(
        help="PyPI repository name - needs to exist " "in your pypi config file",
        default="pypi",
    )

    # sign releases
    sign = confu.schema.Bool(help="sign releases", default=False)
    sign_with = confu.schema.Str(help="sign release with this program", default="gpg")
    identity = confu.schema.Str(help="sign release with this identity", default=None)


@ctl.plugin.register("pypi")
class PyPIPlugin(release.ReleasePlugin):

    """
    facilitate a PyPI package release

    # Instanced Attributes

    - dry_run (`bool`): are we doing a dry run?
    - pypi_repository (`str`): name of the pypi repostiroy we will be targeting
    - pypirc_path (`str`): path to to pypi config file
    - twine_settings (`twine.Settings`)
    """

    class ConfigSchema(ctl.plugins.PluginBase.ConfigSchema):
        config = PyPIPluginConfig()

    @property
    def dist_path(self):
        """
        the path for dist output
        """
        return os.path.join(self.repository.checkout_path, "dist", "*")

    def prepare(self):
        super(PyPIPlugin, self).prepare()
        self.shell = True
        self.pypi_repository = self.get_config("pypi_repository")
        self.pypirc_path = os.path.expanduser(self.config.get("config_file"))
        self.twine_settings = Settings(
            config_file=self.pypirc_path,
            repository_name=self.pypi_repository,
            sign=self.get_config("sign"),
            identity=self.get_config("identity"),
            sign_with=self.get_config("sign_with"),
        )

    def _release(self, **kwargs):
        """
        Build dist and validate dist and then upload to pypi
        """

        # build dist and validate package
        self._validate()

        # upload to pypi repo
        self._upload()

    def _build_dist(self, **kwargs):
        """
        Build dist
        """

        command = ["rm dist/* -rf", "python setup.py sdist"]
        self._run_commands(command)

    def _validate(self, **kwargs):
        """
        Build dist and validate
        """

        self._build_dist()
        self._validate_dist(**kwargs)
        self._validate_manifest(**kwargs)

    def _validate_dist(self, **kwargs):
        """
        Validate dist
        """

        twine_check([self.dist_path])

    def _validate_manifest(self, **kwargs):
        pass

    def _upload(self, **kwargs):
        """
        Upload to pypi
        """

        self.log.info("Using pypi config from {}".format(self.pypirc_path))

        if not self.dry_run:
            twine_upload(self.twine_settings, [self.dist_path])
