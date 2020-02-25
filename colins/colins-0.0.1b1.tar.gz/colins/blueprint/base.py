class BaseBlueprint:
    pass


class BlueprintItem:
    pass


class Task(BlueprintItem):
    def __init__(self, name, url, params=None, page_info=None, fields=None):
        self.name = name
        self.url = url
        self.params = params or dict()
        self.page_info = page_info or None
        self.fields = dict()
        if fields:
            self.set_fields(fields)

    def set_fields(self, fields):
        if fields is None:
            self.fields = dict()
        else:
            pass

    def get_name(self):
        return self.name

    def get_page_info(self):
        return self.page_info

    def get_params(self):
        return self.params

    def get_url(self):
        return self.url

    def get_fields(self):
        return self.fields


class Field(BlueprintItem):
    ALLOWED_FIELD_TYPE = ['str', 'int', 'datetime']

    def __init__(self, name, selector, type='str', attr=None, exclude=None, required=False):
        self.name = name
        self.selector = selector
        self.type = type
        self.attr = attr
        self.exclude = exclude or []
        self.required = required
