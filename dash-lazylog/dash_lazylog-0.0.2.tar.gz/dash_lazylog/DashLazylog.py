# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashLazylog(Component):
    """A DashLazylog component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- props (dict; optional): Properties to pass onto react-lazylog. See:
https://mozilla-frontend-infra.github.io/react-lazylog/"""
    @_explicitize_args
    def __init__(self, props=Component.UNDEFINED, **kwargs):
        self._prop_names = ['props']
        self._type = 'DashLazylog'
        self._namespace = 'dash_lazylog'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['props']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashLazylog, self).__init__(**args)
