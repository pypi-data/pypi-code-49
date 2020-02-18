from gracie_feeds_api import GracieBaseAPI


class webLinksController(GracieBaseAPI):
    """Web links. """

    _controller_name = "webLinksController"

    def add(self, entityId, webLink):
        """

        Args:
            entityId: (string): entityId
            webLink: (string): web-link

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'entityId': {'name': 'entityId', 'required': True, 'in': 'query'}, 'webLink': {'name': 'web-link', 'required': True, 'in': 'query'}}
        parameters_names_map = {'webLink': 'web-link'}
        api = '/web-links/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, entityId):
        """

        Args:
            entityId: (string): entityId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'entityId': {'name': 'entityId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/web-links/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def remove(self, webLinkId):
        """

        Args:
            webLinkId: (string): webLinkId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'webLinkId': {'name': 'webLinkId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/web-links/remove'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, webLinkId):
        """

        Args:
            webLinkId: (string): webLinkId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'webLinkId': {'name': 'webLinkId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/web-links/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
