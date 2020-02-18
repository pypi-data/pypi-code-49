from gracie_feeds_api import GracieBaseAPI


class topicEntitiesController(GracieBaseAPI):
    """Topic entity."""

    _controller_name = "topicEntitiesController"

    def add(self, names, popularity, topicTypeId, **kwargs):
        """

        Args:
            alias: (string): alias
            briefs: (string): briefs is an array of:{ "text": "...brief text...", "languageId": "...long id..." }if you only pass one brief, you can omit the languageId
            names: (string): names is an array of:{ "name":  "somename", "isMainName":"true", "languageId": "....long id....." }and one of the names must have isMainName == true
            popularity: (integer): popularity
            topicTypeId: (string): topicTypeId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'alias': {'name': 'alias', 'required': False, 'in': 'query'}, 'briefs': {'name': 'briefs', 'required': False, 'in': 'query'}, 'names': {'name': 'names', 'required': True, 'in': 'query'}, 'popularity': {'name': 'popularity', 'required': True, 'in': 'query'}, 'topicTypeId': {'name': 'topicTypeId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/topicEntity/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def clone(self, id, topicTypeId, **kwargs):
        """

        Args:
            deleteSource: (boolean): deleteSource
            id: (string): id
            popularity: (integer): popularity
            topicTypeId: (string): topicTypeId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'deleteSource': {'name': 'deleteSource', 'required': False, 'in': 'query'}, 'id': {'name': 'id', 'required': True, 'in': 'query'}, 'popularity': {'name': 'popularity', 'required': False, 'in': 'query'}, 'topicTypeId': {'name': 'topicTypeId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/topicEntity/clone'
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
        api = '/topicEntity/delete'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def downloadExportFile(self, taskId):
        """

        Args:
            taskId: (string): taskId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'taskId': {'name': 'taskId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/topicEntity/downloadExportFile'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def edit(self, id, **kwargs):
        """

        Args:
            id: (string): id
            popularity: (integer): popularity
            topicTypeId: (string): topicTypeId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'id': {'name': 'id', 'required': True, 'in': 'query'}, 'popularity': {'name': 'popularity', 'required': False, 'in': 'query'}, 'topicTypeId': {'name': 'topicTypeId', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/topicEntity/edit'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def exportTopicEntities(self, topicTypeId, **kwargs):
        """

        Args:
            languageId: (string): languageId
            topicTypeId: (string): topicTypeId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'topicTypeId': {'name': 'topicTypeId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/topicEntity/exportTopicEntities'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def importTopicEntities(self, file, topicTypeId, **kwargs):
        """

        Args:
            file: (file): file
            languageId: (string): languageId
            stopOnError: (boolean): stopOnError
            topicTypeId: (string): topicTypeId

        Consumes:
            multipart/form-data

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'file': {'name': 'file', 'required': True, 'in': 'formData'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'stopOnError': {'name': 'stopOnError', 'required': False, 'in': 'query'}, 'topicTypeId': {'name': 'topicTypeId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/topicEntity/importTopicEntities'
        actions = ['post']
        consumes = ['multipart/form-data']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, **kwargs):
        """

        Args:
            languageId: (string): languageId
            limit: (integer): limit
            name: (string): Prefix of searched name
            offset: (integer): offset
            onlyMainNames: (boolean): onlyMainNames
            orderAsc: (boolean): orderAsc
            orderBy: (string): orderBy
            topicId: (string): topicId
            topicTypeId: (string): topicTypeId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'limit': {'name': 'limit', 'required': False, 'in': 'query'}, 'name': {'name': 'name', 'required': False, 'in': 'query'}, 'offset': {'name': 'offset', 'required': False, 'in': 'query'}, 'onlyMainNames': {'name': 'onlyMainNames', 'required': False, 'in': 'query'}, 'orderAsc': {'name': 'orderAsc', 'required': False, 'in': 'query'}, 'orderBy': {'name': 'orderBy', 'required': False, 'in': 'query'}, 'topicId': {'name': 'topicId', 'required': False, 'in': 'query'}, 'topicTypeId': {'name': 'topicTypeId', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/topicEntity/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def restore(self, id):
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
        api = '/topicEntity/restore'
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
        api = '/topicEntity/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
