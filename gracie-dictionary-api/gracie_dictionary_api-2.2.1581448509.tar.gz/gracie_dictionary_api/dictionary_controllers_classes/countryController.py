from gracie_dictionary_api import GracieBaseAPI


class countryController(GracieBaseAPI):
    """Countries."""

    _controller_name = "countryController"

    def add(self, code, name, **kwargs):
        """

        Args:
            capital: (string): capital
            code: (string): code
            continentId: (string): continentId
            currencyCode: (string): currency-code
            currencyName: (string): currency-name
            name: (string): name
            phoneCode: (string): phone-code
            postalCodeFormat: (string): postal-code-format
            postalCodeRegExp: (string): postal-code-reg-exp
            topLevelDomain: (string): top-level-domain

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'capital': {'name': 'capital', 'required': False, 'in': 'query'}, 'code': {'name': 'code', 'required': True, 'in': 'query'}, 'continentId': {'name': 'continentId', 'required': False, 'in': 'query'}, 'currencyCode': {'name': 'currency-code', 'required': False, 'in': 'query'}, 'currencyName': {'name': 'currency-name', 'required': False, 'in': 'query'}, 'name': {'name': 'name', 'required': True, 'in': 'query'}, 'phoneCode': {'name': 'phone-code', 'required': False, 'in': 'query'}, 'postalCodeFormat': {'name': 'postal-code-format', 'required': False, 'in': 'query'}, 'postalCodeRegExp': {'name': 'postal-code-reg-exp', 'required': False, 'in': 'query'}, 'topLevelDomain': {'name': 'top-level-domain', 'required': False, 'in': 'query'}}
        parameters_names_map = {'currencyCode': 'currency-code', 'currencyName': 'currency-name', 'phoneCode': 'phone-code', 'postalCodeFormat': 'postal-code-format', 'postalCodeRegExp': 'postal-code-reg-exp', 'topLevelDomain': 'top-level-domain'}
        api = '/country/add'
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
        api = '/country/delete'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def edit(self, id, **kwargs):
        """

        Args:
            capital: (string): capital
            continentId: (string): continentId
            currencyCode: (string): currency-code
            currencyName: (string): currency-name
            id: (string): id
            name: (string): name
            phoneCode: (string): phone-code
            postalCodeFormat: (string): postal-code-format
            postalCodeRegExp: (string): postal-code-reg-exp
            topLevelDomain: (string): top-level-domain

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'capital': {'name': 'capital', 'required': False, 'in': 'query'}, 'continentId': {'name': 'continentId', 'required': False, 'in': 'query'}, 'currencyCode': {'name': 'currency-code', 'required': False, 'in': 'query'}, 'currencyName': {'name': 'currency-name', 'required': False, 'in': 'query'}, 'id': {'name': 'id', 'required': True, 'in': 'query'}, 'name': {'name': 'name', 'required': False, 'in': 'query'}, 'phoneCode': {'name': 'phone-code', 'required': False, 'in': 'query'}, 'postalCodeFormat': {'name': 'postal-code-format', 'required': False, 'in': 'query'}, 'postalCodeRegExp': {'name': 'postal-code-reg-exp', 'required': False, 'in': 'query'}, 'topLevelDomain': {'name': 'top-level-domain', 'required': False, 'in': 'query'}}
        parameters_names_map = {'currencyCode': 'currency-code', 'currencyName': 'currency-name', 'phoneCode': 'phone-code', 'postalCodeFormat': 'postal-code-format', 'postalCodeRegExp': 'postal-code-reg-exp', 'topLevelDomain': 'top-level-domain'}
        api = '/country/edit'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def list(self, **kwargs):
        """

        Args:
            continentId: (string): continentId
            orderAsc: (boolean): orderAsc
            orderBy: (string): orderBy

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'continentId': {'name': 'continentId', 'required': False, 'in': 'query'}, 'orderAsc': {'name': 'orderAsc', 'required': False, 'in': 'query'}, 'orderBy': {'name': 'orderBy', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/country/list'
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
        api = '/country/retrieve'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
