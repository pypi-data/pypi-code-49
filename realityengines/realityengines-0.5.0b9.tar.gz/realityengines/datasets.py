$CLASS_IMPORTS


class Datasets():
    '''

    '''

    def __init__(self, client, ):
        self.client = client
        self.id = None

    def __repr__(self):
        return f"Datasets()"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {}

    def refresh(self):
        self = self.describe()
        return self
