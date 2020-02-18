from gracie_dictionary_api import GracieBaseAPI


class testDocumentsController(GracieBaseAPI):
    """Test documents"""

    _controller_name = "testDocumentsController"

    def add(self, testGroupId, text, **kwargs):
        """

        Args:
            languageId: (string): languageId
            testGroupId: (string): testGroupId
            text: (type): text

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'testGroupId': {'name': 'testGroupId', 'required': True, 'in': 'query'}, 'text': {'name': 'text', 'required': True, 'in': 'body'}}
        parameters_names_map = {}
        api = '/test-documents/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def addFile(self, files, testGroupId, **kwargs):
        """

        Args:
            files: (array): files
            languageId: (string): languageId
            testGroupId: (string): testGroupId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'files': {'name': 'files', 'required': True, 'in': 'formData'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'testGroupId': {'name': 'testGroupId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-documents/addFile'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def edit(self, desiredResult, testDocumentId):
        """

        Args:
            desiredResult: (string): desiredResult
            testDocumentId: (string): testDocumentId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'desiredResult': {'name': 'desiredResult', 'required': True, 'in': 'query'}, 'testDocumentId': {'name': 'testDocumentId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-documents/edit'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, testGroupId, **kwargs):
        """

        Args:
            languageId: (string): languageId
            maxNumber: (integer): maxNumber
            offset: (integer): offset
            testGroupId: (string): testGroupId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'maxNumber': {'name': 'maxNumber', 'required': False, 'in': 'query'}, 'offset': {'name': 'offset', 'required': False, 'in': 'query'}, 'testGroupId': {'name': 'testGroupId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-documents/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def remove(self, testDocumentId):
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
        api = '/test-documents/remove'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, testDocumentId):
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
        api = '/test-documents/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
