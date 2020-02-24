import sys

from billingo_client import BillingoClient

PUBLIC_KEY = sys.argv[1]
PRIVATE_KEY = sys.argv[2]

client = BillingoClient(PUBLIC_KEY, PRIVATE_KEY)
# print(client.list_invoices())
# print(client.get_invoice(1403140148))
print(client.get_currency(123.75, change_from='USD', change_to='HUF'))
