from .generics import CrudEntity


class Template(CrudEntity):
    def inspect_endpoint(self, **kwargs):
        self.endpoint = '/api/marketing/emailtemplates/'
        id_ = kwargs.pop('id', None)
        if id_:
            self.endpoint = '/api/marketing/emailtemplates/' + str(id_) + '/'
