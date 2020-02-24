class Module(object):
    """
    A module is, well, a module. Modules loaded when the program is loaded and enabled when the bot is ready
    """

    def __init__(self, module_manager, meta: dict):
        from buildabot import Bot, ModuleManager, Logger
        self.module_manager: ModuleManager = module_manager
        self.bot: Bot = module_manager.bot
        self.meta: dict = meta
        self._enabled = False
        self.logger = Logger(module=self)
        self.events = []
        self.config = {}

    async def enable(self):
        """
        Attempt to enable the module
        """
        if 'disable' in self.meta:
            if self.meta['disable']:
                return
        if self.is_enabled():
            return
        await self.on_enable()
        self.logger.info('Enabled')
        self._enabled = True
        await self.module_manager.emit_event('buildabot', 'on_enabled', self)

    async def disable(self):
        """
        Attempt to disable the module
        :return:
        """
        if not self.is_enabled():
            return
        if 'threaded' in self.meta:
            if self.meta['threaded']:
                return
        await self.on_disable()
        self.logger.info('Disabled')
        self._enabled = False
        await self.module_manager.emit_event('buildabot', 'on_disabled', self)

    def is_enabled(self):
        """
        Get weather the module is enabled
        :return: boolean
        """
        return self._enabled

    def on_event(self, event, func, priority=0, namespace='discord', ignore_canceled=False):
        """
        Add an event handler
        :param event: Name of the event
        :param func: Function to be called when the event is called
        :param priority: Priority of event, higher numbers will be called first
        :param ignore_canceled: Ignore the event if it is canceled before the listener can be called
        :return: The event handler
        """
        event = self.module_manager.on_event(self, event, func, namespace=namespace, priority=priority, ignore_canceled=ignore_canceled)
        self.events.append(event)
        return event

    def unregister_all_events(self):
        """
        Unregister all events associated with this module. This is called when the module is disabled.
        :return:
        """
        for event in self.events:
            event.unregister(self.module_manager.events)
        self.events = []

    # defaults
    def on_load(self):
        """
        Called when the module is loaded

        Note: Do not attempt to get other modules in this method as they might not be loaded
        """
        pass

    async def on_enable(self):
        """
        Called when the module is enabled
        """
        pass

    async def on_disable(self):
        """
        Called when the module is disabled
        """
        pass
