from gracie_dictionary_api import GracieBaseAPI


class inputLanguagesController(GracieBaseAPI):
    """Supported input languages."""

    _controller_name = "inputLanguagesController"

    def list(self):
        """"""

        all_api_parameters = {}
        parameters_names_map = {}
        api = '/input-languages/list'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, inputLanguageId):
        """

        Args:
            inputLanguageId: (string): inputLanguageId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'inputLanguageId': {'name': 'inputLanguageId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/input-languages/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
