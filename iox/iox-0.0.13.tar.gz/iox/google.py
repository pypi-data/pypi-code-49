"""
google.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from hashlib import md5
from glovebox import GloveBox
from googleapiclient.discovery import build
from google.cloud import bigquery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import numpy as np
import os.path
import pandas as pd
import pickle
from privatize import privatize


# Allows data extract from BigQuery database
class BigQuery:
    """
    Connect to BigQuery
    """

    # Privatize class variables
    project_id = privatize(dtype='str', immutable=True)
    credentials = privatize(dtype='str', immutable=True)
    client = privatize(dtype=(None, bigquery.Client))

    # Initialize the instance
    def __init__(self, project_id, credentials='credentials.json'):
        """
        Initialize instance of BigQuery class

        Parameters
        ----------
        project_id : str
            Google project ID
        credentials : str
            Path to Google credentials
        """

        # Save information
        self.project_id = project_id
        self.credentials = credentials
        self.client = None

    # Connection check
    def _connection_check(self):
        """
        Connect if the connection has not already been set up
        """

        if self.client is None:
            self.connect()

    # Connect to client
    def connect(self):
        """
        Start the client connection with BigQuery using :func:`~iox.authenticate`
        """

        # Authenticate credentials
        _credentials = authenticate('https://www.googleapis.com/auth/bigquery', self.credentials)

        # Connect to client and save
        self.client = bigquery.Client(self.project_id, _credentials)

    # TODO add create_table method
    def create_table(self, table):
        pass

    # Delete table in BigQuery
    def delete_table(self, table):
        """
        Delete table in BigQuery

        Parameters
        ----------
        table : str
            Name of table to be deleted
        """

        # Check that the connection is active
        self._connection_check()

        # Delete the table
        self.client.delete_table(table, not_found_ok=True)

    # TODO execute SQL code without intention to return
    def execute(self, sql):
        pass

    # Query database with a file
    def fquery(self, file_name):
        """
        Query database with a file.

        Parameters
        -------
        file_name : str
            Path to file that contains a SQL query.

        Returns
        -------
        pandas.DataFrame
            The results from the query
        """

        # Open file, read in query, and run it
        with open(file_name, 'r') as file_stream:
            sql = file_stream.read()
            return self.query(sql)

    # Query database with a string
    def query(self, sql):
        """
        Query database with a string.

        Parameters
        ----------
        sql : str
            SQL statements to be run.

        Returns
        -------
        pandas.DataFrame
            The results from the query
        """

        # Check that we are connected to BigQuery
        self._connection_check()

        # Run SQL
        return self.client.query(sql).to_dataframe()


# Class for reading & writing to Google Sheets
class GoogleSheet:
    """
    Read and write to Google sheets.
    """

    # Initialize the class instance
    def __init__(self, spreadsheet_id, credentials='credentials.json'):
        self.spreadsheet_id = spreadsheet_id
        self.credentials = credentials
        self.sheet = None

    # Check if we're connected
    def _connection_check(self):
        if self.sheet is None:
            self.connect()

    # Helper function to read
    def _read(self, cell, formula=False):
        # Define parameters
        params = {
            'spreadsheetId': self.spreadsheet_id,
            'range': cell,
        }

        # Read the sheet as text or formulas?
        if not formula:
            params['valueRenderOption'] = 'UNFORMATTED_VALUE'
            params['dateTimeRenderOption'] = 'FORMATTED_STRING'
        else:
            params['valueRenderOption'] = 'FORMULA'

        # Read using API
        result = self.sheet.values().get(**params).execute()

        # Return values
        return result.get('values', [])

    # Write
    def _write(self, cell, values, formula=False):
        # Parameters
        params = {
            'spreadsheetId': self.spreadsheet_id,
            'range': cell,
            'body': {'values': values},
            'valueInputOption': 'USER_ENTERED' if formula else 'RAW',
        }

        # Execute the write
        _ = self.sheet.values().update(**params).execute()

    # Connect
    def connect(self):
        # Authenticate credentials
        _credentials = authenticate('https://www.googleapis.com/auth/spreadsheets', self.credentials)

        # Connect to sheet
        self.sheet = build('sheets', 'v4', credentials=_credentials).spreadsheets()

    def copy(self, cell1, cell2, formula=True):
        # Check that we're connected
        self._connection_check()

        # Read
        values = self._read(cell1, formula=formula)

        # Write to new range
        self._write(cell2, values, formula=formula)

    # Read
    def read(self, cell, header=False):
        # Read
        values = self._read(cell, formula=False)

        # Convert to DataFrame
        df = pd.DataFrame(values)

        # Fix headers?
        if header:
            df = df.rename(columns=df.iloc[0]).drop(df.index[0])

        # Return
        return df

    # Write
    def write(self, cell, values, index=False, header=True):
        """

        Parameters
        ----------
        cell
        values : pd.DataFrame or array-like or singular
        index
        header

        Returns
        -------

        """
        # Convert DataFrame to correct format
        if isinstance(values, pd.DataFrame):
            # Include index if necessary
            if index:
                values = values.copy().reset_index()

            # Include header if necessary
            header_values = []
            if header:
                header_values = [values.columns.values.tolist()]

            # Convert into usable format
            values = header_values + values.iloc[:, :].values.tolist()

        # If list-like, convert to correct format
        elif isinstance(values, (list, tuple, np.ndarray)):
            values = [values]

        # If singular, convert
        elif isinstance(values, (int, bool, str, float)):
            values = [[values]]

        # Write
        self._write(cell, values)


# Authenticate:
def authenticate(endpoint, credentials='credentials.json'):
    """
    Authenticate Google

    Parameters
    ----------
    endpoint : str
        Google scope to authenticate
    credentials : str
        Google credentials

    Returns
    -------
    google.oauth2.credentials.Credentials
        Authenticated credentials
    """

    # Type check
    if not isinstance(endpoint, str):
        raise AttributeError('endpoint must be a string')
    if not isinstance(credentials, str):
        raise AttributeError('credentials must be a string')

    # Check if credentials.json exists
    if not os.path.isfile(credentials):
        raise AttributeError("""
            %s does not exist
            you can create it at any of:
                https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries
                https://developers.google.com/sheets/api/quickstart/python
        """ % credentials)

    # Name our authentication token and place it in tempdir
    token_name = os.path.join(GloveBox('iox-google', persist=True).path, md5(endpoint.encode()).hexdigest() + '.pickle')

    # Dummy for authenticated credentials
    _credentials = None

    # If the token already exists, read in
    if os.path.exists(token_name):
        with open(token_name, 'rb') as token_stream:
            _credentials = pickle.load(token_stream)

    # If there are no valid credentials, generate
    if not _credentials or not _credentials.valid:
        # Simply fresh if possible
        if _credentials and _credentials.expired and _credentials.refresh_token:
            _credentials.refresh(Request())

        # Otherwise, generate
        else:
            # BUGFIX: #1 (https://github.com/LockhartLab/izzy/issues/1)
            flow = InstalledAppFlow.from_client_secrets_file(credentials, [endpoint])
            _credentials = flow.run_local_server()

        # Save the new authenticated credentials
        with open(token_name, 'wb') as token_stream:
            pickle.dump(_credentials, token_stream)

    # Return the authenticated credentials
    return _credentials


# Clean stored credentials
def clean_stored_credentials():
    GloveBox('iox-google').delete()
