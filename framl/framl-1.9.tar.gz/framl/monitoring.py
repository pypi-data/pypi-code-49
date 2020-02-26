from typing import Union, List
from framl.config_model import ConfigModel
from framl.wrappers.bigquery import BigQuery
from framl.wrappers.pubsub import Pubsub
from google.cloud import bigquery


class Monitoring:

    def __init__(self, app_path: str):
        model_conf_ob = ConfigModel(app_path)
        self._model_params = model_conf_ob.get_monitored_fields()

        self._model_name = model_conf_ob.get_model_name()
        self._project_id = model_conf_ob.get_gcp_project_id()

    def prepare_table(self) -> None:
        schema = BigQuery.create_schema(self._model_params)
        BigQuery.create_external_table(self._model_name, schema)

    def list(self) -> dict:
        return {
            "topic":  f"projects/{Pubsub.PROJECT_ID}/topics/{Pubsub.TOPIC_NAME}",
            "bucket": "gs://framl-model-monitoring",
            "table":  f"{BigQuery.PROJECT_ID}:{BigQuery.DATASET_NAME}.{BigQuery.get_table_name(self._model_name)}"
        }
