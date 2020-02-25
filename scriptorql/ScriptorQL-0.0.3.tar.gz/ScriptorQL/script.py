# import os


def df_to_SQL_insert(df, schema="dbo", table="Table"):
    """
    Generate SQL script:
        Insert Into Table(a, b)
        Values ("a1", "b1"), ("a2", "b2")
    """
    # _script_dir = os.path.dirname(__file__)
    # _template_file = "templates\\insert_values.sql"
    # _template_file_path = os.path.join(_script_dir, _template_file)

    columns = ', '.join(list(df))

    values = ''
    for index, row in df.iterrows():
        value = ''
        for column in list(df):
            value += "'{}',".format(row[column])
        values += '({}),\n\t'.format(value[:-1])
    values = values[:-3]

    # sql_insert_values = open(_template_file_path, "r").read()
    sql_insert_values = """
INSERT INTO {schema}.{table}({columns})
VALUES  {values}
    """

    result = sql_insert_values.format(schema=schema,
                                      table=table,
                                      columns=columns,
                                      values=values)
    return result
