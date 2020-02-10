from simple_salesforce import Salesforce
from pprint import pprint
import pandas as pd

# This simple wrapper is necessary, because simple_salesforce doesnt seem to store the email
class jSalesforce(Salesforce):
    def __init__(self, username, password, security_token):
        super().__init__(username, password, security_token)
        self.username = username

    def get_username(self):
        return self.username


def login(username, password, security_token):
    return jSalesforce(
        username=username, password=password, security_token=security_token,
    )


def get_contract_data(sf, hiring_id):
    hiring = sf.Hiring__c.get(hiring_id)
    employee = sf.Employee__c.get(hiring["Employee__c"])
    service = sf.Service__c.get(hiring["Service__c"])

    data = {}
    data["PRENAME"] = employee["Prename__c"]
    data["NAME"] = employee["Name"]
    data["STREET"] = employee["MailingStreet__c"]
    data["POSTAL_CODE"] = employee["MailingPostalCode__c"]
    data["CITY"] = employee["MailingCity__c"]
    data["START"] = hiring["Anstellungsstart__c"]
    data["END"] = hiring["Anstellungsende__c"]
    data["MANAGER"] = service["PM_1__c"]
    data["PRESIDENT"] = "Tassilo Gilgenreiner"

    wage = hiring["InternalPricingPerHour__c"]
    groundwage = wage / 1.0833
    vacation = wage - groundwage
    data["WAGE"] = f"{wage:.2f}"
    data["GROUNDWAGE"] = f"{groundwage:.2f}"
    data["VACATION"] = f"{vacation:.2f}"
    return data


def create_contract(id):
    data = get_contract_data(sf, "a062o00001p3AX9")
    with MailMerge("../word_templates/01a_Arbeitsvertrag.docx") as document:
        document.merge(**data)
        document.write("../output/Arbeitsvertrag {data['PRENAME']} {data['NAME']}.docx")
    pprint(data)


def get_contact_from_email(email):
    contacts = sf.query(
        f"SELECT Id, AccountId, Email FROM Contact WHERE Email='{email}'"
    )["records"]
    if len(contacts) != 1:
        print("Wrong number of contacts with that email found")
    return contacts[0]


def get_lead_from_email(email):
    leads = sf.query(f"SELECT Id, Email FROM Lead WHERE Email='{email}'")["records"]
    if len(leads) != 1:
        print(f"Wrong number of leads with email: {email}. Found {len(leads)}")
    return leads[0]


def get_contact_type(email):
    sf_escape_characters = [
        "?",
        "&",
        "|",
        "!",
        "{",
        "}",
        "[",
        "]",
        "(",
        ")",
        "^",
        "~",
        "*",
        ":",
        "\\",
        '"',
        "'",
        " ",
        "+",
        "-",
    ]
    for c in sf_escape_characters:
        email = email.replace(c, "\\" + c)
    print(f"Lookinf for email: {email}")
    query = f"FIND {{{email}}}"
    results = sf.search(query)["searchRecords"]

    if len(results) >= 2:
        print(f"Too many contacts/ leads with that email: {len(results)}")
    types = [res["attributes"]["type"] for res in results]
    if "Contact" in types:
        return "Contact"
    if "Lead" in types:
        return "Lead"
    return None


def create_task(data):
    """
    data: For example
    {
    'WhoId':'0035700002AcAy6AAF',
    'WhatId':'00120000008F6vJAAS',
    'Subject': 'test',
    'ActivityDate':'2019-11-13',
    'Status':'Abgeschlossen',
    'OwnerId':'0052o000008Ana1',
    'Sales_Aktivit_t__c':'CI: Buchung neue Firma (25)',
    }
    """
    return sf.Task.create(data)


def create_lead(data):
    """
    data: For example
    {
    'Email':'',
    'FirstName':'',
    'LastName': '',
    'Company':'',
    'LeadSource':'',
    'Status':'',
    'OwnerId':'0052o000008Ana1',
    'Funktion__c':'',
    }
    """
    allowed_keys = [
        "Email",
        "FirstName",
        "LastName",
        "Company",
        "LeadSource",
        "Status",
        "OwnerId",
        "Funktion__c",
    ]
    data_keys = data.keys()
    for key in data_keys:
        if key not in allowed_keys:
            del data[key]
    return sf.Lead.create(data)


def create_tasks_from_df(df):
    """
    df: DataFrame with columns:
    'Email',
    'FirstName',
    'LastName',
    'Company',
    'Subject',
    'ActivityDate',
    'OwnerId',
    'Sales_Aktivit_t__c',
    'Funktion__c'
    """
    # clean df
    df = df.astype("str")
    df["Email"] = df["Email"].str.strip()

    responses = []
    for i, row in enumerate(df.iterrows()):
        row = row[1]
        contact_type = get_contact_type(row["Email"])
        print(i)
        print(row)
        print(contact_type)
        data = {}

        if contact_type == "Contact":
            contact = get_contact_from_email(row["Email"])
            print(f"Contact {contact['Email']}")
            data = {
                "WhoId": contact["Id"],
                "WhatId": contact["AccountId"],
                "Subject": row["Subject"],
                "ActivityDate": row["ActivityDate"],
                "Status": "Abgeschlossen",
                "OwnerId": row["OwnerId"],
                "Sales_Aktivit_t__c": row["Sales_Aktivit_t__c"],
            }
        if contact_type == "Lead":
            lead = get_lead_from_email(row["Email"])
            print(f"Lead {lead['Email']}")
            data = {
                "WhoId": lead["Id"],
                "Subject": row["Subject"],
                "ActivityDate": row["ActivityDate"],
                "Status": "Abgeschlossen",
                "OwnerId": row["OwnerId"],
                "Sales_Aktivit_t__c": row["Sales_Aktivit_t__c"],
            }
        if contact_type == None:
            lead_data = {
                "Email": row["Email"],
                "FirstName": row["FirstName"],
                "LastName": row["LastName"],
                "Company": row["Company"],
                "LeadSource": "Sonstiges",
                "Status": "Offen",
                "OwnerId": row["OwnerId"],
                "Funktion__c": row["Funktion__c"],
            }
            lead_id = create_lead(lead_data)["id"]
            print(f"New Lead {row['Email']}")
            data = {
                "WhoId": lead_id,
                "Subject": row["Subject"],
                "ActivityDate": row["ActivityDate"],
                "Status": "Abgeschlossen",
                "OwnerId": row["OwnerId"],
                "Sales_Aktivit_t__c": row["Sales_Aktivit_t__c"],
            }

        res = create_task(data)
        responses.append(res)
    return responses


def update_jwall(df):
    results = []
    for row in abacus_pay.iterrows():
        zlg_datum = row[1]["Zlg-Datum"]
        beleg_nr_pre = str(int(row[0]))[:-2]
        beleg_nr_year = str(int(row[0]))[-2:]
        beleg_nr = f"INV-{beleg_nr_pre}-{beleg_nr_year}"
        contact = sf.Invoices__c.get_by_custom_id("Name", beleg_nr)
        res = sf.Invoices__c.update(contact["Id"], {"Rechnung_bezahlt__c": zlg_datum})
        results.append(res)
        print(res)
    return results


def jwall_df_from_excel(filename):
    """
    filename: example Zahlungen_Stand_2019-11-25.xlsx
    """
    abacus_pay = (
        pd.read_excel(filename)
        .groupby("Beleg-Nr")
        .agg({"Zlg-Datum": "last", "Kurzname": "first", "Betrag": "sum"})
        .astype("str")
    )
    return abacus_pay
