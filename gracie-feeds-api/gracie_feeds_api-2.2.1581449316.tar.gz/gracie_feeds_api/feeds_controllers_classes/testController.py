from gracie_feeds_api import GracieBaseAPI


class testController(GracieBaseAPI):
    """Test Controller"""

    _controller_name = "testController"

    def convert(self, **kwargs):
        """

        Args:
            stringArg: (string): stringArg

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'stringArg': {'name': 'stringArg', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test/convert'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def test(self, argInteger, argIntegerArray, argString, argStringArray, **kwargs):
        """

        Args:
            argInteger: (integer): argInteger
            argIntegerArray: (array): argIntegerArray
            argIntegerArrayOptional: (array): argIntegerArrayOptional
            argIntegerOptional: (integer): argIntegerOptional
            argString: (string): argString
            argStringArray: (array): argStringArray
            argStringArrayOptional: (array): argStringArrayOptional
            argStringOptional: (string): argStringOptional

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'argInteger': {'name': 'argInteger', 'required': True, 'in': 'query'}, 'argIntegerArray': {'name': 'argIntegerArray', 'required': True, 'in': 'query'}, 'argIntegerArrayOptional': {'name': 'argIntegerArrayOptional', 'required': False, 'in': 'query'}, 'argIntegerOptional': {'name': 'argIntegerOptional', 'required': False, 'in': 'query'}, 'argString': {'name': 'argString', 'required': True, 'in': 'query'}, 'argStringArray': {'name': 'argStringArray', 'required': True, 'in': 'query'}, 'argStringArrayOptional': {'name': 'argStringArrayOptional', 'required': False, 'in': 'query'}, 'argStringOptional': {'name': 'argStringOptional', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test/test'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def testRequest(self, **kwargs):
        """

        Args:
            booleanArg: (boolean): booleanArg
            doubleArg: (number): doubleArg
            intArg: (integer): intArg
            longArg: (integer): longArg
            stringArg: (string): stringArg

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'booleanArg': {'name': 'booleanArg', 'required': False, 'in': 'query'}, 'doubleArg': {'name': 'doubleArg', 'required': False, 'in': 'query'}, 'intArg': {'name': 'intArg', 'required': False, 'in': 'query'}, 'longArg': {'name': 'longArg', 'required': False, 'in': 'query'}, 'stringArg': {'name': 'stringArg', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test/testRequest'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)

    def testTask(self, **kwargs):
        """

        Args:
            booleanArg: (boolean): booleanArg
            doubleArg: (number): doubleArg
            intArg: (integer): intArg
            longArg: (integer): longArg
            sleepMs: (integer): sleepMs
            stringArg: (string): stringArg

        Consumes:
            application/json

        Returns:
            application/json;charset=UTF-8
        """

        all_api_parameters = {'booleanArg': {'name': 'booleanArg', 'required': False, 'in': 'query'}, 'doubleArg': {'name': 'doubleArg', 'required': False, 'in': 'query'}, 'intArg': {'name': 'intArg', 'required': False, 'in': 'query'}, 'longArg': {'name': 'longArg', 'required': False, 'in': 'query'}, 'sleepMs': {'name': 'sleepMs', 'required': False, 'in': 'query'}, 'stringArg': {'name': 'stringArg', 'required': False, 'in': 'query'}}
        parameters_names_map = {}
        api = '/test/testTask'
        actions = ['post']
        consumes = ['application/json']
        params, data = self._format_params_for_api(locals(), all_api_parameters, parameters_names_map)
        return self._process_api(self._controller_name, api, actions, params, data, consumes)
