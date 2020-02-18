import json


def dumps(to_dump):
    def dump(obj):
        return obj.__dict__

    return json.dumps(to_dump, indent=4, default=dump, ensure_ascii=False)


class AtomicCounter:
    def __init__(self):
        self.counter = 0

    def count(self):
        self.counter += 1
        return self.counter
