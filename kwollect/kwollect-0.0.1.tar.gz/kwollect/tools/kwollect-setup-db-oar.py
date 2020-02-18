#!/usr/bin/python3

import psycopg2
from pyonf import pyonf

config = """
db_host: /var/run/postgresql/
db_port: 5432
db_admin: postgres
db_admin_password: changeme
kwollect_db_name: kwdb
kwollect_user: kwuser
oardb_host: oar
oardb_port: 5432
oardb_name: oar2
oardb_user: oarreader
oardb_password: read
"""
config = pyonf(config)
globals().update(config)

def sql(cmd):
    global sql_cur
    # print(cmd)
    sql_cur.execute(cmd)


sql_conn = psycopg2.connect(
    dbname=kwollect_db_name,
    host=db_host,
    port=db_port,
    user=db_admin,
    password=db_admin_password,
)
sql_conn.autocommit = True
sql_cur = sql_conn.cursor()

print("Creating OAR integration in database...")
sql(f"""
SET LOCAL SESSION AUTHORIZATION default;
CREATE EXTENSION IF NOT EXISTS  postgres_fdw;
CREATE SERVER oar_server  FOREIGN DATA WRAPPER postgres_fdw  OPTIONS (host '{oardb_host}', port '{oardb_port}', dbname '{oardb_name}');
ALTER SERVER oar_server OPTIONS (ADD use_remote_estimate 'true');
CREATE USER MAPPING FOR {kwollect_user} SERVER oar_server OPTIONS (user '{oardb_user}', password '{oardb_password}');
GRANT ALL PRIVILEGES ON FOREIGN SERVER oar_server TO {kwollect_user};
CREATE SCHEMA oar;
GRANT USAGE ON SCHEMA oar TO {kwollect_user};
GRANT ALL PRIVILEGES ON SCHEMA oar TO {kwollect_user};


SET LOCAL SESSION AUTHORIZATION {kwollect_user};
IMPORT FOREIGN SCHEMA public FROM SERVER oar_server INTO oar;

CREATE OR REPLACE VIEW nodetime_by_oarjob AS
  SELECT DISTINCT jobs.job_id,
    to_timestamp(jobs.start_time::double precision) AS start_time,
    CASE
      WHEN jobs.stop_time = 0 THEN NULL::timestamp with time zone
      ELSE to_timestamp(jobs.stop_time::double precision)
    END AS stop_time,
    split_part(resources.network_address::text, '.'::text, 1) AS node
  FROM oar.jobs,
    oar.assigned_resources,
    oar.resources
  WHERE jobs.assigned_moldable_job = assigned_resources.moldable_job_id
    AND assigned_resources.resource_id = resources.resource_id
    AND resources.type::text = 'default'::text;

CREATE OR REPLACE VIEW nodetime_by_job AS
  SELECT * FROM nodetime_by_oarjob;

CREATE OR REPLACE VIEW promoted_metrics_job AS
    SELECT distinct job_id, split_part(resources.network_address::text, '.'::text, 1) AS node
      FROM oar.jobs, oar.assigned_resources, oar.resources
      WHERE jobs.assigned_moldable_job = assigned_resources.moldable_job_id
        AND assigned_resources.resource_id = resources.resource_id
        AND resources.type::text = 'default'::text
        AND jobs.state = 'Running'
        AND job_name LIKE '%wattmetre%';

CREATE OR REPLACE FUNCTION api.update_promoted_metrics()
RETURNS SETOF promoted_metrics AS $$
BEGIN
  DELETE FROM promoted_metrics;
  RETURN QUERY INSERT INTO promoted_metrics(device_id, metric_id)
    SELECT DISTINCT node, 'wattmetre_power_watt' FROM promoted_metrics_job
    RETURNING *;
END;
$$ LANGUAGE 'plpgsql';
""")
print("Database setup for OAR integration done.")
