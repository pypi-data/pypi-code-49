import os

import pandas as pd
import xlrd

from miniMinio import create_connection, get_single_object_content_bytes, get_all_object_details_in_bucket, \
    get_single_excel_file_content, get_buckets

client = create_connection("localhost:9000", "minioadmin", "minioadmin", secure=False)
print(get_buckets(client))

details = get_all_object_details_in_bucket(client, bucket_name="buckettest", attributes=["object_name"], filter_object=("files"))
print(details)
output = get_single_object_content_bytes(client, "Book1.xlsx" , bucket_name="buckettest")
objection = xlrd.open_workbook(file_contents=output)
print(output)
output = get_single_excel_file_content(client, "BigBook.xlsx", bucket_name="buckettest")
print(output)


client = create_connection("local")
print(get_buckets(client))

client = create_connection("remote")
print(get_buckets(client, os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")))

print(get_all_object_details_in_bucket(client, os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "buckettest")))