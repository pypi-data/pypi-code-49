# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DivOverlay(Component):
    """A DivOverlay component.
DivOverlay is a wrapper of DivOverlay in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- id (string; optional): The ID used to identify this component in Dash callbacks
- className (string; optional): The class of the component
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'pane', 'attribution']
        self._type = 'DivOverlay'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'pane', 'attribution']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DivOverlay, self).__init__(children=children, **args)
