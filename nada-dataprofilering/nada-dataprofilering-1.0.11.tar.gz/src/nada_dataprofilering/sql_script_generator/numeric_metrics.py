from nada_dataprofilering.sql_script_generator.util_sql_scripts import *
from math import *


# NO SAMPLING
def num_min(schema, table, column):
    sql_string = f"select min({column}) from {schema}.{table}"
    return sql_string


def num_max(schema, table, column):
    sql_string = f"select max({column}) from {schema}.{table}"
    return sql_string


def num_median(schema, table, column):
    sql_string = f"select median({column}) from {schema}.{table}"
    return sql_string


def num_percentile(schema, table, column, p):
    sql_string = f"select percentile_disc({p}) within group(order by {column}) from {schema}.{table}"
    return sql_string


def num_sum(schema, table, column):
    sql_string = f"select sum({column}) from {schema}.{table}"
    return sql_string


def num_zero(schema, table, column):
    sql_script = f"select sum(case when {column} = 0 then 1 else 0 end) from {schema}.{table}"
    return sql_script


# SAMPLING
def num_mean(schema, table, column, sampling, sample_pct):
    sql_string = f"select avg({column}) from {schema}.{table} "
    if sampling:
        sql_string += sample_statement(sample_pct)

    return sql_string


def num_var(schema, table, column, sampling, sample_pct):
    sql_string = f"select variance({column}) from {schema}.{table} "
    if sampling:
        sql_string += sample_statement(sample_pct)

    return sql_string


def num_mad(schema, table, column, median_value, sampling, sample_pct):
    sql_string = f"select median(abs({column} - {median_value})) from {schema}.{table} "
    if sampling:
        sql_string += sample_statement(sample_pct)

    return sql_string


def num_sum_n_power(schema, table, column, mean_value, n, sampling, sample_pct):
    sql_string = f"select sum(power({column}- {mean_value},{n})) from {schema}.{table} "
    if sampling:
        sql_string += sample_statement(sample_pct)

    return sql_string


# 'PURE' PYTHON FUNCTIONS
def num_range(min_value, max_value):
    return max_value - min_value


def num_iqr(q1, q3):
    return q3 - q1


def num_std(var_value):
    return sqrt(var_value)


def num_cov(std_value, mean_value):
    if mean_value != 0:
        return std_value/mean_value
    else:
        return 'NaN'


def num_skewness(number_rows, sample_size, sampling, std_value, sum_3_power):
    if std_value == 0:
        return 'NaN'
    else:
        if sampling:
            return (sum_3_power/sample_size)/(std_value**3)
        else:
            return (sum_3_power/number_rows)/(std_value**3)


def num_kurt(number_rows, sample_size, sampling, sum_2_power, sum_4_power):
    if sum_2_power == 0:
        return 'NaN'
    else:
        if sampling:
            return (sum_4_power/sample_size)/(sum_2_power/sample_size)**2 - 3
        else:
            return (sum_4_power/number_rows)/(sum_2_power/number_rows)**2 - 3

