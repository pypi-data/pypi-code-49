from gracie_dictionary_api import GracieBaseAPI


class searchController(GracieBaseAPI):
    """Search"""

    _controller_name = "searchController"

    def processFile(self, file, **kwargs):
        """

        Args:
            file: (file): file
            filterFields: (string): filterFields
            idfScoreMin: (number): idfScoreMin
            includeKeywordsReport: (boolean): includeKeywordsReport
            inputLanguageId: (string): inputLanguageId
            logging: (boolean): logging
            minRelevance: (integer): min-relevance
            pipelineId: (string): pipelineId
            stopAfterChunkNum: (integer): stopAfterChunkNum
            typeId: (string): typeId

        Consumes:
            multipart/form-data

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'file': {'name': 'file', 'required': True, 'in': 'formData'}, 'filterFields': {'name': 'filterFields', 'required': False, 'in': 'query'}, 'idfScoreMin': {'name': 'idfScoreMin', 'required': False, 'in': 'query'}, 'includeKeywordsReport': {'name': 'includeKeywordsReport', 'required': False, 'in': 'query'}, 'inputLanguageId': {'name': 'inputLanguageId', 'required': False, 'in': 'query'}, 'logging': {'name': 'logging', 'required': False, 'in': 'query'}, 'minRelevance': {'name': 'min-relevance', 'required': False, 'in': 'query'}, 'pipelineId': {'name': 'pipelineId', 'required': False, 'in': 'query'}, 'stopAfterChunkNum': {'name': 'stopAfterChunkNum', 'required': False, 'in': 'query'}, 'typeId': {'name': 'typeId', 'required': False, 'in': 'query'}}
        parameters_names_map = {'minRelevance': 'min-relevance'}
        api = '/search/processFile'
        actions = ['post']
        consumes = ['multipart/form-data']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def processText(self, text, **kwargs):
        """

        Args:
            filterFields: (string): filterFields
            idfScoreMin: (number): idfScoreMin
            includeKeywordsReport: (boolean): includeKeywordsReport
            inputLanguageId: (string): inputLanguageId
            logging: (boolean): logging
            minRelevance: (integer): min-relevance
            pipelineId: (string): pipelineId
            stopAfterChunkNum: (integer): stopAfterChunkNum
            text: (type): text
            typeId: (string): typeId

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'filterFields': {'name': 'filterFields', 'required': False, 'in': 'query'}, 'idfScoreMin': {'name': 'idfScoreMin', 'required': False, 'in': 'query'}, 'includeKeywordsReport': {'name': 'includeKeywordsReport', 'required': False, 'in': 'query'}, 'inputLanguageId': {'name': 'inputLanguageId', 'required': False, 'in': 'query'}, 'logging': {'name': 'logging', 'required': False, 'in': 'query'}, 'minRelevance': {'name': 'min-relevance', 'required': False, 'in': 'query'}, 'pipelineId': {'name': 'pipelineId', 'required': False, 'in': 'query'}, 'stopAfterChunkNum': {'name': 'stopAfterChunkNum', 'required': False, 'in': 'query'}, 'text': {'name': 'text', 'required': True, 'in': 'body'}, 'typeId': {'name': 'typeId', 'required': False, 'in': 'query'}}
        parameters_names_map = {'minRelevance': 'min-relevance'}
        api = '/search/processText'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
