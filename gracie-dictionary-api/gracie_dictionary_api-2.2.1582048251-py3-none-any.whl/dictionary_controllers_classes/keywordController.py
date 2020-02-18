from gracie_dictionary_api import GracieBaseAPI


class keywordController(GracieBaseAPI):
    """Keywords."""

    _controller_name = "keywordController"

    def add(self, name, **kwargs):
        """

        Args:
            folderId: (string): Id is some of { topic, topic-type, skillset, skill, cluster set, cluster group, cluster }
            languageId: (string): languageId
            name: (string): name
            weight: (number): weight

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'folderId': {'name': 'folderId', 'required': False, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'name': {'name': 'name', 'required': True, 'in': 'query'}, 'weight': {'name': 'weight', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/keyword/add'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def bulkDelete(self, ids, **kwargs):
        """

        Args:
            addToBlacklist: (boolean): addToBlacklist
            ids: (array): ids

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'addToBlacklist': {'name': 'addToBlacklist', 'required': False, 'in': 'query'}, 'ids': {'name': 'ids', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/keyword/bulkDelete'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def delete(self, id, **kwargs):
        """

        Args:
            addToBlacklist: (boolean): addToBlacklist
            id: (string): id

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'addToBlacklist': {'name': 'addToBlacklist', 'required': False, 'in': 'query'}, 'id': {'name': 'id', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/keyword/delete'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def edit(self, id, weight):
        """

        Args:
            id: (string): id
            weight: (number): weight

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'id': {'name': 'id', 'required': True, 'in': 'query'}, 'weight': {'name': 'weight', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/keyword/edit'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, **kwargs):
        """

        Args:
            folderId: (string): Id is some of { topic, topic-type, skillset, skill, cluster set, cluster group, cluster }
            languageId: (string): * - request keywords in all languages. For sorting folders by proximity user's language is used.
            limit: (integer): limit
            offset: (integer): offset
            orderAsc: (boolean): true = ascending (default); false = descending
            orderBy: (string): { "NONE", "NAME", "WEIGHT", "PROXIMITY", "DOC2VEC", "KEYWORDS", "ENTITIES" }

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'folderId': {'name': 'folderId', 'required': False, 'in': 'query'}, 'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'limit': {'name': 'limit', 'required': False, 'in': 'query'}, 'offset': {'name': 'offset', 'required': False, 'in': 'query'}, 'orderAsc': {'name': 'orderAsc', 'required': False, 'in': 'query'}, 'orderBy': {'name': 'orderBy', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/keyword/list'
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
        api = '/keyword/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
