"""Contains functions to fetch zip codes."""

import fiona
import geopandas as gpd
import requests


def fetch_latest_zip_code_areas(
        url="https://www.suche-postleitzahl.org/download_files/public/plz-gebiete.shp.zip"  # noqa
):
    """Fetch the latest zip code areas for Germany.

    The latest release of zip code areas is downloaded and converted
    into a standardized format. The resulting data consists of two columns:
    'zip_code' and 'wkt'.

    .. note:: All polygons of an identical zip code will be merged to a
        union.

    :param str url: URL of the zipped shapefile containing zip code areas.
    :return: DataFrame containing columns `zip_code` and `wkt`.
    :rtype: geopandas.GeoDataFrame
    """
    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    with fiona.io.ZipMemoryFile(resp.content) as zip_memory_file:
        with zip_memory_file.open('plz-gebiete.shp') as collection:
            gdf = gpd.GeoDataFrame.from_features(collection, crs=collection.crs)

    gdf = gdf[['plz', 'geometry']]
    gdf = gdf.dissolve(by='plz')

    gdf = gdf.reset_index()
    gdf = gdf.rename(columns={"plz": "zip_code", "geometry": "wkt"})

    return gdf
