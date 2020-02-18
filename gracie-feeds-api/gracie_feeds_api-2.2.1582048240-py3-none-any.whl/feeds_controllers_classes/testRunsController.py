from gracie_feeds_api import GracieBaseAPI


class testRunsController(GracieBaseAPI):
    """Test runs"""

    _controller_name = "testRunsController"

    def export(self, testDocumentId):
        """

        Args:
            testDocumentId: (string): testDocumentId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'testDocumentId': {'name': 'testDocumentId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-runs/export'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, testDocumentId, **kwargs):
        """

        Args:
            maxNumber: (integer): maxNumber
            offset: (integer): offset
            testDocumentId: (string): testDocumentId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'maxNumber': {'name': 'maxNumber', 'required': False, 'in': 'query'}, 'offset': {'name': 'offset', 'required': False, 'in': 'query'}, 'testDocumentId': {'name': 'testDocumentId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-runs/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def remove(self, testRunId):
        """

        Args:
            testRunId: (string): testRunId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'testRunId': {'name': 'testRunId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-runs/remove'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, testRunId):
        """

        Args:
            testRunId: (string): testRunId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'testRunId': {'name': 'testRunId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-runs/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
