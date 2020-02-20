


##############
#
# DATA PRINTING
#
##############

def get_line(fields_value_list, max_width_value_list, separator='|'):
    """
    Return a string with values contains in fields_value_list separate by seperator and with for column width the
    informations contained in max_width_value_list

    :param fields_value_list: list of values that we want print
    :param max_width_value_list: list of width column for each values that we want print
    :param separator: separator character between each column
    :return: the formated values contain in fields_value_list
    """
    line = separator + separator.join([(' ' * (width_value + 2))[:1] + str(fields_value_list[i_field]) + (' ' * (
            width_value + 2))[len(str(fields_value_list[i_field])) + 1:] for i_field, width_value in
                                       enumerate(max_width_value_list)]) + separator

    return line


def get_header_separator(width_column_list, table_type='RST'):
    """
    Return a string header of data table

    :param width_column_list: the width for each column
    :param table_type: type of output (value : 'RST' or 'MD' only)
    :return: header separator
    """
    if table_type == 'RST':
        separator = '+'
        header = '='

    elif table_type == 'MD':
        separator = '|'
        header = '-'
    else:
        raise ValueError('error table type value {} not valid'.format(table_type))

    combi = header + separator + header

    return separator + header + combi.join(
        [header * width_value for width_value in width_column_list]) + header + separator


def get_line_separator(width_column_list):
    """
    Return a string separator between line of data table
    :param width_column_list:
    :return:
    """
    return '+-' + '-+-'.join(['-' * width_value for width_value in width_column_list]) + '-+'


def print_features_data_table(geolayer, field_name_list=None, print_i_feat=True, table_type='RST', light=True,
                              display_geo_data=False, max_width_coordinates_printing=30):
    """
    Returns a generator to display the attribute data of a geolayer    
    
    :param geolayer: geolayer that we want print
    :param field_name_list: if filled out we restrain printing on only indicate fields
    :param print_i_feat: choose if you want to see appears i_feat or not (default : NOT)
    :param table_type: choose type of printing ( 2 format allowed Markdown ('MD') or reStructuredText (RST))
    :param light: choose if you want a separator between line or not (default: NOT)
    :param display_geo_data: print geometry information (Geometry Type and Coordinates extract) ? (default: NOT)
    :param max_width_coordinates_printing: if display_geo_data is True you can choose the max width of coordinates 
    column. (if None all coordinates are print).
    
    :return: line that compose table
    """
    if not field_name_list:
        # create field name
        field_name_list = [None] * len(geolayer['metadata']['fields'])
        for i_field, field_name in enumerate(geolayer['metadata']['fields']):
            idx_field = geolayer['metadata']['fields'][field_name]['index']
            field_name_list[idx_field] = field_name

    max_width_value_list = [len(field_name) for field_name in field_name_list]

    if print_i_feat:
        key_max_width = len('i_feat')

    if display_geo_data:
        max_width_value_list += [len('type'), len('coordinates')]

    for i_feat in geolayer['features']:
        width_value_list = [len(str(geolayer['features'][i_feat]['attributes'][field_name])) if field_name in geolayer['features'][i_feat]['attributes'] else 0 for field_name in
                          field_name_list]

        if display_geo_data:
            width_coordinates = len(str(geolayer['features'][i_feat]['geometry']['coordinates']))
            if max_width_coordinates_printing:
                if width_coordinates > max_width_coordinates_printing:
                    width_coordinates = max_width_coordinates_printing

            width_value_list += [len(str(geolayer['features'][i_feat]['geometry']['type'])), width_coordinates]

        # compute width data_value
        for i_width_value, width_value in enumerate(width_value_list):
            if width_value > max_width_value_list[i_width_value]:
                max_width_value_list[i_width_value] = width_value

            # compute key width
            if print_i_feat:
                if len(str(i_feat)) > key_max_width:
                    key_max_width = len(str(i_feat))

    if print_i_feat:
        # add i_feat max wisth to field_name_list
        max_width_value_list = [key_max_width] + max_width_value_list
        # add 'i_feat' value to complete_field_name_list
        complete_field_name_list = ['i_feat'] + field_name_list
    else:
        complete_field_name_list = field_name_list

    # add field type and coordinates at the end
    if display_geo_data:
        complete_field_name_list = complete_field_name_list + ['type', 'coordinates']

    if table_type == 'RST':
        yield get_line_separator(max_width_value_list)

    yield get_line(complete_field_name_list, max_width_value_list)
    yield get_header_separator(max_width_value_list, table_type=table_type)

    for i_feat in geolayer['features']:

        field_value_list = [geolayer['features'][i_feat]['attributes'][field_name] if field_name in geolayer['features'][i_feat]['attributes'] else None for field_name in field_name_list]

        if print_i_feat:
            field_value_list = [i_feat] + field_value_list

        if display_geo_data:
            geometry_type = geolayer['features'][i_feat]['geometry']['type']
            field_value_list += [geometry_type]

            if geometry_type == 'GeometryCollection':
                coordinates_value = str(geolayer['features'][i_feat]['geometry']['geometries'])
            else:
                coordinates_value = str(geolayer['features'][i_feat]['geometry']['coordinates'])

            if max_width_coordinates_printing:
                coordinates_value = coordinates_value[:max_width_coordinates_printing]

                if len(coordinates_value) == max_width_coordinates_printing:
                    if geometry_type.upper() in ['POINT', 'GEOMETRYCOLLECTION']:  # ['Point', 'GeometryCollection']
                        coordinates_value = coordinates_value[:-5] + ' ...]'
                    elif geometry_type.upper() in ['LINESTRING', 'MULTIPOINT']:  # ['LineString', 'MultiPoint']
                        coordinates_value = coordinates_value[:-6] + ' ...]]'
                    elif geometry_type.upper() in ['POLYGON', 'MULTILINESTRING']:  # ['Polygon', 'MultiLineString']
                        coordinates_value = coordinates_value[:-7] + ' ...]]]'
                    elif geometry_type.upper() in ['MULTIPOLYGON']:  # ['MultiPolygon']
                        coordinates_value = coordinates_value[:-8] + ' ...]]]]'

            field_value_list += [coordinates_value]

        yield get_line(field_value_list, max_width_value_list)

        if table_type == 'RST':
            if light is False:
                yield get_line_separator(max_width_value_list)

    if table_type == 'RST':
        yield get_line_separator(max_width_value_list)


def print_metadata_field_table(geolayer, field_name_list=None, key_field_name='field name', order_value=False,
                               table_type='RST', light=True):
    """
    Returns a generator to display the metadata data of a geolayer

    :param geolayer:
    :param field_name_list: if filled out we restrain printing on only indicate fields
    :param key_field_name: name of column that contains field_name
    :param order_value: respect the order apparition of field_name ('index' key must be filled out in field metadata).
    (default: NOT)
    :param table_type: choose type of printing ( 2 format allowed Markdown ('MD') or reStructuredText (RST))
    :param light: choose if you want a separator between line or not (default: NOT)
    :return: line that compose table
    """

    dict_data = geolayer['metadata']['fields']
    if not field_name_list:
        # field_name_list = dict_data.items()[0][1].keys()
        key_0 = list(dict_data.keys())[0]
        field_name_list = list(dict_data[key_0].keys())

    max_width_value_list = [len(str(field_name)) for field_name in field_name_list]

    # create a calling list who is
    call_feature_order = list(dict_data.keys())

    # compute max width for data_value
    key_max_width = 0
    for i_field, key in enumerate(dict_data):
        width_value_list = [len(str(dict_data[key][field_name])) for field_name in field_name_list]
        # compute width data_value
        for i_width_value, width_value in enumerate(width_value_list):
            if width_value > max_width_value_list[i_width_value]:
                max_width_value_list[i_width_value] = width_value
        # compute key width
        if len(str(key)) > key_max_width:
            key_max_width = len(str(key))

        if order_value:
            idx = dict_data[key]['index']
            call_feature_order[idx] = key

    # add max key width to key width value list
    max_width_value_list = [key_max_width] + max_width_value_list

    # add key_field_name to field_name_list
    complete_field_name_list = [key_field_name] + field_name_list

    # create line separator
    # line_separator = '+-'+'-+-'.join(['-' * width_value for width_value in max_width_value_list])+'-+'
    line_separator = get_line_separator(max_width_value_list)

    # create fields name line
    line_field_name = get_line(complete_field_name_list, max_width_value_list)

    # generate table to print
    if table_type == 'RST':
        yield line_separator
    yield line_field_name
    yield get_header_separator(max_width_value_list, table_type=table_type)

    # for i_field, key in enumerate(dict_data):
    for i_feat in call_feature_order:
        field_value_list = [i_feat] + [dict_data[i_feat][field_name] for field_name in field_name_list]
        yield get_line(field_value_list, max_width_value_list)
        if not light:
            yield line_separator

    if table_type == 'RST':
        yield get_line_separator(max_width_value_list)
