class ItemStorage(object):

    def __init__(self, identifier, item, last_save):
        self.identifier = identifier
        self.item = item
        self.is_modified = False
        self.last_save = last_save
