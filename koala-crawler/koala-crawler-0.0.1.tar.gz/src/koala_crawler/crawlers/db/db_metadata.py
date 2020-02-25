from nada_dataprofilering.sql_script_generator.util_sql_scripts import metadata
from nada_dataprofilering.connectors.oracle import OracleConnector


def get_schema_metadata(connection_string: str, schema_name: str):
    dvh = OracleConnector(connection_string)

    columns = get_metadata(schema_name, dvh)
    tables = [get_table(column) for column in columns]

    return unique_tables(tables), unique_columns(columns)


def get_metadata(schema_name, dvh):
    sql_script_metadata = metadata(schema_name)
    column_metadata = dvh.execute_select(sql_script_metadata)

    return format_metadata(column_metadata)


def format_metadata(column_metadata):
    columns = []

    for i in range(len(column_metadata['SCHEMA_NAME'])):
        current_column = {'schema_name': column_metadata['SCHEMA_NAME'][i],
                          'table_name': column_metadata['TABLE_NAME'][i],
                          'column_name': column_metadata['COLUMN_NAME'][i],
                          'data_type': column_metadata['DATA_TYPE'][i],
                          'table_description': column_metadata['TABLE_DESCRIPTION'][i],
                          'column_description': column_metadata['COLUMN_DESCRIPTION'][i],
                          'team_name': column_metadata['TEAM_NAME'][i]}

        columns.append(current_column)

    return columns


def get_table(column):
    return {'table_name': column['table_name'],
            'schema_name': column['schema_name'],
            'team_name': column['team_name'],
            'table_description': column['table_description']}


def unique_columns(columns):
    return list({f"{column['table_name']}/{column['column_name']}": column for column in columns}.values())


def unique_tables(tables):
    return list({table['table_name']: table for table in tables}.values())


