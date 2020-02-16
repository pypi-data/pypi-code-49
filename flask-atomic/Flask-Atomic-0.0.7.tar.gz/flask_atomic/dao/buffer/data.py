class DataBuffer:

    def __init__(self, data, schema, rels=False, exclusions=None):
        self.object = True
        self.showrefs(rels)
        if isinstance(data, list):
            self.object = False
        self.schema = schema
        self.data = data
        self.exclusions = exclusions or list()
        self.include = list(map(lambda sch: sch.get('key'), self.schema))

    def schema(self):
        return self.schema

    def name(self):
        return str(self.data)

    def showrefs(self, value=True):
        """
        Set the model references value. References are backref and relationships on Alchemy model instances
        :param value: boolean True / False
        :return: self
        :rtype: DataBuffer
        """

        self.relationships = value
        return self

    def prepare(self, instance, exclude):
        if not exclude:
            exclude = []
        if isinstance(instance, tuple):
            return instance[0].serialize(
                rel=self.relationships,
                exc=exclude
            )
        return instance.serialize(
            rel=self.relationships,
            exc=exclude
        )

    def json(self, exclude=None, relations=None):
        if not exclude:
            exclude = list()
        elif exclude and not hasattr(exclude, '__iter__'):
            raise ValueError('Cannot use exclusions that are not in a collection')

        exclude = exclude + [self.exclusions]
        if relations is not None:
            self.relationships = relations

        if self.data is None:
            return list()

        if self.object:
            return self.prepare(self.data, exclude)
        return [self.prepare(entry, exclude) for entry in self.data]

    def view(self):
        return self.data

    def __iter__(self):
        return iter(self.data)
