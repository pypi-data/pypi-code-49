from pythontools.core import logger

events = []

def registerEvent(trigger, event, scope="global"):
    events.append({"trigger": trigger, "event": event, "scope": scope})

def unregisterEvent(event):
    for e in events:
        if e["event"] == event:
            events.remove(e)

def call(trigger, params=None, scope="global"):
    try:
        for event in events:
            if event["trigger"] == trigger and event["scope"] == scope:
                if params is None:
                    event["event"]()
                else:
                    event["event"](params)
    except Exception as e:
        logger.log("§cEvent '" + trigger + "' throw exception: " + str(e))