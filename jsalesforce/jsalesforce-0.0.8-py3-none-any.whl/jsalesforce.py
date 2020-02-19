from simple_salesforce import Salesforce
from pprint import pprint
import pandas as pd
from datetime import datetime


def login(username, password, security_token):
    return jSalesforce(
        username=username, password=password, security_token=security_token,
    )


class SalesforceError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class MissingDataError(SalesforceError):
    def __init__(self, keys, data, msg=None):
        self.data = data
        if msg == None:
            msg = f"Missing data for {keys} on the data: \n{data}"
        super().__init__(msg)


class DuplicatesError(SalesforceError):
    def __init__(self, n_items, msg=None):
        self.n_items = n_items
        if msg == None:
            msg = f"There are {n_items} duplicates in salesforce."
        super().__init__(msg)


class jSalesforce(Salesforce):
    def __init__(self, username, password, security_token):
        super().__init__(username, password, security_token)
        self.username = username

    def active_users(self):
        """Returns a list salesforce users that are active, usually the active
        juniors.

        Parameters
        ----------
        sf: Salesforce connector from login function

        Returns
        -------
        list(dict): Returns a list of dictionaries. Each dict represents a user and has the following keys:
            Id, Email, isActive, FirstName, LastName, isActive
        """
        users = self.query(
            "SELECT Id, Email, isActive, FirstName, LastName FROM User WHERE isActive=True"
        )["records"]
        return users

    def user_id(self, email):
        """Returns the salesforce id from the user (usually a junior) with that
        email."""
        users = self.active_users()
        try:
            sf_id = next(user["Id"] for user in users if user["Email"] == email)
        except StopIteration:
            raise SalesforceError(f"No user with email {email} found.")
        return sf_id

    def escape_email(self, email):
        """In Salesforce queries the emails have to be escaped.

        Returns escaped email.
        """
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
            escaped_email = email.replace(c, "\\" + c)
        return escaped_email

    # TODO probably refactor this into smaller useful functions
    def object_with_email(self, email):
        """Get the salesforce id and type from an object with that email as a
        pandas Series. Prioritizes Contacts.

        Parameters
        ----------
        self:
        email: string of an email that has been escaped and trimmed for the salesforce API

        Returns
        -------
        Series: keys are "Type" and "WhoId"

        Raises
        ------
        DuplicatesError: If there are multiple leads/contacts with that email.
        """
        query = f"FIND {{{email}}}"
        results = self.search(query)["searchRecords"]

        types = [res["attributes"]["type"] for res in results]
        if "Contact" in types:
            index = types.index("Contact")
            return pd.Series({"Type": "Contact", "WhoId": results[index]["Id"]})
        if "Lead" in types:
            index = types.index("Lead")
            return pd.Series({"Type": "Lead", "WhoId": results[index]["Id"]})
        return pd.Series({"Type": None, "WhoId": None})

    def add_type_and_id_from_email(self, df):
        """Takes DataFrame with a column "Escaped Email" and adds columns "Type"
        and "WhoId"."""
        email_to_type_and_id = lambda email: self.object_with_email(email)
        concat_df = df["Escaped Email"].apply(email_to_type_and_id)
        return pd.concat([df, concat_df], axis=1)

    def create_lead(self, data):
        """Creates a Lead from a pandas Series. Checks keys and data.

        Parameters
        ----------
        sf:
        data: pandas Series containing at least ['Email', 'FirstName', 'LastName', 'Company', 'OwnerId', 'Funktion__c']

        Returns
        -------
        The result from saleselforce API

        Raises
        ------
        MissingDataErro
        """
        allowed_keys = {
            "Email",
            "FirstName",
            "LastName",
            "Company",
            "Funktion__c",
            "LeadSource",
            "OwnerId",
        }
        required_keys = {
            "Email",
            "FirstName",
            "LastName",
            "Company",
            "Funktion__c",
            "OwnerId",
        }
        data = data.dropna()
        data_keys = set(data.keys())
        missing_keys = required_keys - data_keys
        if len(missing_keys) > 0:
            raise MissingDataError(missing_keys, data)

        not_allowed_keys = data_keys - allowed_keys
        data = data.drop(labels=not_allowed_keys).to_dict()
        data["Email"] = self.escape_email(data["Email"])

        return self.Lead.create(data)

    def types_with_email(self, email):
        """Finds the types of salesforce objects with that email."""
        email = self.escape_email(email)
        q_leads = f"SELECT Id FROM Lead WHERE Email='{email}'"
        q_contacts = f"SELECT Id FROM Contact WHERE Email='{email}'"
        r_leads = self.query(q_leads)["records"]
        r_contacts = self.query(q_contacts)["records"]

        types = {res["attributes"]["type"] for res in r_leads}.union(
            {res["attributes"]["type"] for res in r_contacts}
        )
        return types

    def create_new_leads(self, df):
        """Creates all leads from the DataFrame.

        Parameters
        ----------
        self:
        df: pandas DataFrame with columns = [Company, FirstName, LastName, Funktion__c, Email, Subject, Owner Email, Sales_Aktivit_t__c, ActivityDate, Result]

        Returns
        -------
        DataFrame: If a new Lead got created the column "Result" contains the new id. It also adds the WhoId and the Type to the new Leads

        Raises
        ------
        MissingDataError
        """
        df["OwnerId"] = df["Owner Email"].transform(self.user_id)

        df = df.drop_duplicates(subset=["Email"])
        df["Types"] = df["Email"].transform(self.types_with_email)
        no_object = lambda types: not ("Lead" in types or "Contact" in types)
        no_object = df["Types"].transform(no_object)
        df_new_leads = df[no_object]
        for row in df_new_leads.iterrows():
            data = row[1]
            # TODO handle exception
            try:
                result = self.create_lead(data)
                lead_id = result["id"]
                print(f"Created Lead with id {lead_id}")
                df.at[row[0], "Types"] = {"Lead"}
            except MissingDataError as e:
                raise
        return df

    def create_task(self, data):
        """Creates a Task based on a pandas Series. Checks keys and data.
        Parameters
        ----------
        self:
        data: pandas Series containing at least ['WhoId','Subject','ActivityDate','Status','OwnerId','Sales_Aktivit_t__c']

        Returns
        -------
        The result from salesforce API

        Raises
        ------
        MissingDataError
        """
        allowed_keys = {
            "WhoId",
            "WhatId",
            "Subject",
            "ActivityDate",
            "Status",
            "Description",
            "OwnerId",
            "Sales_Aktivit_t__c",
        }
        required_keys = {
            "WhoId",
            "Subject",
            "ActivityDate",
            "Status",
            "OwnerId",
            "Sales_Aktivit_t__c",
        }
        data = data.dropna()
        data_keys = set(data.keys())
        missing_keys = required_keys - data_keys
        if len(missing_keys) > 0:
            raise MissingDataError(missing_keys, data)

        not_allowed_keys = data_keys - allowed_keys
        data = data.drop(labels=not_allowed_keys).to_dict()

        return self.Task.create(data)

    def lead_id_from_email(self, email):
        email = self.escape_email(email)
        q = f"SELECT Id FROM Lead WHERE Email='{email}'"
        records = self.query(q)["records"]
        return records[0]["Id"]

    def contact_id_from_email(self, email):
        email = self.escape_email(email)
        q = f"SELECT Id FROM Contact WHERE Email='{email}'"
        records = self.query(q)["records"]
        return records[0]["Id"]

    def create_tasks(self, df):
        """Creates all tasks from the DataFrame.

        Parameters
        ----------
        self: Salesforce connectore from login function
        df: DataFrame containing at least the columns ['Email','Subject','ActivityDate','Status','Owner Email','Sales_Aktivit_t__c', 'Result']

        Returns
        -------
        DataFrame: the same DataFrame with the Task id added to the column "Result"

        Raises
        ------
        MissingDataError
        """
        df["OwnerId"] = df["Owner Email"].transform(self.user_id)
        df["Types"] = df["Email"].transform(self.types_with_email)
        print(df["Types"])
        is_contact = df["Types"].map(lambda types: "Contact" in types)
        is_lead = df["Types"].map(lambda types: "Lead" in types)
        df["WhoId"] = df.loc[is_contact, "Email"].transform(self.contact_id_from_email)
        df["WhoId"] = df.loc[is_lead, "Email"].transform(self.lead_id_from_email)
        is_object = ~df["WhoId"].isna()
        has_task = ~df["Status"].isna()

        for row in df[is_object & has_task].iterrows():
            data = row[1]
            # TODO handle exception
            try:
                result = self.create_task(data)
                task_id = result["id"]
                print(f"Tracked Task with id {task_id}")
            except:
                raise
        return df

    def salesforce_datetime(self, python_dt):
        """Converts python datetime to the salesforce format.

        Example: 2014-11-20T14:23:44.000+0000
        """
        return python_dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0000"

    def get_objects_created_after(self, python_dt, object_type):
        """Returns objects of specific type created by the logged in user after
        that time."""
        salesforce_dt = self.salesforce_datetime(python_dt)
        user_id = sf.salesforce_user_id(self.username)
        q = f"SELECT Id FROM {object_type} WHERE CreatedDate>{salesforce_dt} AND CreatedById='{user_id}'"
        return self.query(q)["records"]

    def delete_object(self, salesforce_id, object_type):
        """Deletes salesforce object with that id and that type."""
        delete_function = {"Lead": self.Lead.delete, "Task": self.Task.delete}
        result = delete_function[object_type](salesforce_id)
        return result

    def delete_objects_created_after(self, python_dt, object_type, delete_many=False):
        """Deletes objects of specific type created after some time.

        Protects against mass deletions of more than 25 elements by default.
        Set delete_many=True if you want to skip that protection.
        """
        records = sf.get_objects_created_after(python_dt, object_type)
        if len(records) > 25 and delete_many == False:
            raise DuplicatesError(
                len(records),
                msg=f"You are about to delete {records} items. If that is correct, call the function with delete_many=True",
            )

        for record in records:
            salesforce_id = record["Id"]
            result = sf.delete_object(salesforce_id, object_type)
            # TODO: Use proper logging
            print(
                f"Deleted object with Type {object_type} and id {salesforce_id}. Result:\n{result}"
            )
