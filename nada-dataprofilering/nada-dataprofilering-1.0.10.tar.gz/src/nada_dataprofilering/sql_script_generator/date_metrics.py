def date_min(schema, table, column):
    sql_string = f"select min({column}) from {schema}.{table}"
    return sql_string


def date_median(schema, table, column):
    sql_string = f"select median({column}) from {schema}.{table}"
    return sql_string


def date_max(schema, table, column):
    sql_string = f"select max({column}) from {schema}.{table}"
    return sql_string

