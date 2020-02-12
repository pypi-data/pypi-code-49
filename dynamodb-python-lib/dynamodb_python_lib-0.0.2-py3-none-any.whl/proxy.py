import sys
from datetime import datetime

import boto3
import pandas as pd
from boto3.dynamodb.conditions import Key, Attr


class Proxy:
    __instance = None
    __aws_region = ""

    __dynamo_resource = None
    __dynamo_table = None

    @staticmethod
    def get_instance(table_name: str = "cpnlu_UnderstandingData",
                     aws_region: str = "us-west-2",
                     localhost_url: str = None):
        if Proxy.__instance is None:
            Proxy(table_name, aws_region, localhost_url)
        return Proxy.__instance

    def __init__(self, table_name, aws_region, localhost_url):
        self.__dynamo_resource = boto3.resource(
            "dynamodb",
            region_name=aws_region,
            endpoint_url=localhost_url)
        self.__dynamo_table = self.__dynamo_resource.Table(table_name)
        Proxy.__instance = self

    def query(self,
              query_params: dict,
              ready_only: bool = True,
              dataframe_output: bool = True):
        dynamo_db_query = self.create_dynamo_db_query(query_params, ready_only)

        try:
            response = self.__dynamo_table.query(**dynamo_db_query)
            items = response["Items"]

            while "LastEvaluatedKey" in response:
                dynamo_db_query["ExclusiveStartKey"] = response["LastEvaluatedKey"]
                response = self.__dynamo_table.query(**dynamo_db_query)
                items.extend(response["Items"])

        except Exception as e:
            print("Error retrieving data from DynamoDB. ", e)
            sys.exit(1)

        if dataframe_output:
            return self.create_dataframe(items)
        else:
            return items

    @classmethod
    def create_dynamo_db_query(cls, query_params: dict, ready_only: bool = True):
        if "index" not in query_params:
            raise KeyError("Missing 'index' key in query parameters.")

        if query_params["index"] not in query_params:
            raise KeyError("Missing '{}' key/value mapping to the selected index.".format(query_params["index"]))

        mapped_query_params = {}
        fields_with_caps_values = ["product", "intent"]

        # Build IndexName
        query_index = query_params["index"]
        mapped_query_params["IndexName"] = "{}-index".format(query_index)
        query_params.pop("index")

        # Build KeyConditionExpression
        query_index_value = query_params[query_index]
        if query_index in fields_with_caps_values:
            query_index_value = query_index_value.upper()
        mapped_query_params["KeyConditionExpression"] = Key(query_index).eq(query_index_value)
        query_params.pop(query_index)

        # if ready_only, insert additional filter to constrain to rows with status=ready
        if ready_only:
            query_params["status"] = ["ready"]

        # Build FilterExpression
        for field_name in query_params:
            field_values = query_params[field_name]
            filter_attribute = None
            for field_value in field_values:
                if field_name in fields_with_caps_values:
                    field_value = field_value.upper()

                if filter_attribute is None:
                    filter_attribute = Attr(field_name).eq(field_value)
                else:
                    # OR condition for all values within the same field_name
                    filter_attribute = filter_attribute | Attr(field_name).eq(field_value)

            if "FilterExpression" not in mapped_query_params:
                mapped_query_params["FilterExpression"] = filter_attribute
            else:
                # AND condition for each field_name
                mapped_query_params["FilterExpression"] = mapped_query_params["FilterExpression"] & filter_attribute

        return mapped_query_params

    @classmethod
    def create_dataframe(cls, source_data: list):
        """
        Explode values from nested json to new top-level fields
        :param source_data:
        :return: dataframe
        """
        for i, row in enumerate(source_data):
            nested_keys = []
            for key, value in row.items():
                if type(value) == dict:
                    nested_keys.append(key)
            for nested_key in nested_keys:
                nested_dict = row[nested_key]
                for key, value in nested_dict.items():
                    top_level_key = "{}|{}".format(nested_key, key)
                    source_data[i][top_level_key] = value
                source_data[i].pop(nested_key, None)  # should not be in innermost loop
        return pd.DataFrame(source_data)

    def insert(self, record: dict):
        """
        Check if an utterance is exist in the DB
            Yes, increment record frequency
            No, insert a new record to DB
        """
        if "utterance" in record and "locale" in record:
            query_dict = {
                "index": "locale",
                "locale": record["locale"],
                "utterance": [record["utterance"]]
            }
        else:
            raise ValueError("An input record must have locale and utterance.")

        items = self.query(query_dict, ready_only=False, dataframe_output=False)

        date_time_now = datetime.now()
        if len(items) == 0:
            # insert a new record
            if record["data_id"] is None or len(record["data_id"]) < 22:
                record["data_id"] = date_time_now.strftime("d_%Y%m%d%H%M%S%f")
            record["frequency"] = 1
            record["status"] = "new"
            record["loaded_datetime"] = date_time_now.strftime("%Y%m%dT%H%M00")
            record["updated_datetime"] = date_time_now.strftime("%Y%m%dT%H%M00")
        else:
            # update frequency of existing record
            record = items[0]
            if "frequency" in record:
                record["frequency"] = int(record["frequency"]) + 1
            else:
                record["frequency"] = 2
            record["updated_datetime"] = date_time_now.strftime("%Y%m%dT%H%M00")

        self.put_item(record)

    def insert_to_new_db(self, record: dict):
        """
            Use this method to insert a record to DB without checking an existing row
        """
        date_time_now = datetime.now()

        if record["data_id"] is None or len(record["data_id"]) < 22:
            record["data_id"] = date_time_now.strftime("d_%Y%m%d%H%M%S%f")
        record["frequency"] = 1
        record["loaded_datetime"] = date_time_now.strftime("%Y%m%dT%H%M00")
        record["updated_datetime"] = date_time_now.strftime("%Y%m%dT%H%M00")

        self.put_item(record)

    def update(self, record: dict):
        """
        Check if a record is exist in the DB using locale with data_id or utterance
            Yes, update the record
            No, raise an exception
        """
        if "data_id" in record and "locale" in record:
            query_dict = {
                "index": "locale",
                "locale": record["locale"],
                "data_id": [record["data_id"]]
            }
        elif "utterance" in record and "locale" in record:
            query_dict = {
                "index": "locale",
                "locale": record["locale"],
                "utterance": [record["utterance"]]
            }
        else:
            raise ValueError("An input record must have locale with data_id or utterance.")

        items = self.query(query_dict, ready_only=False, dataframe_output=False)

        if len(items) == 0:
            raise ResourceWarning("No record found, nothing to be updated.")
        else:
            # TODO: Once we have a data processing story the status will be changed accordingly
            record["updated_datetime"] = datetime.now().strftime("%Y%m%dT%H%M00")

        self.put_item(record)

    def put_item(self, record):
        try:
            self.__dynamo_table.put_item(Item=record)
        except Exception as e:
            print("Error insert data to DynamoDB. ", e)
            raise e
