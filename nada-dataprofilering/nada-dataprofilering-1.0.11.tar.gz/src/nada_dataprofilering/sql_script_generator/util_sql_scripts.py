def sample_statement(sample_pct, seed=0):
    return f"sample({sample_pct}) seed({seed})"


def sample_bool(number_rows, threshold=10000):
    if number_rows > threshold:
        return True
    else:
        return False


def metadata(schema):
    sql_string = f"""select
     a.owner as schema_name,
     a.table_name,
     a.column_name,
     a.data_type,
     b.comments as column_description,
     c.comments as table_description,
     d.team_name
     from all_tab_cols a
     inner join all_col_comments b
     on  a.table_name = b.table_name and a.column_name = b.column_name
     inner join all_tab_comments c
     on a.table_name = c.table_name
     inner join OSDDM_REPORT_REPOS.dmo_dstr_tables_to_team d on a.table_name = d.table_name
     where a.owner = '{schema}' and b.owner = '{schema}' and c.owner = '{schema}' and d.schema_name = '{schema}'"""

    return sql_string


def count_data(schema, table, column):
    sql_script = f"select {column} as verdi , count({column}) as antall " \
                 f"from {schema}.{table} group by {column}  having count({column}) >4 order by {column} asc"

    return sql_script
