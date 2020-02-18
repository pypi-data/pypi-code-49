from gracie_feeds_api import GracieBaseAPI


class clusterGroupController(GracieBaseAPI):
    """Сluster group"""

    _controller_name = "clusterGroupController"

    def add(self, clusterSetId, name, **kwargs):
        """

        Args:
            clusterSetId: (string): clusterSetId
            iterations: (integer): iterations
            languageId: (string): languageId
            maxClusters: (integer): maxClusters
            maxKeywords: (integer): maxKeywords
            minClusters: (integer): minClusters
            name: (string): name
            seed: (integer): seed

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'clusterSetId': {'name': 'clusterSetId', 'required': True, 'in': 'query'}, 'iterations': {'name': 'iterations', 'required': False, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'maxClusters': {'name': 'maxClusters', 'required': False, 'in': 'query'}, 'maxKeywords': {'name': 'maxKeywords', 'required': False, 'in': 'query'}, 'minClusters': {'name': 'minClusters', 'required': False, 'in': 'query'}, 'name': {'name': 'name', 'required': True, 'in': 'query'}, 'seed': {'name': 'seed', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/clusterGroup/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def clusterize(self, id, **kwargs):
        """

        Args:
            id: (string): id
            iterations: (integer): iterations
            languageId: (string): languageId
            maxClusters: (integer): maxClusters
            maxKeywords: (integer): maxKeywords
            minClusters: (integer): minClusters
            seed: (integer): seed

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'id': {'name': 'id', 'required': True, 'in': 'query'}, 'iterations': {'name': 'iterations', 'required': False, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'maxClusters': {'name': 'maxClusters', 'required': False, 'in': 'query'}, 'maxKeywords': {'name': 'maxKeywords', 'required': False, 'in': 'query'}, 'minClusters': {'name': 'minClusters', 'required': False, 'in': 'query'}, 'seed': {'name': 'seed', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/clusterGroup/clusterize'
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
        api = '/clusterGroup/delete'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, clusterSetId, **kwargs):
        """

        Args:
            clusterSetId: (string): clusterSetId
            limit: (integer): limit
            offset: (integer): offset
            orderAsc: (boolean): orderAsc
            orderBy: (string): orderBy

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'clusterSetId': {'name': 'clusterSetId', 'required': True, 'in': 'query'}, 'limit': {'name': 'limit', 'required': False, 'in': 'query'}, 'offset': {'name': 'offset', 'required': False, 'in': 'query'}, 'orderAsc': {'name': 'orderAsc', 'required': False, 'in': 'query'}, 'orderBy': {'name': 'orderBy', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/clusterGroup/list'
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
        api = '/clusterGroup/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
