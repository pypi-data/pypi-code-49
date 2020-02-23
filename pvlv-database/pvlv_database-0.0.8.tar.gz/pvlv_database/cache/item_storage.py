from time import time


class ItemStorage(object):

    def __init__(self, identifier, item):
        self.identifier = identifier
        self.item = item
        self.is_modified = True
        self.last_save = time()

    def __str__(self):
        return 'Identifier: {}\nIs modified: {}\nLast save: {}'.format(
            self.identifier,
            self.is_modified,
            self.last_save,
        )
