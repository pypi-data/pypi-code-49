import json

from billingo_client import BillingoClient

PUBLIC_KEY = 'c0dd15f76fa45b9b7c782b2268611728'
PRIVATE_KEY = '114ba08e933144a25313a887f502168d728183723c6160bfa27242700cf547840b938c7f5c73706a2cd0701852906ed176a1bcbe86787b58fdf551546fd668cd'

client = BillingoClient(PUBLIC_KEY, PRIVATE_KEY)
# print(client.list_invoices())
# print(client.get_invoice(1403140148))
print(client.get_currency(123.75, change_from='USD', change_to='HUF'))
