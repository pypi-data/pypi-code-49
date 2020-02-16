from flask import Flask
from re import findall, match
from re import compile as compile_re

ENDPOINT_VALID_CHARS_REGEX = r'[^\.A-z]'
PARAM_VALID_CHARS_REGEX = r'<([A-z]+:)?([A-z_]+)>'


class RuleError(Exception):
    message: str

    def __str__(self):
        txt = '{}: {}'.format(self.__class__.__name__, self.message)
        return txt


class FieldRequiredError(RuleError):
    def __init__(self, field_name):
        self.message = 'Field "{}" is required for route rule'.format(
            field_name
        )


class InvalidCharsError(RuleError):
    def __init__(self, field_name):
        self.message = 'Field "{}" contains invalid characters'.format(
            field_name
        )


class InvalidValueError(RuleError):
    def __init__(self, field_name):
        self.message = 'Field "{}" contains invalid value'.format(
            field_name
        )


class Router():
    __app = None
    __endpoints = set()

    def __init__(self, app: Flask):
        self.__app = app

    def register(self, *routes):
        '''Registra as rotas dentro da aplicação
        '''

        for group in routes:
            try:
                for route in group:
                    # Validate rule fields
                    self.__validate_route(route)

                    # Get values from rule
                    endpoint = route.endpoint
                    rule = route.rule
                    view = route.view
                    methods = route.methods

                    # Add route to application
                    self.__app.add_url_rule(rule,
                                            endpoint,
                                            view,
                                            methods=methods)

                    self.__endpoints.add(endpoint)
            except RuleError as e:
                self.__register_error(e)

    def __validate_route(self, route):
        '''Validador da rota
        '''
        if findall(ENDPOINT_VALID_CHARS_REGEX, route.endpoint):
            raise InvalidCharsError('endpoint')

        if not route.rule:
            raise FieldRequiredError('rule')

        if not route.view:
            raise FieldRequiredError('view')

        if not callable(route.view):
            raise InvalidValueError('view')

    def __register_error(self, error):
        '''Retorno de error do registrador
        '''
        if self.__app.config['DEBUG']:
            print(error)
        else:
            raise error


class Route():

    def __init__(self, endpoint, rule, view, methods={'GET'}):
        self.__endpoint = endpoint
        self.__view = view

        if not rule.startswith('/'):
            rule = '/' + rule

        self.__rule = rule
        self.__methods = set(method.upper() for method in methods)
        self.__parameters = dict()
        self.__extract_parameters()

    @property
    def view(self):
        return self.__view

    @property
    def endpoint(self):
        return self.__endpoint

    @property
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, value):
        self.__rule = value

    @property
    def methods(self):
        return self.__methods

    @property
    def parameters(self):
        return self.__parameters

    def __extract_parameters(self):
        '''Extrai os parâmetros da url
        '''
        pattern_param = compile_re(PARAM_VALID_CHARS_REGEX)

        paths = self.__rule.split('/')

        for path in paths:
            if not pattern_param.match(path):
                continue

            path = path.strip('<>')
            parameter = path.split(':') if path.find(':') else ['string', path]
            self.__parameters[parameter[1]] = parameter[0]

    def __str__(self):
        return '{0} - (view: {1} | rule: {2} | methods: {3})'.format(
            self.__endpoint,
            self.__view.__name__,
            self.__rule,
            repr(self.__methods))
