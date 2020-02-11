from gracie_feeds_api import GracieBaseAPI


class skillParametersController(GracieBaseAPI):
    """Skill parameters."""

    _controller_name = "skillParametersController"

    def edit(self, skillId, **kwargs):
        """

        Args:
            languageId: (string): languageId
            normalizationHigherThreshold: (number): normalizationHigherThreshold
            normalizationLowerThreshold: (number): normalizationLowerThreshold
            skillId: (string): skillId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'normalizationHigherThreshold': {'name': 'normalizationHigherThreshold', 'required': False, 'in': 'query'}, 'normalizationLowerThreshold': {'name': 'normalizationLowerThreshold', 'required': False, 'in': 'query'}, 'skillId': {'name': 'skillId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/skillParameters/edit'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def retrieve(self, skillId, **kwargs):
        """

        Args:
            languageId: (string): languageId
            skillId: (string): skillId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'languageId': {'name': 'languageId', 'required': False, 'in': 'query'}, 'skillId': {'name': 'skillId', 'required': True, 'in': 'query'}}
        parameters_names_map = {}
        api = '/skillParameters/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
