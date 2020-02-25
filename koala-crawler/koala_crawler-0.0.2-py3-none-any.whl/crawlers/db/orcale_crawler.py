from collections.abc import Sequence, Callable
from koala_crawler.crawlers.crawler_base import CrawlerBase
from koala_crawler.crawlers.db import db_metadata


class OracleCrawler(CrawlerBase):

    def __init__(self, connection_string: str, schemas: Sequence ):
        super().__init__(__name__)
        self._connection_string = connection_string
        self._schemas = schemas

        if isinstance(self._schemas, str):
            self._schemas = [schemas]

    def __enter__(self):
        return self

    @property
    def collection_node_type(self):
        return "db_table"

    @property
    def required_collection_node_fields(self):
        return tuple(('schema_name', 'table_name', 'table_description', 'team_name'))

    @property
    def resource_node_type(self):
        return "db_table_column"

    @property
    def required_resource_node_fields(self):
        return tuple(('schema_name', 'table_name', 'table_description', 'column_name',
                      'column_description', 'data_type', 'team_name'))

    @property
    def required_edge_fields(self):
        return tuple(('n1', 'n2'))

    @property
    def collection_id_creator(self) -> Callable:
        return lambda column_map: f"{column_map['schema_name']}.{column_map['table_name']}"

    @property
    def resource_id_creator(self) -> Callable:
        return lambda column_map: f"{column_map['schema_name']}.{column_map['table_name']}.{column_map['column_name']}"

    def crawl(self) -> Sequence:
        tables = []
        columns = []
        for schema in self._schemas:
            self._crawl_tables(self._connection_string, schema, tables, columns)

        return self._create_graph_objects(tables, columns)

    def _crawl_tables(self, connection_string, schema, tables, columns) -> None:

        schema_tables, schema_columns = db_metadata.get_schema_metadata(connection_string, schema)

        self._logger.info(f"Gathered metadata and metrics on {len(schema_tables)} tables "
                          f"and {len(schema_columns)} columns from {schema}.")

        tables += schema_tables
        columns += schema_columns
