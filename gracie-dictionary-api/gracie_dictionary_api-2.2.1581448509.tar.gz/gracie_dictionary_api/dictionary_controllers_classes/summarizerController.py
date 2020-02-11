from gracie_dictionary_api import GracieBaseAPI


class summarizerController(GracieBaseAPI):
    """Summarize text down to N sentences."""

    _controller_name = "summarizerController"

    def summarize(self, maxSentences, text, **kwargs):
        """

        Args:
            inputLanguageId: (string): inputLanguageId
            maxSentences: (integer): maxSentences
            text: (type): text

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'inputLanguageId': {'name': 'inputLanguageId', 'required': False, 'in': 'query'}, 'maxSentences': {'name': 'maxSentences', 'required': True, 'in': 'query'}, 'text': {'name': 'text', 'required': True, 'in': 'body'}}
        parameters_names_map = {}
        api = '/summarize'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
