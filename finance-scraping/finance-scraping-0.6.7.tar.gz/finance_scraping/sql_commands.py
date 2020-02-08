CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS {} (
    company_name VARCHAR,
    capital FLOAT,
    date DATE,
    time TIME,
    last_quote FLOAT,
    last_close FLOAT,
    daily_change_abs FLOAT,
    daily_change_rel FLOAT,
    bid FLOAT,
    offer FLOAT,
    low FLOAT,
    high FLOAT,
    day_volume FLOAT,
    p_e FLOAT,
    yield_percent FLOAT,
    collection_date DATE
    );"""

CREATE_NO_NULL_VIEW = """
    CREATE MATERIALIZED VIEW IF NOT EXISTS {table_name}_no_nulls
    AS
    SELECT * FROM {table_name}
    WHERE (
        company_name IS NOT NULL AND
        capital IS NOT NULL AND
        date IS NOT NULL AND
        last_quote IS NOT NULL AND
        p_e IS NOT NULL
    );"""

REFRESH_NO_NULL_VIEW = """REFRESH MATERIALIZED VIEW {table_name}_no_nulls;"""
