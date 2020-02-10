from google.cloud import bigquery


class BQ(object):
    def __init__(self, dataset_id=None, table_id=None, project_id=None, cred_file_path=None):
        self.dataset_id = dataset_id
        self.table_id = table_id
        if cred_file_path is None:
            self.client = bigquery.Client(project=project_id)
        else:
            self.client = bigquery.Client.from_service_account_json(cred_file_path)
        if project_id is not None:
            self.client.project = project_id

    def __dataset_id(self, dataset_id):
        if dataset_id is None:
            dataset_id = self.dataset_id
        return dataset_id

    def __table_id(self, table_id):
        if table_id is None:
            table_id = self.table_id
        return table_id

    def create_dataset(self, dataset_id=None, location='EU'):
        dataset_id = self.__dataset_id(dataset_id)
        dataset_ref = self.client.dataset(dataset_id)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = location
        self.client.create_dataset(dataset)  # API request

    def create_table(self, schema, dataset_id=None, table_id=None, partitioning_field=None, clustering_fields=[], require_partition_filter=False):
        dataset_id = self.__dataset_id(dataset_id)
        table_id = self.__table_id(table_id)

        if self.check_if_table_exists(table_id) is False:
            dataset_ref = self.client.dataset(dataset_id)
            table_ref = dataset_ref.table(table_id)
            table = bigquery.Table(table_ref, schema=schema)
            if partitioning_field is not None:
                if partitioning_field == '_PARTITIONTIME':
                    table.time_partitioning = bigquery.table.TimePartitioning(type_=bigquery.TimePartitioningType.DAY, require_partition_filter=require_partition_filter, field=None)
                else:
                    table.time_partitioning = bigquery.table.TimePartitioning(type_=bigquery.TimePartitioningType.DAY, require_partition_filter=require_partition_filter, field=partitioning_field)
            if len(clustering_fields) > 0:
                table.clustering_fields = clustering_fields
            table = self.client.create_table(table)  # API request
            _ = table.table_id
        else:
            print("Table {} already exists or another error occurred.".format(table_id))

    def check_if_table_exists(self, dataset_id=None, table_id=None):
        dataset_id = self.__dataset_id(dataset_id)
        table_id = self.__table_id(table_id)
        dataset_ref = self.client.dataset(dataset_id)
        dataset = bigquery.Dataset(dataset_ref)
        table_ref = dataset.table(table_id)
        try:
            table = self.client.get_table(table_ref)  # API request
            _ = table.schema
            # If no error, table exists
            table_exists = True
        except:
            table_exists = False
        return table_exists

    def get_schema(self, dataset_id=None, table_id=None):
        dataset_id = self.__dataset_id(dataset_id)
        table_id = self.__table_id(table_id)
        dataset_ref = self.client.dataset(dataset_id)
        dataset = bigquery.Dataset(dataset_ref)
        table_ref = dataset.table(table_id)
        table = self.client.get_table(table_ref) # API request
        return table.schema

    def streaming_insert_single_json(self, data, dataset_id=None, table_id=None):
        dataset_id = self.__dataset_id(dataset_id)
        table_id = self.__table_id(table_id)
        table_ref = self.client.dataset(dataset_id).table(table_id)
        table = self.client.get_table(table_ref)  # API request
        errors = self.client.insert_rows_json(table, [data])  # API request
        return errors

    def run_query(self, query):
        query_job = self.client.query(query)  # API request
        rows = query_job.result()  # Waits for query to finish
        return rows.to_dataframe()



if __name__ == '__main__':

    # With default values: (i. e. if you only work within one dataset)
    bq_handler = BQ(dataset_id='default_dataset_id', table_id='default_table_id')
    # Without defaults:
    # bq_handler = BQ()

    # You can also specify a project_id and a cred_file_path (credential file path) if you need it

    # Creating a new Dataset:
    #bq_handler.create_dataset(dataset_id='test_dataset_id')

    # Creating a new Table:
    from google.cloud import bigquery
    SCHEMA = [
        bigquery.SchemaField('full_name', 'STRING',
                             mode='required', description="Visitor's Name"),
        bigquery.SchemaField('visit_time', 'TIMESTAMP',
                             mode='required', description="Visit Time"),
        bigquery.SchemaField('visit_length', 'INT64',
                             mode='required', description="Length of Visit in Seconds"),
        bigquery.SchemaField('sentiment', 'FLOAT64',
                             mode='required', description="Calculated Happiness Score"),
    ]
    #bq_handler.create_table(schema=SCHEMA, dataset_id='test_dataset_id', table_id='test_table_id')
    # You can also create a table with day partitioning and with clustering:
    #bq_handler.create_table(schema=SCHEMA, dataset_id='test_dataset_id', table_id='test_table_id', partitioning_field='_PARTITIONTIME', require_partition_filter=False, clustering_fields=['visit_time'])
    # _PARTITIONTIME is the default partitioning from BigQuery


    # Checking if a table exists or not:
    #check = bq_handler.check_if_table_exists(dataset_id='test_dataset_id', table_id='test_table_id')
    #print(check)

    # Getting a schema of an existing table:
    #schema = bq_handler.get_schema(dataset_id='test_dataset_id', table_id='test_table_id')
    #print(schema)

    # Streaming a row into an existing BQ table:
    data = {'full_name': 'Max Mustermann', 'visit_time': '2019-07-23 13:45:07.372826 UTC', 'visit_length': 100, 'sentiment': 1.111}
    bq_handler.streaming_insert_single_json(data, dataset_id='test_dataset_id', table_id='test_table_id')

    # Running a query and get results as a dataframe:
    query = '''
    SELECT * FROM `v135-5683-playground-goppold.test_dataset_id.test_table_id`  
    '''
    df = bq_handler.run_query(query)
    print(df)

