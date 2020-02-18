from gracie_dictionary_api import GracieBaseAPI


class clusterController(GracieBaseAPI):
    """Cluster"""

    _controller_name = "clusterController"

    def add(self, clusterGroupId, name):
        """

        Args:
            clusterGroupId: (string): clusterGroupId
            name: (string): name

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'clusterGroupId': {'name': 'clusterGroupId', 'required': True, 'in': 'query'}, 'name': {'name': 'name', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/cluster/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def copyDocuments(self, clusterId, targetId, **kwargs):
        """

        Args:
            clusterId: (string): clusterId
            languageId: (string): languageId
            targetId: (string): targetId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'clusterId': {'name': 'clusterId', 'required': True, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'targetId': {'name': 'targetId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/cluster/copyDocuments'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def delete(self, id):
        """

        Args:
            id: (string): id

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'id': {'name': 'id', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/cluster/delete'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def findNames(self, clusterId, **kwargs):
        """

        Args:
            clusterId: (string): clusterId
            languageId: (string): languageId
            maxNames: (integer): maxNames

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'clusterId': {'name': 'clusterId', 'required': True, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'maxNames': {'name': 'maxNames', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/cluster/findNames'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, clusterGroupId, **kwargs):
        """

        Args:
            clusterGroupId: (string): clusterGroupId
            limit: (integer): limit
            offset: (integer): offset
            orderAsc: (boolean): orderAsc
            orderBy: (string): orderBy

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'clusterGroupId': {'name': 'clusterGroupId', 'required': True, 'in': 'query'}, 'limit': {'name': 'limit', 'required': False, 'in': 'query'}, 'offset': {'name': 'offset', 'required': False, 'in': 'query'}, 'orderAsc': {'name': 'orderAsc', 'required': False, 'in': 'query'}, 'orderBy': {'name': 'orderBy', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/cluster/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, id):
        """

        Args:
            id: (string): id

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'id': {'name': 'id', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/cluster/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
