from .exceptions import ParameterIncompleteException
from .generics import CrudEntity


class Numbers(CrudEntity):
    def list(self, url_params=None, **kwargs):
        self.endpoint = '/api/marketing/phone-numbers/'
        return super(Numbers, self).list(url_params, **kwargs)

    def available(self, url_params=None, **kwargs):
        self.endpoint = '/api/marketing/check_phone_numbers/'
        return super(Numbers, self).create(url_params=url_params, **kwargs)

    def buy(self, **kwargs):
        self.endpoint = '/api/marketing/buy_phone_numbers/'
        return super(Numbers, self).create(**kwargs)

    def retrieve(self, **kwargs):
        id_ = kwargs.pop('id', None)
        if not id_:
            raise ParameterIncompleteException('Phone number ID {} is invalid'.format(id_))
        self.endpoint = '/api/marketing/phone-numbers/' + str(id_) + '/'
        return super(Numbers, self).retrieve(**kwargs)

    def release(self, **kwargs):
        id_ = kwargs.pop('id', None)
        if not id_:
            raise ParameterIncompleteException('Phone number ID {} is invalid'.format(id_))
        self.endpoint = '/api/marketing/release-phone-number/' + str(id_) + '/'
        return super(Numbers, self).list(**kwargs)


class Redirect(CrudEntity):
    def inspect_endpoint(self, **kwargs):
        self.endpoint = '/api/marketing/numbers/redirects/'
        id_ = kwargs.pop('id', None)
        if id_:
            self.endpoint = '/api/marketing/numbers/redirects/' + str(id_) + '/'
