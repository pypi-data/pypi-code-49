try:
    import h3

    h3.k_ring('841e265ffffffff', 4)
except AttributeError:
    from h3 import h3


def get_geojson_dict_of_hex_id_boundary(hex_id):
    """
    :param str hex_id:
        A hex ID
    :return dict:
        geoJSON-like dictionary
    """
    geojson_dict = {
        "type": "Polygon",
        "coordinates":
            [
                h3.h3_to_geo_boundary(
                    h3_address=str(hex_id),
                    geo_json=True)
            ]
    }
    return geojson_dict
