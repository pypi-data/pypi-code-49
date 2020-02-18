#!/usr/bin/python3

import psycopg2
import jwt

from pyonf import pyonf

config = """
db_host: /var/run/postgresql/
db_port: 5432
db_admin: postgres
db_admin_password: changeme
kwollect_db_name: kwdb
kwollect_user: kwuser
kwollect_password: changeme
chunk_interval_hour: 12
chunk_compress_hour: 48
"""
config = pyonf(config, mandatory_opts = ['kwollect_password'])
globals().update(config)

# We must set chunk_interval_hour so that data in most recent interval fits in memory
# 1 row is about 200 units of storage
# ie: chunk_time_interval (sec) = (0.25*mem_size_in_mbytes*10^6) / (num_metrics_per_second*200)
# For instance, a 8GB machine would handle a chunk of one day with 100 metrics per sec.


def sql(cmd):
    global sql_cur
    # print(cmd)
    sql_cur.execute(cmd)


sql_conn = psycopg2.connect(
    host=db_host, port=db_port, user=db_admin, password=db_admin_password
)
sql_conn.autocommit = True
sql_cur = sql_conn.cursor()


sql(f"SELECT * FROM pg_database WHERE datname = '{kwollect_db_name}'")
db_exists = False
try:
    if sql_cur.fetchall():
        db_exists = True
except psycopg2.ProgrammingError:
    pass


if db_exists:
    print(f"Database {kwollect_db_name} already exists, skipping database and users creation")
else:
    print("Creating database...")
    sql(f"CREATE DATABASE {kwollect_db_name}")

    cmd = f"""
    DROP ROLE IF EXISTS {kwollect_user};
    CREATE USER {kwollect_user} WITH ENCRYPTED PASSWORD '{kwollect_password}';
    DROP ROLE IF EXISTS {kwollect_user}_ro;
    CREATE ROLE {kwollect_user}_ro nologin;
    GRANT ALL PRIVILEGES ON DATABASE {kwollect_db_name} TO {kwollect_user};
    GRANT {kwollect_user}_ro TO {kwollect_user};
    """
    sql(cmd)
sql_conn = psycopg2.connect(
    dbname=kwollect_db_name,
    host=db_host,
    port=db_port,
    user=db_admin,
    password=db_admin_password,
)
sql_conn.autocommit = True
sql_cur = sql_conn.cursor()


print("Creating or updating database schema...")
cmd = f"""
SET LOCAL SESSION AUTHORIZATION DEFAULT;
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

SET LOCAL SESSION AUTHORIZATION {kwollect_user};

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO {kwollect_user}_ro;

CREATE TABLE IF NOT EXISTS metrics (
  timestamp   TIMESTAMPTZ       DEFAULT NOW(),
  device_id   TEXT              NOT NULL,
  metric_id   TEXT              NOT NULL,
  value       DOUBLE PRECISION  DEFAULT 'NaN',
  labels      JSONB             DEFAULT NULL,
  PRIMARY KEY(timestamp, device_id, metric_id)
  );

{"SELECT create_hypertable('metrics', 'timestamp', chunk_time_interval => INTERVAL '%s hours');" % chunk_interval_hour if not db_exists else ""}
{"ALTER TABLE metrics SET (timescaledb.compress, timescaledb.compress_segmentby = 'device_id, metric_id, labels');" if not db_exists else ""}
{"SELECT add_compress_chunks_policy('metrics', INTERVAL '%s hours');" % chunk_compress_hour if not db_exists else ""}

CREATE INDEX IF NOT EXISTS metrics_device_idx ON metrics(device_id, timestamp DESC);
CREATE INDEX IF NOT EXISTS metrics_alias_idx
  ON metrics((labels->>'_device_alias'), timestamp DESC)
  WHERE labels IS NOT NULL AND labels ? '_device_alias';


CREATE TABLE IF NOT EXISTS promoted_metrics (
  device_id   TEXT              NOT NULL,
  metric_id   TEXT              NOT NULL
  );

CREATE OR REPLACE VIEW nodetime_by_job AS
  SELECT * FROM 
    (SELECT 0 AS job_id, now() AS start_time, now() AS stop_time, '' AS node) empty
  WHERE false;

CREATE OR REPLACE VIEW metrics_by_device AS
 SELECT metrics."timestamp",
    metrics.device_id,
    metrics.metric_id,
    metrics.value,
    metrics.labels
   FROM metrics
UNION
 SELECT metrics."timestamp",
    metrics.labels ->> '_device_alias'::text AS device_id,
    metrics.metric_id,
    sum(metrics.value) AS value,
    metrics.labels
   FROM metrics
  WHERE metrics.labels ? '_device_alias'::text
  GROUP BY metrics."timestamp", metrics.metric_id, metrics.labels; 

CREATE OR REPLACE VIEW metrics_by_job AS
 SELECT nodemetrics."timestamp",
    nodemetrics.device_id,
    nodemetrics.metric_id,
    nodemetrics.value,
    nodemetrics.labels,
    nodetime.start_time,
    nodetime.stop_time,
    nodetime.job_id
   FROM (
     SELECT nodetime_by_job.job_id,
            nodetime_by_job.node,
            nodetime_by_job.start_time,
            nodetime_by_job.stop_time
     FROM nodetime_by_job
     ) nodetime
   JOIN LATERAL (
     SELECT metrics."timestamp",
            metrics.device_id,
            metrics.metric_id,
            metrics.value,
            metrics.labels
     FROM metrics
     WHERE metrics."timestamp" > nodetime.start_time
       AND (nodetime.stop_time IS NULL OR metrics."timestamp" < nodetime.stop_time)
       AND metrics.device_id = nodetime.node
     UNION
     SELECT metrics."timestamp",
            metrics.labels ->> '_device_alias'::text AS device_id,
            metrics.metric_id,
            sum(metrics.value) AS value,
            metrics.labels
     FROM metrics
     WHERE metrics.labels ? '_device_alias'::text
       AND metrics.labels ->> '_device_alias' = nodetime.node
       AND metrics."timestamp" > nodetime.start_time
       AND (nodetime.stop_time IS NULL OR metrics."timestamp" < nodetime.stop_time)
     GROUP BY metrics."timestamp", metrics.metric_id, metrics.labels
     ) nodemetrics ON true;


SET LOCAL SESSION AUTHORIZATION default;
CREATE SCHEMA IF NOT EXISTS api;
GRANT ALL PRIVILEGES ON SCHEMA api TO {kwollect_user};
GRANT USAGE ON SCHEMA api TO {kwollect_user}_ro;

CREATE EXTENSION IF NOT EXISTS plpython3u;
UPDATE pg_language SET lanpltrusted = true WHERE lanname = 'plpython3u';


SET LOCAL SESSION AUTHORIZATION {kwollect_user};

CREATE OR REPLACE FUNCTION api.get_metrics(job_id INTEGER DEFAULT NULL,
                                           nodes TEXT DEFAULT NULL,
                                           devices TEXT DEFAULT NULL,
                                           metrics TEXT DEFAULT NULL,
                                           start_time TEXT DEFAULT NULL,
                                           end_time TEXT DEFAULT NULL)
RETURNS SETOF metrics AS $$
def time_to_sql(time):
    if not time:
        time = "now"
    try:
        return "to_timestamp(%f)" % float(time)
    except ValueError:
        return "'%s'::timestamp with time zone" % time

_devices = ",".join([arg for arg in [nodes,devices] if arg])
if not job_id and not _devices:
    plpy.error("Missing 'devices', 'nodes' or 'job_id' argument")
elif job_id:
    req = "SELECT timestamp, device_id, metric_id, value, labels FROM metrics_by_job WHERE job_id = %d" % job_id
elif _devices:
    _devices = [device.split('.')[0] for device in _devices.split(",")]
    req = "SELECT * FROM metrics_by_device WHERE device_id in ('%s')" % "','".join(_devices)
    end_time_sql = time_to_sql(end_time)
    if start_time:
        start_time_sql = time_to_sql(start_time)
    else:
        start_time_sql = end_time_sql + " - interval '5 min'"
    req += " AND %s <= timestamp AND timestamp <= %s" % (start_time_sql, end_time_sql)
if metrics:
    metrics_id = metrics.split(",")
    req += " AND metric_id in ('%s')" % "','".join(metrics_id)
req += " ORDER BY timestamp ASC"
plpy.info(req)
return plpy.execute(req)
$$ LANGUAGE 'plpython3u';
"""
sql(cmd)
print("Database setup done.")
print("")

print("Postgrest configuration file:")
print("-----------------")
print(
f"""db-uri = "postgres://{kwollect_user}:{kwollect_password}@{db_host if not "/" in db_host else "localhost"}:{db_port}/{kwollect_db_name}"
db-schema = "api"
db-anon-role = "{kwollect_user}_ro"
jwt-secret = "{kwollect_password * (1+(32//len(kwollect_password))) }" """
)
print("-----------------")
print("")
print("API token:")
print("-----------------")
print(jwt.encode({'role': kwollect_user}, kwollect_password, algorithm='HS256').decode())
print("-----------------")
