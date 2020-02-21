from os.path import join


class Resource:

    path = None

    def __init__(self, parent=None, path=None):
        self.session = parent.session
        self.parent = parent
        self.url = self.parent.url
        if path is None:
            path = self.path
        if path is not None:
            self.url = join(self.url, str(path))

    def get(self, **kwargs):
        return self.session.get(self.url, **kwargs).json()


class Deletable:

    def delete(self, key):
        self.session.delete(join(self.url, str(key)))


class Mutable:

    def create_or_update(self, key, **kwargs):
        if key is None:
            return self.session.post(self.url, **kwargs).json()
        else:
            return self.session.put(join(self.url, str(key)), **kwargs)

    def create(self, **kwargs):
        return self.create_or_update(None, **kwargs)

    def update(self, key, **kwargs):
        return self.create_or_update(key, **kwargs)


class Mapping:

    def __getitem__(self, key):
        return self.mapped_class(self, key)
