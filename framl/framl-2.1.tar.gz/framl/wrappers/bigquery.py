from google.cloud import bigquery


class BigQuery:
    FIELDS_MAPPING = {
        "integer":   "INTEGER",
        "float":     "FLOAT",
        "boolean":   "BOOLEAN",
        "string":    "STRING",
        "timestamp": "TIMESTAMP"
    }

    PROJECT_ID = "bbc-data-science"
    DATASET_NAME = "framl"
    LOG_BUCKET = "framl-model-monitoring"

    @staticmethod
    def get_table_name(model_name: str) -> str:
        return model_name.replace("-", "_")

    @staticmethod
    def create_schema(model_params: dict) -> list:
        schema = [
            bigquery.SchemaField("prediction_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("prediction_time", "TIMESTAMP", mode="REQUIRED"),
            bigquery.SchemaField("model_version", "INTEGER", mode="REQUIRED"),
        ]

        inputs = []
        for feature_name, type_name in model_params.get("input").items():
            inputs.append(bigquery.SchemaField(feature_name, BigQuery.FIELDS_MAPPING[type_name]))

        schema.append(bigquery.SchemaField("input", "RECORD", fields=inputs))

        outputs = []
        for feature_name, type_name in model_params.get("output").items():
            outputs.append(bigquery.SchemaField(feature_name, BigQuery.FIELDS_MAPPING[type_name]))

        schema.append(bigquery.SchemaField("output", "RECORD", fields=outputs))

        return schema

    @staticmethod
    def create_external_table(model_name: str, schema: list) -> None:
        table_id = f"{BigQuery.PROJECT_ID}.{BigQuery.DATASET_NAME}.{BigQuery.get_table_name(model_name)}"
        client = bigquery.Client(project=BigQuery.PROJECT_ID)

        external_config = bigquery.ExternalConfig('NEWLINE_DELIMITED_JSON')
        external_config.autodetect = False
        external_config.ignore_unknown_values = True
        external_config.source_uris = f"gs://{BigQuery.LOG_BUCKET}/{model_name}/*"

        table = bigquery.Table(table_id, schema=schema)
        table.external_data_configuration = external_config
        table = client.create_table(table)
        print(f"Created external table {table.project}.{table.dataset_id}.{table.table_id}")
