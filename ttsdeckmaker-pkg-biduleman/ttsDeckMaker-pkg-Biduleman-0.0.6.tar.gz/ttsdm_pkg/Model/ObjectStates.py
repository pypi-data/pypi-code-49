import json


class ObjectStates:
    def __init__(self):
        self.objectStates = []

    def __len__(self):
        return len(self.objectStates)

    def add_object_state(self, object_state):
        self.objectStates.append(object_state)

    def get_json(self):
        return json.dumps(self.objectStates)

    def get_dict(self):
        return self.objectStates
