import asyncio
import importlib
import json
import os
import time
import traceback
from pathlib import Path

from .module import Module
from .event_handler import EventHandler
from .logger import Logger
from .typer import Typer


def get_sub_files(a_dir):
    """
    Get all files in a directory
    :param a_dir: Directory to search
    :return: List of files in directory
    """
    return [name for name in os.listdir(a_dir)
            if os.path.isfile(os.path.join(a_dir, name))]


def get_sub_fd(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isfile(os.path.join(a_dir, name)) or os.path.isdir(os.path.join(a_dir, name))]


class ModuleManager(object):
    """
    The ModuleManager handles the loading, enabling and reloading of modules and all events.
    """

    def __init__(self, bot, modules_dir=None):
        from .bot import Bot
        self.bot: Bot = bot
        self.logger = Logger()
        self.modules = {}
        self.loop: asyncio.BaseEventLoop = asyncio.get_event_loop()
        self.modules_dir = modules_dir
        if self.modules_dir is None:
            self.modules_dir = 'modules/'
        self.events = {
            'discord': {
                # 'on_ready': {},
                # 'on_shard_ready': {},
                'on_resumed': {},
                'on_error': {},
                'on_socket_raw_receive': {},
                'on_socket_raw_send': {},
                'on_typing': {},
                'on_message': {},
                'on_message_delete': {},
                'on_raw_message_delete': {},
                'on_raw_bulk_message_delete': {},
                'on_message_edit': {},
                'on_raw_message_edit': {},
                'on_reaction_add': {},
                'on_raw_reaction_add': {},
                'on_reaction_remove': {},
                'on_raw_reaction_remove': {},
                'on_reaction_clear': {},
                'on_raw_reaction_clear': {},
                'on_private_channel_delete': {},
                'on_private_channel_create': {},
                'on_private_channel_update': {},
                'on_private_channel_pins_update': {},
                'on_guild_channel_delete': {},
                'on_guild_channel_create': {},
                'on_guild_channel_update': {},
                'on_guild_channel_pins_update': {},
                'on_member_join': {},
                'on_member_remove': {},
                'on_member_update': {},
                'on_guild_join': {},
                'on_guild_remove': {},
                'on_guild_update': {},
                'on_guild_role_create': {},
                'on_guild_role_delete': {},
                'on_guild_role_update': {},
                'on_guild_emojis_update': {},
                'on_guild_available': {},
                'on_voice_state_update': {},
                'on_member_ban': {},
                'on_member_unban': {},
                'on_group_join': {},
                'on_group_remove': {},
                'on_relationship_add': {},
                'on_relationship_remove': {},
                'on_relationship_update': {},
            },
            'buildabot': {
                # Module Manager
                'on_ready': {},
                'on_done': {},
                'on_all_load': {},
                'on_load': {},
                'on_all_enabled': {},
                'on_enabled': {},
                'on_all_disabled': {},
                'on_disabled': {}
            }
        }

        for name in self.events['discord']:
            event_name = str(name)
            funcs = {}

            exec("""async def {0}(*args, **kwargs):
    await self.emit_event("discord", "{0}", *args, **kwargs)""".format(event_name), {'self': self}, funcs)

            self.bot.client.event(funcs[event_name])

        self.emit_event_sync('buildabot', 'on_ready')
        self.logger.info("Loading modules...")

        self.load_all_modules()

    async def emit_event(self, namespace, event_name, *args, **kwargs):
        """
        Call an event
        :param event_name: Name of the event, it must be already defined
        :param args: Arguments to be sent to the event
        :param kwargs: Named arguments to be sent to the event
        :return: true if canceled
        """
        if namespace not in self.events:
            return True
        if event_name not in self.events[namespace]:
            return True

        canceled = False
        handler: EventHandler = None

        prioritys = sorted(self.events[namespace][event_name])
        prioritys.reverse()

        for priority in prioritys:
            for handler in self.events[namespace][event_name][priority]:
                if canceled and not handler.ignore_canceled:
                    continue

                try:
                    rtn = await handler.call(*args, **kwargs)

                    if not rtn and rtn is not None:
                        canceled = True
                        break
                except:
                    self.logger.error(
                        'Error emitting event "{}" to module "{}":'.format(event_name, handler.module.meta['class']))
                    self.logger.error(traceback.format_exc())

        return not canceled

    def load_all_modules(self):
        """
        Load every available module
        :return: None
        """
        modules_dir = self.modules_dir
        for module_file in get_sub_fd(modules_dir):
            try:
                if module_file.endswith(".py"):
                    module_file = module_file[:len(module_file) - 3]
                f = self.load_module(module_file)
                if not f:
                    self.logger.error('Invalid module', module_file)
            except Exception as e:
                self.logger.error('Failed to load module', module_file)
                self.logger.error(traceback.format_exc())
        self.emit_event_sync('buildabot', 'on_all_load')

    def load_module(self, name):
        """
        Load a module. Each module is automatically loaded when `load_all_modules` is called.
        :param name: Name of the module
        :return: The module
        """
        name = str(name).lower()
        modules_dir = self.modules_dir

        template = {
            'main': 'str',
            'class*': 'str',
            'name*': 'str',
            'description*': 'str',
            'disable': 'bool',
            'threaded': 'bool',
            'depends': 'str[]',
            'softdepends': 'str[]'
        }

        package = "modules"
        if Path("{}/{}.py".format(modules_dir, name)).is_file():
            module = getattr(__import__(package, fromlist=[name]), name)
            meta = module.meta

            Typer.verify_dict(template, meta)
        elif Path("{}/{}".format(modules_dir, name)).is_dir():
            module_meta_file = Path(
                "{}/{}/module.json".format(modules_dir, name))
            if not module_meta_file.is_file():
                return False
            meta = json.load(module_meta_file.open(mode='r'))

            Typer.verify_dict(template, meta)

            split: list = meta['class'].split('.')
            main = split[-1]
            package = '{}.{}.{}'.format(
                package, name, '.'.join(split[0:-1])).strip('.')
            module = __import__(package, fromlist=[main])
        else:
            return False

        importlib.reload(module)

        module: Modules = getattr(
            module, meta['class'].split('.')[-1])(self, meta)
        module.logger.info('Loaded')
        self.modules[meta['name']] = module
        if meta['name'] in self.bot.config['modules']:
            module.config = self.bot.config['modules'][meta['name']]
        module.on_load()
        self.emit_event_sync('buildabot', 'on_load', module)
        return module

    def get_module(self, name):
        """
        Get a module
        :param name: Name of the module
        :return: The module object
        """
        if name not in self.modules:
            return None
        return self.modules[name]

    async def enable_all_modules(self):
        """
        Attempts to enable all modules. This is automatically called when the bot is ready
        :return:
        """
        self.logger.info("Enabling modules...")
        skiped = []
        last_len = 0
        start_time = int(round(time.time() * 1000))

        async def enable(module_name, force=False):
            try:
                module = self.modules[module_name]
                if not force:
                    if 'depends' in module.meta:
                        for d in module.meta['depends']:
                            if not self.is_enabled(d):
                                if not module_name in skiped:
                                    skiped.append(module_name)
                                return False
                    if 'softdepends' in module.meta:
                        for d in module.meta['softdepends']:
                            if not self.is_enabled(d):
                                if not module_name in skiped:
                                    skiped.append(module_name)
                                return False

                if module.is_enabled():
                    module.logger.info("Already enabled")
                    if module_name in skiped:
                        skiped.remove(module_name)
                    return True

                if module_name in skiped:
                    skiped.remove(module_name)

                await module.enable()
            except Exception:
                self.logger.error('Failed to enable', module_name)
                self.logger.error(traceback.format_exc())

            return True

        for fn in self.modules:
            await enable(fn)

        while last_len != len(skiped):
            last_len = len(skiped)
            for fn in skiped:
                await enable(fn)

        for fn in skiped:
            module = self.modules[fn]
            missing = []
            if 'depends' in module.meta:
                for d in module.meta['depends']:
                    if not self.is_enabled(d):
                        missing.append(d)

            if len(missing) > 0:
                module.logger.error('Failed to enable')
                module.logger.error(
                    'Missing one or more dependencies: {}'.format(', '.join(missing)))
            else:
                await enable(fn, force=True)
        took = int(round(time.time() * 1000)) - start_time
        self.logger.info('Done! ({}ms)'.format(took))
        await self.emit_event('buildabot', 'on_all_enabled')

    def can_disable(self, module):
        """
        Checks to see if a module is able to be disabled.
        This commonly occurs if the module is already disabled or has enabled "threaded" in its meta.
        :param module: The module object
        :return:
        """
        if not module.is_enabled():
            return False
        if 'threaded' in module.meta:
            if module.meta['threaded']:
                return False
        return True

    def is_enabled(self, name):
        """
        Check if a module is enabled
        :param name: Name of the module
        :return: True if the named module is enabled
        """
        module: Module = self.get_module(name)
        if module is None:
            return False
        return module.is_enabled()

    async def disable_all_modules(self):
        """
        Disable all modules
        :return: None
        """
        for module_name in self.modules:
            module = self.modules[module_name]

            if not module.is_enabled():
                continue
            if not self.can_disable(module):
                module.logger.info("Can't disable")
                continue

            module.unregister_all_events()
            await module.disable()

    async def reload_all_modules(self):
        """
        Attempts to disable, reload and re-enable all modules
        :return: None
        """
        self.logger.info("Disabling modules...")

        await self.disable_all_modules()

        self.logger.info("Reloading modules...")

        to_load = []

        for module_name in list(self.modules):
            module = self.modules[module_name]

            if module.is_enabled():
                continue

            del self.modules[module_name]
            to_load.append(module_name)

        for module_name in to_load:
            self.load_module(module_name)

        await self.enable_all_modules()

    def on_event(self, module, event_name, func, namespace='discord', priority=0, ignore_canceled=False):
        """
        Add an event handler
        :param module: The module associated with the handler
        :param event_name: Name of the event
        :param func: function to be called
        :param priority: Priority of event, higher numbers will be called first
        :param ignore_canceled: Ignore the event if it is canceled before the listener can be called
        :return: The event handler
        """
        if namespace not in self.events:
            self.events[namespace] = {}
        if event_name not in self.events[namespace]:
            self.events[namespace][event_name] = {}
        if priority not in self.events[namespace][event_name]:
            self.events[namespace][event_name][priority] = []

        handler = EventHandler(module, namespace, event_name, func, priority, ignore_canceled)
        self.events[namespace][event_name][priority].append(handler)
        return handler

    def event(self, event_name, namespace='discord', priority=0, ignore_canceled=False):
        """
        Add an event handler
        :param event: Name of the event
        :param priority: Priority of event, higher numbers will be called first
        :param ignore_canceled: Ignore the event if it is canceled before the listener can be called
        :return: The event handler
        """

        def add(func):
            self.on_event(event_name, func, priority=priority,
                          ignore_canceled=ignore_canceled, namespace=namespace)

        return add

    def emit_event_sync(self, namespace, event_name, *args, **kwargs):
        """
        Call an event in sync
        :param event_name: Name of the event, it must be already defined
        :param args: Arguments to be sent to the event
        :param kwargs: Named arguments to be sent to the event
        :return: true if canceled
        """
        caller = self.emit_event(namespace, event_name, *args, **kwargs)

        return self.loop.create_task(caller)
