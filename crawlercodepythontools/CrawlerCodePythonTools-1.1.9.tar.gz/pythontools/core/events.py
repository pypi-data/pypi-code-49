from pythontools.core import logger

events = []

def registerEvent(trigger, event):
    events.append({"trigger": trigger, "event": event})

def unregisterEvent(event):
    for e in events:
        if e["event"] == event:
            events.remove(e)

def call(trigger, params=None):
    try:
        for event in events:
            if event["trigger"] == trigger:
                if params is None:
                    event["event"]()
                else:
                    event["event"](params)
    except Exception as e:
        logger.log("§cEvent '" + trigger + "' throw exception: " + str(e))