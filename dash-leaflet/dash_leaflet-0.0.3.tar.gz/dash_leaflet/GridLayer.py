# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GridLayer(Component):
    """A GridLayer component.
GridLayer is a wrapper of GridLayer in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- tileSize (number; optional): Width and height of tiles in the grid. Use a number if width and 
height are equal, or L.point(width, height) otherwise.
- opacity (number; optional): Opacity of the tiles. Can be used in the createTile() function.
- updateWhenIdle (boolean; optional): Load new tiles only when panning ends. true by default on mobile 
browsers, in order to avoid too many requests and keep smooth 
navigation. false otherwise in order to display new tiles during 
panning, since it is easy to pan outside the keepBuffer option 
in desktop browsers.
- updateWhenZooming (boolean; optional): By default, a smooth zoom animation (during a touch zoom or a 
flyTo()) will update grid layers every integer zoom level. 
Setting this option to false will update the grid layer only 
when the smooth animation ends.
- updateInterval (number; optional): Tiles will not update more than once every updateInterval 
milliseconds when panning.
- zIndex (number; optional): The explicit zIndex of the tile layer.
- bounds (list of numbers; optional): If set, tiles will only be loaded inside the set LatLngBounds.
- minZoom (number; optional): The minimum zoom level down to which this layer will be 
displayed (inclusive).
- maxZoom (number; optional): The maximum zoom level up to which this layer will be 
displayed (inclusive).
- minNativeZoom (number; optional): Minimum zoom number the tile source has available. If it 
is specified, the tiles on all zoom levels lower than 
minNativeZoom will be loaded from minNativeZoom level 
and auto-scaled.
- maxNativeZoom (number; optional): Maximum zoom number the tile source has available. If it
is specified, the tiles on all zoom levels higher than 
maxNativeZoom will be loaded from maxNativeZoom level 
and auto-scaled.
- noWrap (boolean; optional): Whether the layer is wrapped around the antimeridian. If 
true, the GridLayer will only be displayed once at low zoom 
levels. Has no effect when the map CRS doesn't wrap around. 
Can be used in combination with bounds to prevent requesting 
tiles outside the CRS limits.
- className (string; optional): A custom class name to assign to the tile layer. Empty by default.
- keepBuffer (number; optional): When panning the map, keep this many rows and columns of tiles 
before unloading them.
- id (string; optional): The ID used to identify this component in Dash callbacks
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component"""
    @_explicitize_args
    def __init__(self, children=None, tileSize=Component.UNDEFINED, opacity=Component.UNDEFINED, updateWhenIdle=Component.UNDEFINED, updateWhenZooming=Component.UNDEFINED, updateInterval=Component.UNDEFINED, zIndex=Component.UNDEFINED, bounds=Component.UNDEFINED, minZoom=Component.UNDEFINED, maxZoom=Component.UNDEFINED, minNativeZoom=Component.UNDEFINED, maxNativeZoom=Component.UNDEFINED, noWrap=Component.UNDEFINED, className=Component.UNDEFINED, keepBuffer=Component.UNDEFINED, id=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'tileSize', 'opacity', 'updateWhenIdle', 'updateWhenZooming', 'updateInterval', 'zIndex', 'bounds', 'minZoom', 'maxZoom', 'minNativeZoom', 'maxNativeZoom', 'noWrap', 'className', 'keepBuffer', 'id', 'pane', 'attribution']
        self._type = 'GridLayer'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'tileSize', 'opacity', 'updateWhenIdle', 'updateWhenZooming', 'updateInterval', 'zIndex', 'bounds', 'minZoom', 'maxZoom', 'minNativeZoom', 'maxNativeZoom', 'noWrap', 'className', 'keepBuffer', 'id', 'pane', 'attribution']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(GridLayer, self).__init__(children=children, **args)
