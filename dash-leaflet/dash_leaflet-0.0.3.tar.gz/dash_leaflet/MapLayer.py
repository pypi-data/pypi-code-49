# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MapLayer(Component):
    """A MapLayer component.
MapLayer is a wrapper of MapLayer in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- id (string; optional): The ID used to identify this component in Dash callbacks
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'pane', 'attribution']
        self._type = 'MapLayer'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'pane', 'attribution']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MapLayer, self).__init__(children=children, **args)
