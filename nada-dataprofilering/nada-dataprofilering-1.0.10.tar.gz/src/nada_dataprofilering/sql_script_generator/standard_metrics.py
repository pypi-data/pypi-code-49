from nada_dataprofilering.sql_script_generator.util_sql_scripts import *


# NO SAMPLING
def num_rows(schema, table, column):
    sql_string = f"select count({column}) from {schema}.{table}"
    return sql_string


def num_nulls(schema, table, column):
    sql_string = f"select sum(case when {column} is null then 1 else 0 end) from {schema}.{table}"
    return sql_string


def num_unique(schema, table, column):
    sql_string = f"select count(distinct {column}) from {schema}.{table}"
    return sql_string


def num_nulls_pct(number_nulls, number_rows):
    return (number_nulls/number_rows)*100


def num_unique_pct(number_unique, number_rows):
    return (number_unique/number_rows)*100


# SAMPLING
def num_sample_size(schema, table, column, sample_pct, seed=0):
    sql_string = f"select count({column}) from {schema}.{table} " + sample_statement(sample_pct, seed)
    return sql_string


# 'PURE' PYTHON FUNCTION
def num_sample_pct(number_rows, threshold=10000):
    return (threshold/number_rows)*100
