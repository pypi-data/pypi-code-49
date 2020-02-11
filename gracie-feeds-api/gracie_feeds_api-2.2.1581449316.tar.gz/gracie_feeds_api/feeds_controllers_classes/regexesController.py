from gracie_feeds_api import GracieBaseAPI


class regexesController(GracieBaseAPI):
    """Regexes."""

    _controller_name = "regexesController"

    def add(self, entityId, regex):
        """

        Args:
            entityId: (string): entityId
            regex: (string): regex

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'entityId': {'name': 'entityId', 'required': True, 'in': 'query'}, 'regex': {'name': 'regex', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/regexes/add'
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
        api = '/regexes/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def remove(self, regexId):
        """

        Args:
            regexId: (string): regexId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'regexId': {'name': 'regexId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/regexes/remove'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, regexId):
        """

        Args:
            regexId: (string): regexId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'regexId': {'name': 'regexId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/regexes/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
