"""Class and functions for making beautiful and interactive HTML maps."""

import branca
import folium
import geojson
import numpy as np

import geospin.utilities.h3


class FoliumMap(folium.Map):
    """
    Creates a Map with Folium and Leaflet.js.
    See folium.Map for options.

    Extend `folium.Map` to add some functions and options.
    """

    def __init__(self, location=[51.133481, 10.018343], zoom_start=6, *args,
                 **kwargs):
        """
        Extend folium.Map.__init__().
        :param args: See folium.Map.__init__() for input a list of arguments.
        :param kwargs: See folium.Map.__init__() for input a list of arguments.
        """
        super(FoliumMap, self).__init__(*args,
                                        **dict(
                                            kwargs,
                                            location=location,
                                            zoom_start=zoom_start,
                                        ))

    def show(self):
        """
        Display the map.
        """
        return self


class GeospinMap(FoliumMap):
    """
    Creates a folium Map using Geospin styles (for now: the tile server).
    """

    def __init__(self, *args, **kwargs):
        """
        Extends folium.Map.__init__().

        :param args: See folium.Map.__init__() for input a list of arguments.
        :param kwargs: See folium.Map.__init__() for input a list of arguments.
        """
        super(GeospinMap, self).__init__(
            *args,
            **dict(
                kwargs,
                tiles=None,
            )
        )

        folium.raster_layers.TileLayer(
            tiles='http://maps.geospin.de/geospin-light-gray/{z}/{x}/{y}.png',
            attr='Geospin').add_to(
            self, name='Geospin Basemap')


class OSMMap(FoliumMap):
    """
    Creates a folium Map using the OSM tile server.
    """

    def __init__(self, *args, **kwargs):
        """
        Extends folium.Map.__init__().

        :param args: See folium.Map.__init__() for input a list of arguments.
        :param kwargs: See folium.Map.__init__() for input a list of arguments.
        """
        super(OSMMap, self).__init__(
            *args,
            **dict(
                kwargs,
                tiles='OpenStreetMap',
            )
        )


def get_marker_factory(icon_args=dict(), marker_args=dict()):
    """
    Returns a function pointer for creating markers.
    :param dict icon_args: Optional icon keyword arguments.
    :param dict marker_args: Optional marker keyword arguments.
    :return func marker_factory: Function marker with a location as argument.
    """

    def marker_factory(location):
        if icon_args:
            icon = folium.features.Icon(**icon_args)
            marker = folium.features.Marker(location,
                                            **dict(marker_args, icon=icon))
        else:
            marker = folium.features.Marker(location, **marker_args)

        return marker

    return marker_factory


class MarkerGroup(folium.FeatureGroup):
    """
    Add mutliple markers in a FeatureGroup.
    """

    def __init__(self, geometries, marker_fn, *args, **kwargs):
        """
        Extends folium.FeatureGroup.__init__().

        :param list[shapely.geometry] geometries: Centroid of each geometry will
            be used for visualization.
        :param marker_fn: Function pointer accepting a location ([lat, lon]) and
            returning a folium.Marker.
        :param args: See folium.Map.__init__() for input a list of arguments.
        :param kwargs: See folium.Map.__init__() for input a list of arguments.
        """
        super(MarkerGroup, self).__init__(*args, **kwargs)

        self.geometries = geometries
        self.marker_fn = marker_fn

        # Add marker for all given geometries.
        for geom in self.geometries:
            lat = geom.centroid.y
            lon = geom.centroid.x
            marker = self.marker_fn([lat, lon])
            marker.add_to(self)


class GridHeatmap(folium.raster_layers.ImageOverlay):
    """
    Creates a pseudo heatmap for gridded data. This can be features, predictions
    or any other values which where fetch for each point on a grid.

    Real kernel density heatmaps lead to boundary effects (i.e. the values
    are decreasing to the borders of the heatmap) which is overcome by this kind
    of visualization. This is basically a smoothened image of the grid values.

    Note: All the given geometries must form a grid which needs to be within one
        Polygon. If grids split into Multipolygons, the visualization won't
        work.
    """

    def __init__(self, gdf, value_column, cmap, opacity=0.5, name='Heatmap',
                 scale_values=True, mercator_project=True, **kwargs):
        """
        Extends folium.raster_layers.ImageOverlay.

        :param geopandas.GeoDataFrame gdf: GeoDataFrame including the geometries
        as well as the specified value_column.
        :param str value_column: Column name of the values to visualize.
        :param cmap: Colormap to map the given values to a color.
        :param float opacity: The opacity of the heatmap overlay.
            Default is 0.5.
        :param str name: Layername of the heatmap. This name will appear in the
            LayerControl. Default is 'Heatmap'.
        :param bool scale_values: If set to True, the given values are scaled
            [0,1]. If set to False, the passed values must be accepted by cmap.
        :param bool mercator_project: Default set to True, to project the
            gridded data onto the spherical world correctly.
        :param kwargs: Additional keyword arguments passed to the super class
            init.
        """
        gdf = gdf.copy()

        if scale_values:
            gdf = self._min_max_scale(gdf, value_column)

        img_overlay, bbox = self._get_overlay(gdf, value_column, cmap)

        super(GridHeatmap, self).__init__(
            img_overlay,
            bbox,
            **dict(
                kwargs,
                mercator_project=mercator_project,
                opacity=opacity,
                name=name,
            )
        )

    @staticmethod
    def _get_overlay(gdf, column_name, cmap):
        """
        Creates the image overlay given the data and geometries.

        :param geopandas.GeoDataFrame gdf: GeoDataFrame including the geometries
        as well as the specified value_column.
        :param str value_column: Column name of the values to visualize.
        :param cmap: Colormap to map the given values to a color.
        :return: img, bounding_box: The image overlay and the its bounding box
            given as  in [[lat_min, lon_min], [lat_max, lon_max]]
        """
        x = gdf.geometry.x.factorize(sort=True)[0]
        y = gdf.geometry.y.factorize(sort=True)[0]
        z = gdf[column_name].values

        # create array for image
        shape = (x.max() - x.min() + 1, y.max() - y.min() + 1, 4)
        img = np.ones(shape)
        img[:, :, 3] = 0

        for pixel in zip(x, y, z):
            img[pixel[0], pixel[1], :] = cmap(pixel[2])

        bounding_box = [[gdf.geometry.y.min(), gdf.geometry.x.min()],
                        [gdf.geometry.y.max(), gdf.geometry.x.max()]]

        img = np.rot90(img)
        img = np.array(img)
        return img, bounding_box

    @staticmethod
    def _min_max_scale(gdf, column_name):
        """
        Perform a min-max scaling of the values in the specified column.

        :param gdf: DataFrame to be changed.
        :param column_name: Column to scale.
        :return: DataFrame containing the scaled column.
        """
        min_val = gdf[column_name].min()
        max_val = gdf[column_name].max()

        if min_val == max_val:
            gdf[column_name] = gdf[column_name] / max_val
        else:
            gdf[column_name] = \
                (gdf[column_name] - min_val) / (max_val - min_val)

        return gdf


class H3Choropleth(folium.GeoJson):
    """
    Layer with color-coded `h3` hexagons

    Each hexagon is internally converted into boundary polygons represented by
    GeoJSON objects. On the map, the color of each polygon is given by the
    provided values.

    Example:
    >>> from geospin.utilities.visualization import maps
    >>> hex_ids = ['841f12dffffffff', '841f131ffffffff']
    >>> values = [1., 2.,]
    >>> h3_choropleth = maps.H3Choropleth(hex_ids, values)
    >>> my_map = maps.GeospinMap(location=(51.2, 10.4), zoom_start=7)
    >>> h3_choropleth.add_to(my_map)  # doctest: +ELLIPSIS
    <geospin.utilities.visualization.maps.H3Choropleth object at ...>
    >>> my_map.save('/tmp/my_map.html')
    """

    def __init__(self,
                 hex_ids,
                 values,
                 colormap=branca.colormap.linear.viridis,
                 fill_opacity=0.7,
                 ):
        """
        :param list or array_like hex_ids:
            Hex IDs of hexagons to plot
        :param list or array_like values:
            Values for each hex ID. These values determine the color.
        :param branca.ColorMap colormap:
            Defaults to viridis colormap (derived from `branca.LinearColormap`)
        :param float fill_opacity:
            Opacity of hexagons
        """
        self.hex_ids = hex_ids
        self.values = values
        self.colormap = colormap
        self.fill_opacity = fill_opacity
        self.value_name = 'value'

        # Check for nans, because colormap does not accept nans.
        self._raise_value_error_if_data_contains_nan()

        self._scale_colormap()

        super(H3Choropleth, self).__init__(
            data=H3BoundaryFeatureCollection(self.hex_ids, self.values),
            style_function=self._style_function,
            name="h3 heatmap"
        )

    def _raise_value_error_if_data_contains_nan(self):
        if np.isnan(self.values).sum() > 0:
            raise ValueError('Data contains NaN')

    def _scale_colormap(self):
        self.colormap = self.colormap.scale(min(self.values), max(self.values))

    def _style_function(self, feature):
        """
        Define style of color-coded polygons

        :param geojson.Feature feature: A GeoJSON feature
        :return dict: Style dictionary
        """
        return {
            'fillColor': self.colormap(feature['properties'][self.value_name]),
            'color': None,
            'weight': 1,
            'fillOpacity': self.fill_opacity
        }


class H3BoundaryFeature(geojson.Feature):
    """GeoJSON Feature that contains boundary geometry of hexagon"""

    def __init__(self, hex_id, value, value_name='value'):
        self.hex_id = hex_id
        super(H3BoundaryFeature, self).__init__(
            geometry=self._get_geometry(),
            id=self.hex_id,
            properties={value_name: value},
        )
        # If type is not set, it would be H3BoundaryFeature
        self.type = "Feature"

    def _get_geometry(self):
        """Get GeoJSON-like geometry of hexagon boundaries"""
        return geospin.utilities.h3.get_geojson_dict_of_hex_id_boundary(
            self.hex_id)


class H3BoundaryFeatureCollection(geojson.FeatureCollection):
    """GeoJSON FeatureCollection of _H3BoundaryFeature"""

    def __init__(self, hex_ids, values, value_name='value'):
        features = []
        for hex_id, value in zip(hex_ids, values):
            features.append(H3BoundaryFeature(hex_id, value, value_name))
        super(H3BoundaryFeatureCollection, self).__init__(features)
        # If type is not set, it would be H3BoundaryFeatureCollection
        self.type = "FeatureCollection"
