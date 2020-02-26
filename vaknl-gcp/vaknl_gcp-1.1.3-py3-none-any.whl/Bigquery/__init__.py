__author__ = "Wytze Bruinsma"

import json
import logging

from google.cloud import bigquery

from vaknl_gcp.DataClasses import rec_to_json
from vaknl_gcp import project_id

BIGQUERY_CLIENT = bigquery.Client(project=project_id)


def execute_query(query):
    # ----------------------------------------------------------------------------------------------------------------
    # Execute query and log errors
    # ----------------------------------------------------------------------------------------------------------------
    query_job = BIGQUERY_CLIENT.query(query)
    logging.info(f'EXECUTE QUERY: {query}'.rstrip())
    if query_job.errors:
        logging.warning(f'QUERY: {query} ERROR:{query_job.errors}'.rstrip())
        assert False, f'QUERY: {query} ERROR:{query_job.errors}'.rstrip()
    return query_job


def stream_to_bigquery(objects: list, table_ref):
    # ----------------------------------------------------------------------------------------------------------------
    # Cast python objects to json and stream them to GBQ
    # Note: this is more expensive compared to using buckets but also quicker
    # ----------------------------------------------------------------------------------------------------------------
    batch_size = 2000
    table = BIGQUERY_CLIENT.get_table(table=table_ref)

    for i in range(0, len(objects), batch_size):
        batch = objects[i:i + batch_size]
        json_batch = list(map(lambda x: json.loads(json.dumps(rec_to_json(x))), batch))
        error = BIGQUERY_CLIENT.insert_rows_json(table=table, json_rows=json_batch)
        if error:
            logging.warning(error)
            assert False, error


def write_disposition_bucket(table_ref, blob_name, write_disposition):
    # ----------------------------------------------------------------------------------------------------------------
    # Get data from bucket to GBQ using a write_disposition method
    # ----------------------------------------------------------------------------------------------------------------
    """
    WRITE_DISPOSITION_UNSPECIFIED	Unknown.
    WRITE_EMPTY	This job should only be writing to empty tables.
    WRITE_TRUNCATE	This job will truncate table data and write from the beginning.
    WRITE_APPEND	This job will append to a table.
    """
    job_config = bigquery.LoadJobConfig()
    job_config.schema = BIGQUERY_CLIENT.get_table(table_ref).schema
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.write_disposition = write_disposition

    uri = f'gs://storage_to_bigquery-{project_id}/{blob_name}'
    logging.info(
        f'STORAGE TO GBQ - method: {write_disposition}, blob name: {blob_name}, destination: {table_ref}'.rstrip())
    load_job = BIGQUERY_CLIENT.load_table_from_uri(
        uri,
        destination=table_ref,
        location="EU",  # Location must match that of the destination dataset.
        job_config=job_config
    )  # API request

    load_job.result()
