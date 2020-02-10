# -*- coding: utf-8 -*-

# src:https://github.com/miraclx/node_events

class EventListenerStack():
    def __init__(self,  event):
        self.__event = event
        self.__listeners = []

    def respond(self, *data):
        if self.hasListeners():
            for listener in self.listeners:
                listener.respond(*data)
            return True
        return False

    def verifyHasListener(self, fn):
        return bool(self.extractInstanceOf(fn))

    def attachListener(self, fn, index):
        if not self.verifyHasListener(fn):
            self.__listeners.insert(index, EventListener(fn))

    def detachListener(self, fn):
        listener = self.extractInstanceOf(fn)
        if (listener):
            self.__listeners.remove(listener)
            return True
        else:
            return False

    def detachAllListeners(self):
        for listener in self.listeners:
            self.detachListener(listener)

    def hasListeners(self):
        return bool(self.listenerCount)

    def extractInstanceOf(self, fn):
        result = None
        for listener in self.listeners:
            if listener.verify(fn):
                result = listener
        return result

    @property
    def listeners(self):
        return list(self.__listeners)

    @property
    def listenerCount(self):
        return len(self.listeners)


class EventListener():
    def __init__(self, listener):
        self._listener = listener
        self.__called_times = 0

    def respond(self, *data):
        self.__called_times += 1
        self._listener(*data)

    def verify(self, fn):
        return self._listener == fn

    @property
    def called_count(self):
        return self.__called_times


class EventEmitter:
    def __init__(self):
        self.__raw_listeners = {}

    def __onceWrap(self, event, listener):
        def wrapped_fn(*data):
            self.removeListener(event, wrapped_fn)
            listener(*data)
        return wrapped_fn

    def __addListener(self, event, listener, prepend):
        if not self.hasEvent(event):
            self.__listeners[event] = EventListenerStack(event)
        stack = self.getStackOf(event)
        stack.attachListener(listener, 0 if prepend else stack.listenerCount)
        self.emit('addlistener:'+event)
        return self

    def on(self, event, listener):
        return self.__addListener(event, listener, False)

    def prependListener(self, event, listener):
        return self.__addListener(event, listener, True)

    def once(self, event, listener):
        return self.__addListener(event, self.__onceWrap(event, listener), False)

    def prependOnceListener(self, event, listener):
        return self.__addListener(event, self.__onceWrap(event, listener), True)

    def emit(self, event, *data):
        return self.hasEvent(event) and self.getStackOf(event).respond(*data)

    def addListener(self,event, listener):
        return self.on(event, listener)

    def off(self, event, listener):
        return self.removeListener(event, listener)

    def removeListener(self, event, listener):
        if self.hasEvent(event, True):
            self.getStackOf(event).detachListener(listener)
            self.emit('rmlistener:'+event)
        return self

    def removeAllListeners(self, event=None):
        if type(event) is str:
            if self.hasEvent(event, True):
                self.getStackOf(event).detachAllListeners()
            del self.__listeners[event]
            self.emit('rmlistener:'+event)
        else:
            for event in self.__listeners:
                self.removeAllListeners(event)
        return self

    def hasEvent(self, event, raiseException=False):
        status = event in self.__listeners
        if not status and raiseException:
            raise Exception(
                "Event: %s doesn't exist within EventEmitter instance" % event)
        return status

    def hasListeners(self, event):
        return self.hasEvent(event) and self.getStackOf(event).hasListeners()

    def getStackOf(self, event):
        return self.__listeners[event] if self.hasEvent(event) else None

    @property
    def __listeners(self):
        return self.__raw_listeners