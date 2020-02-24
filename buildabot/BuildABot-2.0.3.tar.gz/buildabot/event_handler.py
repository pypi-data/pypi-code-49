import asyncio


class EventHandler(object):

    def __init__(self, module, namespace, event_name, func, priority, ignore_canceled):
        from .module import Module
        self.module: Module = module
        self.namespace: str = namespace
        self.event_name: str = event_name
        self.full_name = f"{self.namespace}:{self.event_name}"
        self.func: asyncio.coroutine = func
        self.priority: int = priority
        self.ignore_canceled: bool = ignore_canceled
        self.registered = True

    def unregister(self, events):
        """
        Unregister this event from a list of events
        :param events: List of events
        :return: None
        """
        event_copy = dict(events)
        for full_name in event_copy:
            prioritys = events[full_name]
            for priority_index in prioritys:
                priority = prioritys[priority_index]
                for handler in priority:
                    if self == handler:
                        events[full_name][priority_index].remove(handler)
        self.registered = False
        self.func = None

    async def call(self, *args, **kwargs):
        """
        Call the listener
        :param args: Args to be passed to the listener
        :param kwargs: Named args to be passed to the listener
        :return:
        """
        if not self.registered:
            return True
        if self.func:
            return await self.func(*args, **kwargs)
