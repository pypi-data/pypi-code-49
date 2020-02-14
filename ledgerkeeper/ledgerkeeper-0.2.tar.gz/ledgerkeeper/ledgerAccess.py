from pymongo import MongoClient
from enum import Enum
import click
from datetime import date
from click.testing import CliRunner

class TransactionTypes(Enum):
    APPLY_PAYMENT = 1
    APPLY_INCOME = 2
    MOVE_FUNDS = 3
    BALANCE_BANK = 4


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def mongo_connect(mongodb_url):
    return MongoClient(mongodb_url)

def personal_finance_db():
    return mongo_connect()["PersonalFinance"]

def ledger_collection():
    return personal_finance_db()["ledger"]

def add_ledger_to_mongo(**content):
    document = {
        'date_stamp': content['date_stamp'],
        'transaction_id': content['transaction_id'],
        'description': content['description'],
        'transaction_category': content['transaction_category'],
        'debit': content['debit'],
        'credit': content['credit'],
        'from_account': content['from_account'],
        'from_bucket': content['from_bucket'],
        'to_account': content['to_account'],
        'to_bucket': content['to_bucket'],
        'amount_covered': 0,
        'refunded': 0,
        'notes': content['notes']
    }

    try:
        collection = ledger_collection()

        collection.insert_one(document)
        print("Success")
    except Exception as e:
        raise Exception(f"Unable to add ledger entry: {e}")


@click.group(context_settings=CONTEXT_SETTINGS)
def run():
    pass


@run.command()
@click.argument('transaction_id', type=str)
@click.argument('transaction_category', type=click.Choice([str(x.name) for x in TransactionTypes]))
@click.argument('description', type=str)
@click.argument('credit', type=float)
@click.argument('debit', type=float)
@click.argument('from_account', type=str)
@click.argument('from_bucket', type=str)
@click.argument('to_account', type=str)
@click.argument('to_bucket', type=str)
@click.option('--date_stamp', type=click.DateTime(formats=["%Y-%m-%d"]), default=str(date.today()), help='specify a date for the transaction if it is not today')
@click.option('--notes', default='', type=str, help="used to add detailed comments to the ledger entry")
def add(**kwargs):
    return add_ledger_to_mongo(**kwargs)

@run.command()
def get(**kwargs):
    collection = ledger_collection()

    results = collection.find()

    for result in results:
        print(result)

if __name__ == "__main__":
    run()