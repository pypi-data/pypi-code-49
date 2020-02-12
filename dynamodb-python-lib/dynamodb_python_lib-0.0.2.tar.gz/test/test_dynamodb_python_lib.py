import unittest

from dynamodb_python_lib.proxy import Proxy


class Testing(unittest.TestCase):
    def test_get_instance(self):
        result = Proxy.get_instance()
        self.assertEqual(Proxy, type(result))
        self.assertEqual("cpnlu_UnderstandingData", result._Proxy__dynamo_table._name)

    def test_create_dynamo_db_query(self):
        query_dict = {
            "index": "intent",
            "intent": "amenities",
            "product": ["flight", "lodging"],
            "sentiment": ["positive"]
        }
        dynamo_db_query = Proxy.create_dynamo_db_query(query_dict)

        index_name = "intent-index"
        self.assertEqual(index_name, dynamo_db_query['IndexName'])

        key_condition_name = "intent"
        key_condition_value = "AMENITIES"
        self.assertEqual(key_condition_name, dynamo_db_query['KeyConditionExpression']._values[0].name)
        self.assertEqual(key_condition_value, dynamo_db_query['KeyConditionExpression']._values[1])

        filter_column_count = 2
        self.assertEqual(filter_column_count, len(dynamo_db_query['FilterExpression']._values))


if __name__ == '__main__':
    unittest.main()
