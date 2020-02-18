from .generics import CrudEntity


class Contact(CrudEntity):
    def inspect_endpoint(self, **kwargs):
        self.endpoint = '/api/contacts/'
        id_ = kwargs.pop('id', None)
        if id_:
            self.endpoint = '/api/contacts/' + str(id_) + '/'

    def bulk_delete(self, **kwargs):
        self.endpoint = '/api/contacts/bulk-delete/'
        kwargs.update({'skip_inspect': True})
        return super(Contact, self).create(url_params=None, **kwargs)

    def import_contacts(self, **kwargs):
        self.endpoint = '/api/contacts/import_from_file/'
        kwargs.update({'skip_inspect': True})
        return super(Contact, self).create(url_params=None, **kwargs)


class ContactGroup(CrudEntity):
    def inspect_endpoint(self, **kwargs):
        self.endpoint = '/api/contacts/groups/'
        id_ = kwargs.pop('id', None)
        if id_:
            self.endpoint = '/api/contacts/groups/' + str(id_) + '/'
