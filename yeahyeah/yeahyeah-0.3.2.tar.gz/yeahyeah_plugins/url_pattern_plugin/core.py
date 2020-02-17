import re
import webbrowser

import click

from yeahyeah.core import YeahYeahPlugin
from yeahyeah.context import YeahYeahContext
from yeahyeah.objects import SerialisableMenuItem, MenuItemList


default_settings_file_name = "url_patterns.yaml"


class UrlPattern(SerialisableMenuItem):
    """A named url pattern that launches some url and can be saved to disk"""

    def __init__(self, name, pattern, help_text=None):
        super().__init__(name, help_text)
        self.pattern = pattern

    def __str__(self):
        return f"URLPattern {self.name}:{self.pattern}"

    def get_parameters(self):
        return {"pattern": self.pattern}

    @property
    def help_text(self):
        if self._help_text is None:
            return f"launch {self.name}"
        else:
            return self._help_text

    def render(self, args_tuple):
        """Render this url pattern with the given args

        Parameters
        ----------
        args_tuple: Tuple
            tuple of all arguments

        Returns
        -------
        str

        """
        return self.pattern.format(*args_tuple)

    def to_click_command(self):
        """This url pattern as a click command that can be added with add_command()
        """

        arguments = re.findall(r"\{([^{}]*)\}", self.pattern)

        @click.command(name=self.name, help=self.help_text)
        def the_command(**kwargs):
            url = self.pattern.format(**kwargs)
            click.echo(url)
            click.launch(url)

        for argument_name in arguments:
            the_command = click.argument(argument_name, type=click.STRING)(the_command)

        return the_command


class WildCardUrlPattern(UrlPattern):
    def __init__(self, name, pattern, capture_all_keywords=True, help_text=None):
        super().__init__(name, pattern, help_text)

    def get_parameters(self):
        parameters = super().get_parameters()
        parameters["capture_all_keywords"] = True
        return parameters

    def to_click_command(self):
        """This url pattern as a click command that can be added with add_command()
        """

        arguments = re.findall(r"\{([^{}]*)\}", self.pattern)

        @click.command(name=self.name, help=self.help_text)
        def the_command(**kwargs):

            if kwargs:
                param_name, param_values = list(kwargs.items()).pop()
                url = self.pattern.format(**{param_name: " ".join(param_values)})
            else:
                url = self.pattern
            click.echo(f"loading {url}")
            open_url(url)

        for argument_name in arguments:
            the_command = click.argument(argument_name, type=click.STRING, nargs=-1)(
                the_command
            )

        return the_command


class URLPatternList(MenuItemList):
    """A persistable list of url patterns.

    For human readable saving and loading"""

    item_classes = [WildCardUrlPattern, UrlPattern]


def open_url(url):
    """Open a browser with the given url

    Parameters
    ----------
    url: str

    Returns
    -------
    None

    """
    webbrowser.open_new(url)


class UrlPatternsPlugin(YeahYeahPlugin):

    slug = "url_patterns"
    short_slug = "url"

    def __init__(self, pattern_list):
        """Plugin that holds URL path_items

        Parameters
        ----------
        pattern_list: URLPatternList

        """
        self.pattern_list = pattern_list
        self.config_file_path = None

    @classmethod
    def init_from_context(cls, context: YeahYeahContext):
        settings_file_path = context.settings_path / default_settings_file_name
        cls.assert_config_file(settings_file_path)
        with open(settings_file_path, "r") as f:
            pattern_list = URLPatternList.load(f)

        obj = cls(pattern_list=pattern_list)
        obj.config_file_path = settings_file_path
        return obj

    @classmethod
    def __from_file_path__(cls, config_file_path):
        cls.assert_config_file(config_file_path)
        with open(config_file_path, "r") as f:
            pattern_list = URLPatternList.load(f)

        obj = cls(pattern_list=pattern_list)
        obj.config_file_path = config_file_path
        return obj

    def save(self):
        """Save current pattern list to disk if possible"""
        if self.config_file_path:
            with open(self.config_file_path, "w") as f:
                self.pattern_list.save(file=f)

    @staticmethod
    def assert_config_file(config_file_path):
        """Make sure config file exists. If not, create an example config file"""
        if config_file_path.exists():
            return
        else:
            config_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(config_file_path, "w") as f:
                example_patterns = [
                    UrlPattern(
                        name="virus",
                        pattern="https://www.virustotal.com",
                        help_text="Launch online virus scanner",
                    ),
                    UrlPattern(
                        name="wiki",
                        pattern="https://en.wikipedia.org/wiki/{article_slug}",
                        help_text="Launch given mediawiki article in English",
                    ),
                    WildCardUrlPattern(
                        name="search", pattern="https://duckduckgo.com/?q={query}"
                    ),
                ]
                URLPatternList(items=example_patterns).save(f)
            click.echo(
                f"UrlPattern config file {config_file_path} did not exist. Creating "
                f"with default contents.."
            )

    def get_commands(self):
        """

        Returns
        -------
        List[click.Command]
        """
        commands = []
        for item in self.pattern_list.data:
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
                f"UrlPatternsPlugin:\n"
                f"{len(self.get_commands())} path_items in plugin\n"
            )
            if self.config_file_path:
                status_str += f"Config file: {self.config_file_path}"
            click.echo(status_str)

        @click.command()
        @click.argument("keyword")
        @click.argument("pattern")
        def add(keyword, pattern):
            """Add a new url pattern"""
            pattern = UrlPattern(name=keyword, pattern=pattern)
            click.echo(f"Adding {pattern}")
            self.pattern_list.append(pattern)
            self.save()

        @click.command()
        @click.argument("keyword")
        def remove(keyword):
            """Remove an existing url pattern"""
            to_remove = [x for x in self.pattern_list if x.name == keyword]
            if not to_remove:
                click.echo(f"Pattern with keyword {keyword} not found")
            else:
                click.echo(f"Removing {[str(x) for x in to_remove]}")
                for x in to_remove:
                    self.pattern_list.remove(x)
                self.save()

        @click.command()
        def list():
            """list all url path_items"""
            click.echo("\n".join([str(x) for x in self.pattern_list]))

        return [status, list, add, remove]
