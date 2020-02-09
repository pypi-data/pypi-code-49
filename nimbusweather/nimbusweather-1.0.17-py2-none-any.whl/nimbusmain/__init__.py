#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

CMD_ERROR = 2
IO_ERROR = 4


class BreakLoop(Exception):
    pass


class STARTUP(object):
    pass


class PRE_LOOP(object):
    pass


class NEW_LOOP_PACKET(object):
    pass


class Event(object):
    """Represents an event."""

    def __init__(self, event_type, **argv):
        self.event_type = event_type

        for key in argv:
            setattr(self, key, argv[key])

    def __str__(self):
        """Return a string with a reasonable representation of the event."""
        et = "Event type: %s | " % self.event_type
        s = "; ".join("%s: %s" % (k, self.__dict__[k]) for k in self.__dict__ if k != "event_type")
        return et + s
