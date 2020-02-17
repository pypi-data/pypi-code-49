import platform
import subprocess

import click

from yeahyeah.core import YeahYeahPlugin
from yeahyeah.context import YeahYeahContext
from yeahyeah.objects import SerialisableMenuItem, MenuItemList

default_settings_file_name = "path_items.yaml"


class PathItem(SerialisableMenuItem):
    """A named UNC path"""

    def __init__(self, name, path, help_text=None):
        super().__init__(name, help_text)
        self.path = path

    def __str__(self):
        return f"PathItem {self.name}:{self.path}"

    def get_parameters(self):
        return {"path": self.path}

    @property
    def help_text(self):
        if self._help_text is None:
            return f"open {self.path}"
        else:
            return self._help_text

    def to_click_command(self):
        """This url pattern as a click command that can be added with add_command()

        Returns
        -------
        click.command
        """

        @click.command(name=self.name, help=self.help_text)
        @click.option("--print-only", "-p", is_flag=True)
        def the_command(print_only):
            click.echo(self.path)
            if not print_only:
                open_terminal(self.path)

        return the_command

    @staticmethod
    def from_dict(dict_in):
        """Create a UrlPattern object from given dict.

        Dict should have been created with to_dict()
        """
        name = list(dict_in.keys()).pop()
        values = dict_in[name]
        path = values["path"]
        help_text = values.get("text", None)

        return PathItem(name=name, path=path, help_text=help_text)


class PathItemList(MenuItemList):
    """A persistable list of path items"""

    item_classes = [PathItem]


class PathItemPlugin(YeahYeahPlugin):

    slug = "path_items"
    short_slug = "path"

    def __init__(self, item_list: PathItemList):
        """Plugin that holds PathItems

        Parameters
        ----------        
        item_list: PathItemList, optional
            Optional list of items




        """
        self.item_list = item_list
        self.config_file_path = None

    @classmethod
    def init_from_context(cls, context: YeahYeahContext):
        """
        Parameters
        ----------
        context: YeahYeahContext
            Context containing location to settings file etc.

        Returns
        -------

        """
        return cls.init_from_file_path(
            context.settings_path / default_settings_file_name
        )

    @classmethod
    def init_from_file_path(cls, config_file_path):
        """
        Parameters
        ----------
        config_file_path: Pathlike
            path to path item config file

        Returns
        -------

        """
        cls.assert_config_file(config_file_path)
        with open(config_file_path, "r") as f:
            item_list = PathItemList.load(f)

        obj = cls(item_list=item_list)
        obj.config_file_path = config_file_path
        return obj

    def save(self):
        """Save current list to disk if possible"""
        if self.config_file_path:
            with open(self.config_file_path, "w") as f:
                self.item_list.save(file=f)

    @staticmethod
    def assert_config_file(config_file_path):
        """Make sure config file exists. If not, create an example config file"""
        if config_file_path.exists():
            return
        else:
            config_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(config_file_path, "w") as f:
                example_patterns = [
                    PathItem(
                        name="home",
                        path="/home/a_user/",
                        help_text="(Example) Open home directory",
                    ),
                    PathItem(
                        name="external_disk",
                        path="/mnt/some_mount/user/something",
                        help_text="(Example) Open that external disk",
                    ),
                ]
                PathItemList(items=example_patterns).save(f)
            click.echo(
                f"PathItem config file {config_file_path} did not exist. "
                f"Creating with default contents.."
            )

    def get_commands(self):
        """

        Returns
        -------
        List[click.Command]
        """
        commands = []
        for item in self.item_list:
            command = item.to_click_command()
            command.help += f" ({self.short_slug})"
            commands.append(command)

        return commands

    def get_admin_commands(self):
        """

        Returns
        -------
        List[click.Command]
            list of click commands that can be used to admin this plugin

        """

        @click.command()
        def status():
            """Print some info for this plugin"""
            status_str = (
                f"PathItemPlugin:\n"
                f"{len(self.get_commands())} path items in plugin\n"
            )
            if self.config_file_path:
                status_str += f"Config file: {self.config_file_path}"
            click.echo(status_str)

        @click.command()
        @click.argument("keyword")
        @click.argument("path")
        def add(keyword, path):
            """Add a new url pattern"""
            pattern = PathItem(name=keyword, path=path)
            click.echo(f"Adding {pattern}")
            self.item_list.append(pattern)
            self.save()

        @click.command()
        @click.argument("keyword")
        def remove(keyword):
            """Remove an existing path item"""
            to_remove = [x for x in self.item_list if x.name == keyword]
            if not to_remove:
                click.echo(f"path with keyword {keyword} not found")
            else:
                click.echo(f"Removing {[str(x) for x in to_remove]}")
                for x in to_remove:
                    self.item_list.remove(x)
                self.save()

        @click.command()
        def list():
            """list all paths"""
            click.echo("\n".join([str(x) for x in self.item_list]))

        return [status, list, add, remove]


def open_terminal(path):
    """Open a terminal at the given path.

    Parameters
    ----------
    path: Path
        The path to open terminal on
    """

    if platform.system() == "Linux":
        subprocess.Popen(args=["konsole", "-e", "bash", "-c", f"cd {path}; $SHELL"])
    else:
        raise NotImplemented(
            f"Opening new terminal not supported on platform '{platform.system()}'"
        )
