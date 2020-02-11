from gracie_feeds_api import GracieBaseAPI


class testGroupsController(GracieBaseAPI):
    """Test groups"""

    _controller_name = "testGroupsController"

    def add(self, code, **kwargs):
        """

        Args:
            code: (string): code
            languageId: (string): languageId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'code': {'name': 'code', 'required': True, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-groups/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self):
        """"""

        all_api_parameters = {}
        parameters_names_map = {}
        api = '/test-groups/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def remove(self, testGroupId):
        """

        Args:
            testGroupId: (string): testGroupId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'testGroupId': {'name': 'testGroupId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-groups/remove'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, testGroupId):
        """

        Args:
            testGroupId: (string): testGroupId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'testGroupId': {'name': 'testGroupId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-groups/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def run(self, testGroupId, **kwargs):
        """

        Args:
            includeChanged: (boolean): includeChanged
            includeMissing: (boolean): includeMissing
            includeUnchanged: (boolean): includeUnchanged
            includeUnexpected: (boolean): includeUnexpected
            languageId: (string): languageId
            testGroupId: (string): testGroupId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'includeChanged': {'name': 'includeChanged', 'required': False, 'in': 'query'}, 'includeMissing': {'name': 'includeMissing', 'required': False, 'in': 'query'}, 'includeUnchanged': {'name': 'includeUnchanged', 'required': False, 'in': 'query'}, 'includeUnexpected': {'name': 'includeUnexpected', 'required': False, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'testGroupId': {'name': 'testGroupId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-groups/run'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
