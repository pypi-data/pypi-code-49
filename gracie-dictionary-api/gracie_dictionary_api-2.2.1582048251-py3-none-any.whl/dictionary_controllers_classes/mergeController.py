from gracie_dictionary_api import GracieBaseAPI


class mergeController(GracieBaseAPI):
    """Databases"""

    _controller_name = "mergeController"

    def approve(self, editorId, entityId):
        """

        Args:
            editorId: (string): editorId
            entityId: (string): entityId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'editorId': {'name': 'editorId', 'required': True, 'in': 'query'}, 'entityId': {'name': 'entityId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/merge/approve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def approveAll(self, editorId, **kwargs):
        """

        Args:
            editorId: (string): editorId
            stopOnCollision: (boolean): stopOnCollision

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'editorId': {'name': 'editorId', 'required': True, 'in': 'query'}, 'stopOnCollision': {'name': 'stopOnCollision', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/merge/approveAll'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, editorId, **kwargs):
        """

        Args:
            editorId: (string): editorId
            maxNumber: (integer): maxNumber
            start: (integer): start

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'editorId': {'name': 'editorId', 'required': True, 'in': 'query'}, 'maxNumber': {'name': 'maxNumber', 'required': False, 'in': 'query'}, 'start': {'name': 'start', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/merge/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def merge(self, editorId):
        """

        Args:
            editorId: (string): editorId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'editorId': {'name': 'editorId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/merge/merge'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def reject(self, editorId, entityId, **kwargs):
        """

        Args:
            editorId: (string): editorId
            entityId: (string): entityId
            note: (string): note

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'editorId': {'name': 'editorId', 'required': True, 'in': 'query'}, 'entityId': {'name': 'entityId', 'required': True, 'in': 'query'}, 'note': {'name': 'note', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/merge/reject'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def rejectAll(self, editorId, **kwargs):
        """

        Args:
            editorId: (string): editorId
            note: (string): note

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'editorId': {'name': 'editorId', 'required': True, 'in': 'query'}, 'note': {'name': 'note', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/merge/rejectAll'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def write(self, editorId, entity, entityId, **kwargs):
        """

        Args:
            editorId: (string): editorId
            entity: (string): entity
            entityId: (string): entityId
            note: (string): note

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'editorId': {'name': 'editorId', 'required': True, 'in': 'query'}, 'entity': {'name': 'entity', 'required': True, 'in': 'query'}, 'entityId': {'name': 'entityId', 'required': True, 'in': 'query'}, 'note': {'name': 'note', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/merge/write'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
