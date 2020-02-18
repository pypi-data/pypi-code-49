from .requestor import ApiRequestor


class CrudEntity(object):
    endpoint = ''
    data = dict()
    files = dict()
    token = None

    def __init__(self, token):
        super(CrudEntity, self).__init__()
        self.token = token

    @classmethod
    def clean_data(cls, data_dict):
        """Splits the data into formdata and files"""
        files = dict()
        data = dict()
        for key, value in data_dict.items():
            try:
                file = value
                if type(value) == tuple and hasattr(value[1], 'read'):
                    # must be a file with its filename as the first element in the tuple
                    file = value[1]
                files.update({key: (value[0].split('/')[-1], file.read())})
            except Exception as e:
                data.update({key: value})
        as_json = not bool(files)
        return data, files, as_json

    def interceptor(self, requestor):
        """
        Override this to modify what ever is being sent, you could modify headers, modify data, anything
        See the ApiRequestor Object to know what properties you can modify. Make sure to return the requestor
        """
        return requestor

    def handle_request(self, requestor, as_json=True):
        requestor = self.interceptor(requestor)
        return requestor.send(as_json=as_json)

    def inspect_endpoint(self, **kwargs):
        """
        This method is called on every function in this class, you can use this method to fill in dynamic urls
        or whatever you may want to use it for. It was added to manipulate the endpoint
        """
        pass

    def create(self, url_params=None, **kwargs):
        """
        To use this method, simply override it after inheriting the class and set the class attributes; endpoint,
        and return super().create()
        :return: JSON data returned from the endpoint
        """
        if not kwargs.pop('skip_inspect', False):
            self.inspect_endpoint(**kwargs)
        data, files, as_json = self.clean_data(kwargs)
        return self.handle_request(
            ApiRequestor(
                endpoint=self.endpoint,
                data=data,
                files=files,
                method='POST',
                token=self.token,
                params=url_params
            ),
            as_json=as_json
        )

    def delete(self, url_params=None, **kwargs):
        """
        To use this method, simply override it after inheriting the class and set the class attributes; endpoint
         and return super().delete()
        :return: JSON data returned from the endpoint
        """
        if not kwargs.pop('skip_inspect', False):
            self.inspect_endpoint(**kwargs)
        self.handle_request(
            ApiRequestor(
                endpoint=self.endpoint,
                method='DELETE',
                token=self.token,
                params=url_params
            )
        )

    def retrieve(self, url_params=None, **kwargs):
        """
        To use this method, simply override it after inheriting the class and set the class attributes; endpoint
         and return super().retrieve()
        :return: JSON data returned from the endpoint
        """
        if not kwargs.pop('skip_inspect', False):
            self.inspect_endpoint(**kwargs)
        return self.handle_request(
            ApiRequestor(
                endpoint=self.endpoint,
                method='GET',
                token=self.token,
                params=url_params
            )
        )

    def update(self, url_params=None, **kwargs):
        """
        To use this method, simply override it after inheriting the class and set the class attributes; endpoint,
        and return super().update()
        :return: JSON data returned from the endpoint
        """
        if not kwargs.pop('skip_inspect', False):
            self.inspect_endpoint(**kwargs)
        data, files, as_json = self.clean_data(kwargs)
        return self.handle_request(
            ApiRequestor(
                endpoint=self.endpoint,
                data=data,
                files=files,
                method='PATCH',
                token=self.token,
                params=url_params
            ),
            as_json=as_json
        )

    def list(self, url_params=None, **kwargs):
        if not kwargs.pop('skip_inspect', False):
            self.inspect_endpoint(**kwargs)
        return self.handle_request(
            ApiRequestor(
                method='GET',
                endpoint=self.endpoint,
                token=self.token,
                params=url_params
            )
        )
