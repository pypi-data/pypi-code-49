import importlib
from pathlib import Path

import click

from yeahyeah.context import YeahYeahContext
from yeahyeah.decorators import pass_yeahyeah_context
from yeahyeah.exceptions import YeahYeahException
from yeahyeah.persistence import JSONSettingsFile


class YeahYeah:
    """A bare-bones launch manager. Plugins can be added to add launchable items
    """

    def __init__(self, configuration_path):
        """

        Parameters
        ----------
        configuration_path: Pathlike
            Path to a location where yeahyeah can read and write settings
        """
        self.configuration_path = configuration_path
        self.settings_file_path = configuration_path / 'yeahyeah_settings.json'
        self.plugins = []

        self.root_cli = self.get_root_cli()
        self.admin_cli = self.get_admin_group()
        self.root_cli.add_command(self.admin_cli)

        self.context = YeahYeahContext(settings_path=self.configuration_path)

    def add_plugin_instance(self, plugin):
        """Add this plugin to yeahyeah

        This will add all its actions to root_cli directly and all admin actions to
        root_cli/admin

        Notes
        -----
        Because all actions are added to root_cli directly, actions from different
        yeahyeah_plugins can overwrite each other. YeahYeah does not check this.
        New actions will overwrite old actions.

        Parameters
        ----------
        plugin: yeahyeah.core.YeahYeahPlugin
            Plugin instance to add

        """
        self.plugins.append(plugin)
        for command in plugin.get_commands():
            self.root_cli.add_command(command)

        @click.group(name=plugin.slug, help=f"Admin for {plugin.slug}")
        @click.pass_context
        def plugin_admin(ctx):
            f"""Admin for {plugin.slug}"""
            ctx.obj = self.context

        for command in plugin.get_admin_commands():
            plugin_admin.add_command(command)
        self.admin_cli.add_command(plugin_admin)

    def add_plugin(self, plugin):
        """Create an instance of this class and add to yeahyeah. Hides some
        details over add_plugin_instance

        Parameters
        ----------
        plugin: YeahYeahPlugin class or string
            Plugin class to add. If string, will try to import class, if class, will
            import that class directly

        Raises
        ------
        ModuleNotFoundError
            When given import path does not exist
        AttributeError:
            When given plugin does not fulfill the YeahYeahPlugin signature
        YeahYeahPluginImportException
            When plugin is neither a string nor a type

        """
        if type(plugin) == str:
            self.add_plugin_by_path(class_import_path=plugin)
        elif type(plugin) == type:
            self.add_plugin_class(plugin_class=plugin)
        else:
            msg = f"Cannot add {plugin}. This does not seems to be a class import" \
                  f" path or a class"
            raise YeahYeahPluginImportException(msg)

    def add_plugin_class(self, plugin_class):
        """Create an instance of this class and add to yeahyeah. Hides some
        details over add_plugin_instance

        Parameters
        ----------
        plugin_class: class extending yeahyeah.core.YeahYeahPlugin
            Plugin class to add
        """
        self.add_plugin_instance(plugin_class.init_from_context(context=self.context))

    def add_plugin_by_path(self, class_import_path):
        """Add a plugin by giving the python object import path

        Parameters
        ----------
        class_import_path: str
            Full import path to a YeahYeahPlugin class. For example
            'myplugin.core.YeahYeahPluginClass'

        Returns
        -------
        class:
            loaded from class_import path

        """
        module, classname = class_import_path.rsplit('.', 1)
        class_def = getattr(importlib.import_module(module), classname)
        self.add_plugin_class(class_def)

    def get_root_cli(self):
        """Create yeahyeah root group

        """

        @click.group()
        @click.pass_context
        def root_cli(ctx):
            """Yeahyeah launch things
            """

            ctx.obj = self.context
            return root_cli

        return root_cli

    def get_admin_group(self):
        @click.group(name="admin")
        def admin_group():
            """Admin options for yeahyeah and yeahyeah_plugins"""
            pass

        @click.group(name="yeahyeah")
        def yeahyeah_group():
            """Admin options for yeahyeah itself"""
            pass

        admin_group.add_command(yeahyeah_group)
        yeahyeah_group.add_command(self.enable_autocompletion)
        yeahyeah_group.add_command(self.get_status_command())
        yeahyeah_group.add_command(self.get_edit_plugins_command())

        return admin_group

    def get_status_command(self):
        """Create the command to show this yeahyeah instance's status.

        Notes
        -----
        like main(), status command also gets this slightly smelly access to self.
        This makes it possible for the command to inspect all installed
        yeahyeah_plugins etc.
        """

        @click.command()
        @pass_yeahyeah_context
        def status(ctx: YeahYeahContext):
            """Configuration and status"""
            click.echo("YeahYeah launch status:")
            click.echo(f"settings folder: '{self.configuration_path}'")
            click.echo(
                f"{len(self.plugins)} yeahyeah_plugins activated: [{', '.join([x.slug for x in self.plugins])}]"
            )
            click.echo(f"{len(self.root_cli.commands)} commands in main menu")

        return status

    def get_edit_plugins_command(self):
        """Open the plugins file in default editor
        """

        @click.command()
        def edit_plugins():
            """Configuration and status"""
            click.launch(str(self.settings_file_path))

        return edit_plugins

    @staticmethod
    @click.command()
    def enable_autocompletion():
        """Instructions to enable auto-completion"""
        click.echo(
            "Execute the following line in a terminal to enable auto-completion for that terminal only:\n"
            "\n"
            '    $ eval "$(_JJ_COMPLETE=source jj)"\n'
            "\n"
            "To enable auto completion permanently, run this\n"
            "\n"
            "    $ echo 'eval \"$(_JJ_COMPLETE=source jj)\"' >> ~/.bashrc\n"
        )

    def get_settings(self):
        """Get settings from expected location. Create default settings if not found

        Returns
        -------
        YeahYeahSettings
            Settings loaded from expected disk location, or default settings
        """

        return assert_yeahyeah_settings(self.settings_file_path)


class YeahYeahPlugin:
    """Some named thing that adds launchable commands to yeahyeah"""

    slug = (
        "BasePlugin"
    )  # Short, no space name to use for describing this plugin
    short_slug = (
        "Base"
    )  # Shorter slug, for help text. For example 'url', or 'path'

    @classmethod
    def init_from_context(cls, context: YeahYeahContext):
        """Initialise this plugin from a yeahyeah context object only

        Parameters
        ----------
        context: YeahYeahContext
            Context of the root yeahyeah module
        """
        return cls()

    def __str__(self):
        return f"YeahYeah plugin '{self.slug}'"

    def get_commands(self):
        """All Commands for this plugin

        Returns
        -------
        List[click.Command]
            All click commands that can be executed as part of this plugin
        """
        raise NotImplementedError()

    def get_admin_commands(self):
        """Action to do admin tasks for this plugin, if any

        Returns
        -------
        List[click.Command]
            List of click commands that can be used to admin this plugin

        """
        raise NotImplementedError()


class YeahYeahSettings:
    """Settings for the core yeahyeah module"""

    def __init__(self, plugin_paths):
        self.plugin_paths = plugin_paths

    def to_dict(self):
        return self.plugin_paths

    @classmethod
    def from_dict(cls, dict_in):
        return cls(plugin_paths=dict_in)


DEFAULT_YEAHYEAH_SETTINGS = \
    YeahYeahSettings(["yeahyeah_plugins.url_pattern_plugin.core.UrlPatternsPlugin"])


def assert_yeahyeah_settings(path):
    """Either read settings at path, or put default settings there

    Returns
    -------
    YeahYeahSettings
    """
    settings_file = YeahYeahSettingsFile(path)
    if settings_file.exists():
        return settings_file.load_settings()
    else:
        settings_file.save_settings(DEFAULT_YEAHYEAH_SETTINGS)
        return DEFAULT_YEAHYEAH_SETTINGS


class YeahYeahSettingsFile(JSONSettingsFile):
    """A file that can load and save YeahYeahSettings"""

    def load_settings(self):
        """Load settings from this file

        Returns
        -------
        YeahYeahSettings
            The loaded settings

        Raises
        ------
        FileNotFoundError
            If the file does not exist
        YeahYeahPersistenceException
            If file exists but cannot be parsed

        """
        return YeahYeahSettings.from_dict(self.load())

    def save_settings(self, settings):
        """

        Parameters
        ----------
        settings: YeahYeahSettings

        """
        self.save(settings.to_dict())

    def exists(self):
        """True if this file exists on disk"""
        return Path(self.path).exists()


class YeahYeahPluginImportException(YeahYeahException):
    pass
