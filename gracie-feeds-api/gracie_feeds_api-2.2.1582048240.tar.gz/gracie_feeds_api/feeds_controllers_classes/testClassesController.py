from gracie_feeds_api import GracieBaseAPI


class testClassesController(GracieBaseAPI):
    """Test classes"""

    _controller_name = "testClassesController"

    def runClass(self, className, **kwargs):
        """

        Args:
            className: (string): { "skillsets", "topics" }
            languageId: (string): languageId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'className': {'name': 'className', 'required': True, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-classes/runClass'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def runDocument(self, documentId):
        """

        Args:
            documentId: (string): id of some of documents { skill, topic-entity-brief, topic-type }

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'documentId': {'name': 'documentId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-classes/runDocument'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def runSubclass(self, subclassId, **kwargs):
        """

        Args:
            languageId: (string): languageId
            subclassId: (string): id of some of { skill, topic, topic-type }

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'subclassId': {'name': 'subclassId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test-classes/runSubclass'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
