from fattureincloud import exceptions as exc


class DettagliMixin(object):
    @exc.on_http_error(exc.FattureInCloudDettagliError)
    def dettagli(self, id=None, token=None, **kwargs):
        """
        Retrieve a single object.
        """
        if id is None and token is None:
            if hasattr(self, 'get_id'):
                id = self.get_id()
            else:
                raise AttributeError('You need to specify at least one of id or token')

        path = '%s/dettagli' % self._path
        server_data = self.fattureincloud.http_request(path, data={'id': id, 'token': token}, **kwargs)
        return self._obj_cls(self, server_data[self._dettagli_obj_key])


class NuovoMixin(object):
    def _check_missing_nuovo_attrs(self, data):
        required, optional = self.get_nuovo_attrs()
        missing = []
        for attr in required:
            if attr not in data:
                missing.append(attr)
                continue
        if missing:
            raise AttributeError("Missing attributes: %s" % ", ".join(missing))

    def get_nuovo_attrs(self):
        """Return the required and optional arguments.

        Returns:
            tuple: 2 items: list of required arguments and list of optional
                   arguments for creation (in that order)
        """
        return getattr(self, "_nuovo_attrs", (tuple(), tuple()))

    @exc.on_http_error(exc.FattureInCloudNuovoError)
    def nuovo(self, data, **kwargs):
        """Create a new object.

        Args:
            data (dict): parameters to send to the server to create the
                         resource
            **kwargs: Extra options to send to the server (e.g. sudo)
        """
        self._check_missing_nuovo_attrs(data)

        # Handle specific URL for creation
        path = '%s/nuovo' % self._path
        server_data = self.fattureincloud.http_request(path, data=data, **kwargs)

        if 'new_id' in server_data:
            data['id'] = server_data['new_id']
        if 'id' in server_data:
            data['id'] = server_data['id']
        if 'token' in server_data:
            data['token'] = server_data['token']

        return self._obj_cls(self, data=data)


class ModificaMixin(object):
    def _check_missing_modifica_attrs(self, data):
        required, optional = self.get_modifica_attrs()
        missing = []
        for attr in required:
            if attr not in data:
                missing.append(attr)
                continue
        if missing:
            raise AttributeError("Missing attributes: %s" % ", ".join(missing))

    def get_modifica_attrs(self):
        """Return the required and optional arguments.

        Returns:
            tuple: 2 items: list of required arguments and list of optional
                   arguments for creation (in that order)
        """
        return getattr(self, "_modifica_attrs", (tuple(), tuple()))

    @exc.on_http_error(exc.FattureInCloudModificaError)
    def modifica(self, data=None, **kwargs):
        """Edit a object.

        Args:
            data (dict): parameters to send to the server to create the
                         resource
            **kwargs: Extra options to send to the server (e.g. sudo)
        """
        if data is None:
            data = {}

        if 'id' not in data and 'token' not in data and hasattr(self, 'get_id'):
            data['id'] = self.get_id()

        self._check_missing_modifica_attrs(data)

        # Handle specific URL for creation
        path = '%s/modifica' % self._path
        server_data = self.fattureincloud.http_request(path, data=data, **kwargs)

        if 'new_id' in server_data:
            data['id'] = server_data['new_id']
        if 'id' in server_data:
            data['id'] = server_data['id']
        if 'token' in server_data:
            data['token'] = server_data['token']

        return self._obj_cls(self, data)


class EliminaMixin(object):
    @exc.on_http_error(exc.FattureInCloudEliminaError)
    def elimina(self, id=None, token=None, **kwargs):
        """Delete an object on the server.

        Args:
            id: ID of the object to delete
            **kwargs: Extra options to send to the server (e.g. sudo)

        Raises:
            FattureInCloudDeleteError: If the server cannot perform the request
        """
        if id is None and token is None:
            if hasattr(self, 'get_id'):
                id = self.get_id()
            else:
                raise AttributeError('You need to specify at least one of id or token')

        path = '%s/elimina' % self._path
        self.fattureincloud.http_request(path, data={'id': id, 'token': token}, **kwargs)
        return None


class CRUDMixin(DettagliMixin, NuovoMixin, ModificaMixin, EliminaMixin):
    pass


class InfoMixin(object):
    @exc.on_http_error(exc.FattureInCloudInfoError)
    def info(self, anno, **kwargs):
        """
        Retrieve a single object.
        """
        if anno is None:
            raise AttributeError('You need to specify the anno attribute')

        path = '%s/info' % self._path
        return self.fattureincloud.http_request(path, data={'anno': anno}, **kwargs)


class InfoMailMixin(object):
    @exc.on_http_error(exc.FattureInCloudInfoMailError)
    def infomail(self, id=None, token=None, **kwargs):
        """
        Retrieve a single object.
        """
        if id is None and token is None:
            if hasattr(self, 'get_id'):
                id = self.get_id()
            else:
                raise AttributeError('You need to specify at least one of id or token')

        path = '%s/infomail' % self._path
        return self.fattureincloud.http_request(path, data={'id': id, 'token': token}, **kwargs)


class InviaMailMixin(object):
    def _check_missing_inviamail_attrs(self, data):
        required, optional = self.get_inviamail_attrs()
        missing = []
        for attr in required:
            if attr not in data:
                missing.append(attr)
                continue
        if missing:
            raise AttributeError("Missing attributes: %s" % ", ".join(missing))

    def get_inviamail_attrs(self):
        """Return the required and optional arguments.

        Returns:
            tuple: 2 items: list of required arguments and list of optional
                   arguments for creation (in that order)
        """
        return getattr(self, "_inviamail_attrs", (tuple(), tuple()))

    @exc.on_http_error(exc.FattureInCloudModificaError)
    def inviamail(self, data, **kwargs):
        """Send email about object

        Args:
            data (dict): parameters to send to the server to create the
                         resource
            **kwargs: Extra options to send to the server (e.g. sudo)
        """
        self._check_missing_inviamail_attrs(data)

        # Handle specific URL for creation
        path = '%s/inviamail' % self._path
        return self.fattureincloud.http_request(path, data=data, **kwargs)