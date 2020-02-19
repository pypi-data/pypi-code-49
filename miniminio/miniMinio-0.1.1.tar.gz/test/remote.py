import os

from miniMinio import create_connection, get_buckets

HOSTNAME = os.environ.get("HOSTNAME")
ACCESS = os.environ.get("ACCESS")
SECRET = os.environ.get("SECRET")

client = create_connection(HOSTNAME, ACCESS, SECRET)
print(get_buckets(client))

# details = get_all_object_details_in_bucket(client, "buckettest", ["object_name"], filter_object=("files"))
# print(details)
# output = get_single_object_content_bytes(client, "buckettest", "folder1/file5.txt")
# print(output)
# output = get_single_object_content_bytes(client, "buckettest", "Book1.xlsx")
# objection = xlrd.open_workbook(file_contents=output)
# print(output)
# output = get_single_excel_file_content(client, "buckettest", "Book1.xlsx")
# print(output)
