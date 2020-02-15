import logging
from .types import PubSubError, acceptable, apply_ref


log = logging.getLogger("beercraft.event")


class EventError(PubSubError):
    def __init__(self, handler, ex):
        super(EventError, self).__init__(ex)
        self.handler = handler
        self.ex = ex

    def __str__(self):
        return "EventError: {0}".format(self.ex)


class EventErrorHandler:
    def __init__(self):
        self.halt_current = True
        self.halt_parent = True
        self._handler = self._raise

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, value):
        self._handler = value

    def _raise(self, exception):
        raise EventError(self, exception)

    def handle_error(self, exception):
        self._handler(exception)


class Event:
    def __init__(self, eid):
        self.eid = eid
        self._notify_list = []
        self._clean = False
        self._errors = EventErrorHandler()

    @property
    def halt_on_error(self):
        return self._errors.halt_current

    @halt_on_error.setter
    def halt_on_error(self, value):
        self._errors.halt_current = value

    def set_error_handler(self, handler):
        self._errors.handler = handler

    def _iter_ref(self):
        """Return the WeakMethod object.
        """
        for listener_ref in self._notify_list:
            yield listener_ref

    def _iter_callables(self):
        """Return the call to WeakMethod object.
        Gives the referenced object.
        """
        for listener_ref in self._notify_list:
            yield listener_ref()

    def register(self, listener):
        """ register function!
        """
        if not acceptable(listener):
            msg = "{} is not a valid beercraft pub subscriber!"
            raise PubSubError(msg.format(str(listener)))
        lref = apply_ref(listener)
        self._notify_list.append(lref)

    def unregister(self, listener):
        """ unregister fuction!
        """
        references = self._iter_ref()
        for listener_ref in references:
            if listener_ref() == listener:
                self._notify_list.remove(listener_ref)
                references.close()

    def notify(self, *args, **kwargs):
        """ Call all listeners.
        """
        callables = self._iter_callables()
        for listener_obj in callables:
            log.debug("calling {0}".format(listener_obj))
            if listener_obj:
                try:
                    listener_obj(*args, **kwargs)
                except Exception as ex:  # pylint: disable=broad-except
                    try:
                        self._errors.handle_error(ex)
                    finally:
                        if self._errors.halt_current:
                            callables.close()
                            raise EventError(self._errors, ex)
            else:
                self._clean = True

        self._cleanup()

    def _cleanup(self):
        """remove any null references.
        """
        self._notify_list = [c for c in self._notify_list if c() is not None]

    def clear(self):
        """remove all listners.
        """
        self._notify_list = []

    def __contains__(self, other):
        callables = self._iter_callables()
        contains = False
        for obj in callables:
            if obj == other:
                callables.close()
                contains = True
        return contains

    def __call__(self, *args, **kwargs):
        self.notify(*args, **kwargs)

    def __iadd__(self, listener):
        self.register(listener)
        return self

    def __isub__(self, listener):
        self.unregister(listener)
        return self
