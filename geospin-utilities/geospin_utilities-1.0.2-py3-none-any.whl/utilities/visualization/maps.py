"""Class and functions for making beautiful and interactive HTML maps."""

import folium
import numpy as np


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
