import urllib
import os
import re
import json
import datetime

import sqlalchemy
from sqlalchemy.orm import Session
import cx_Oracle
import dpath.util
import pandas as pd
import numpy as np


class Connection(object):
    def __init__(
        self, connectionDetails, conDetailsDictPath=None, serverWarnings=False
    ):
        """ Creates a connection to a sql database using SQLAlchemy session

        Currently supports MySQL,  PostgreSQL, SQL Server (MSSQL), and Oracle.

        Args:
            connectionDetails (dict or string): Holds the connection details and can be a dictionary or path to json file
            conDetailsDictPath (string): Defaults to None. Can be used to define the path in the file to the database 
                connection details. The path must be described via /slashed/path ala xpath. The library used is dpath.
                Required when using a file and if the file contains more than just the database connection details.
            serverWarnings (boolean): Defaults to False. Server warnings will be displayed when set to True.
        
        Returns:
            No value
        """

        self.conDetailsDictPath = conDetailsDictPath
        self.connectionDetails = connectionDetails

        self.validateConnectionDetails()

        self.connectionDetails["db"] = self.connectionDetails.get("db", "")

        # MySQL
        if self.connectionDetails["serverType"] == "mysql":

            self.connectionDetails["port"] = self.connectionDetails.get("port", 3306)

            connectionString = "mysql+pymysql://{user}:{pw}@{ip}:{port}/{db}".format(
                **self.connectionDetails
            )

            self.serverType = "mysql"

        # PostgreSQL
        elif self.connectionDetails["serverType"] in ["postgresql", "postgres"]:

            self.connectionDetails["port"] = self.connectionDetails.get("port", 5432)

            connectionString = "postgresql+psycopg2://{user}:{pw}@{ip}:{port}/{db}".format(
                **self.connectionDetails
            )

            self.serverType = "postgresql"

        # MSSQL
        elif self.connectionDetails["serverType"] == "mssql":

            self.connectionDetails["port"] = self.connectionDetails.get("port", 1433)
            self.connectionDetails["odbcDriver"] = self.connectionDetails.get(
                "odbcDriver", "{ODBC Driver 17 for SQL Server}"
            )

            connectionParameters = urllib.parse.quote_plus(
                "DRIVER={odbcDriver};SERVER={ip};DATABASE={db};UID={user};PWD={pw};PORT={port}".format(
                    **self.connectionDetails
                )
            )

            connectionString = "mssql+pyodbc:///?odbc_connect={}".format(
                connectionParameters
            )

            self.serverType = "mssql"

        # Oracle
        elif self.connectionDetails["serverType"] == "oracle":

            self.connectionDetails["port"] = self.connectionDetails.get("port", 1521)
            self.connectionDetails["dsn"] = cx_Oracle.makedsn(
                self.connectionDetails["ip"],
                self.connectionDetails["port"],
                service_name=self.connectionDetails["service"],
            )

            connectionString = "oracle://{user}:{pw}@{dsn}".format(
                **self.connectionDetails
            )

            self.serverType = "oracle"

        else:
            raise Exception(
                "The serverType '{serverType}' is not supported".format(
                    **self.connectionDetails
                )
            )

        engine = sqlalchemy.create_engine(connectionString)
        self.session = sqlalchemy.orm.session.Session(bind=engine)
        self.metadata = sqlalchemy.MetaData(bind=engine)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def validateConnectionDetails(self):
        """Get connection details and perform basic validation

        If a file path was provided, loads the connection details from file into a dictionary.
        Checks that the minimum connection parameters are provided in the dictionary.
        The following parameters are cosidered minimum: serverType, user, pw, and ip.
        Connection parameters that are specific to a server type are not checked.
        
        Args:
            No Args

        Returns:
            No value
        """

        if isinstance(self.connectionDetails, str):
            # If connectionDetails is a string it is assumed that is a filepath which is used to load the connection details.

            connectionDetailsFilePath = self.connectionDetails

            if os.path.isfile(self.connectionDetails):

                filename, filetype = os.path.splitext(connectionDetailsFilePath)

                if filetype == ".json":

                    with open(connectionDetailsFilePath) as f:
                        self.connectionDetails = json.load(f)
                else:
                    raise Exception(
                        "The connection details filetype '{}' is not supported".format(
                            filetype
                        )
                    )
            else:
                raise Exception(
                    "The connection details file specified does not exist ({})".format(
                        connectionDetailsFilePath
                    )
                )

        elif isinstance(self.connectionDetails, dict):
            pass
        else:
            raise Exception(
                "The variable connectionDetails has to be a dictionary or file path but the variable provided is of type {}".format(
                    type(self.connectionDetails)
                )
            )

        if self.conDetailsDictPath is not None:
            self.connectionDetails = dpath.util.get(
                self.connectionDetails, self.conDetailsDictPath
            )

        # Check that the minimum connection parameters are provided
        requiredConnectionValues = ["serverType", "user", "pw", "ip"]
        for v in requiredConnectionValues:
            if v not in self.connectionDetails:
                raise Exception(
                    "No value for key '{}' provided in connection details".format(v)
                )

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def now(self):
        return datetime.datetime.now()

    def query(
        self,
        queryStr,
        commit=False,
        returnType="list",
        queryType=None,
        insertIdField=None,
    ):
        """Execute raw sql query 
        
        Args:
            queryStr (str):
            commit (boolean): Defaults to False. If set to True will use commit command after executing the query.
            returnType (str): Defaults to the value 'list'. Other possible values are 'df' (dataframe) or 'listOfDicts'.
            queryType (str): Defaults to None. Used to set the query type. Valid values are 'insert', 'update', and 'select'.
            insertIdField (str): Defaults to None. Needs to be provided for insert statements for Oracle and PostgreSQL if
                returning the last inserted id is required (will return None if not provided).

        Returns:
            rows (select) or lastRowId (insert): If the query type is select (SQLAlchemy returns rows) a dataframe, list of lists or 
                list of dicts is returned depending on the specified returnType. If the queryType is insert and the database supports 
                the functionallity to return the last inserted id the system will return the id. If neither of these cases is matched
                None is returned.
        """

        # If queryType is not provided determine it based on the first word of the query (works for update, insert, select)
        if queryType is None:
            try:
                queryType = re.split(" |\n", queryStr, 1)[0].lower()
                if queryType not in ("select", "insert", "update"):
                    queryType = None
            except:
                queryType = None

        # Inserts for PostgreSQL and Oracle require a modification to the query to retrief the inserted id (todo Oracle)
        if (
            queryType == "insert"
            and self.serverType in ("postgresql", "oracle")
            and insertIdField
        ):
            if self.serverType == "postgresql":
                queryStr += ' returning "{}"'.format(insertIdField)

        result = self.session.execute(queryStr)

        if commit:
            self.commit()

        if queryType == "insert":

            if self.serverType == "mysql":
                lastRowId = result.lastrowid

            elif self.serverType == "mssql":
                lastRowId = self.session.execute("select scope_identity()").fetchone()[
                    0
                ]

            elif self.serverType in ("postgresql"):  # still to do for 'oracle'
                lastRowId = result.fetchone()[0]

            else:
                lastRowId = None

            return lastRowId

        elif result.returns_rows:
            rows = result.fetchall()
            columns = result.keys()

            if returnType == "list":

                return rows

            elif returnType == "df":

                rows = pd.DataFrame(rows, columns=columns)
                return rows

            elif returnType == "listOfDicts":

                rows = convertToListOfDicts({"columns": columns, "rows": rows})
                return rows

            else:
                raise Exception(
                    "'{}' is an invalid value for the variable returnType.".format(
                        returnType
                    )
                )

        else:
            return None

    def select(self, table, columns, filters={}, returnType="list"):
        """Select statement
        
        Args:
            table (str): Name of table to select from.
            columns (list): List of columns to select values for.
            filters (dict): The keys indicate which columns should be used for filtering and the associated values are
            used as filter criteria. E.g. {'job' : ['developer'], 'skill': ['python', 'pandas', 'sqlalchemy']}
            returnType (str): Defaults to the value 'list'. Other possible values are 'df' (dataframe) or 'listOfDicts'.
            
        Returns:
            rows (): Depending on the query type either a dataframe, list of lists or list of dict.
        """

        for key, val in filters.items():
            if isinstance(val, list) is False:
                filters[key] = [val]

        table = sqlalchemy.Table(table, self.metadata, autoload=True)

        rows = (
            self.session.query(*[table.c[col] for col in columns])
            .filter(
                *[table.c[col].in_([val for val in filters[col]]) for col in filters]
            )
            .all()
        )

        if returnType == "list":

            return rows

        elif returnType == "df":

            rows = pd.DataFrame(rows, columns=columns)
            return rows

        elif returnType == "listOfDicts":

            rows = convertToListOfDicts({"columns": columns, "rows": rows})
            return rows

        else:
            raise Exception(
                "'{}' is an invalid value for the variable returnType.".format(
                    returnType
                )
            )

    def insert(self, table, data, staticValues=None):
        """Used to insert records into table.

        Args:
            table (str): The table to insert into.
            data (list, dict or df): List of records that will be inserted.
                If a list is provided it needs to be a list of dictionaries (column names as keys). E.g. 
                [{'id':'1','name':'frodo','occ':'none'}, {'id':'2','name':'aragon','occ':'king'}]
                If a dictionary is provided it must contain columns (list) and rows (list of lists). E.g.
                {'columns' : ['id', 'name', 'occ'], 'rows' : [[1, 'frodo', 'none'], [2, 'aragon', 'king']]}
                If a pandas dataframe is provided the headers must be the column names. E.g.                                
                id  |  name  | occ 
                ----|--------|------ 
                1   | frodo  | none 
                2   | aragon | king
            staticValues (dict): Defaults to None. This can be used to define values that are the same for each record.
                The key has to match the column name and the value the desired record value. E.g. {'company_name' : 'Google'}

        Returns:
            No value
        """

        insertData = convertToListOfDicts(data)

        if staticValues:
            extendListOfDicts(insertData, staticValues)

        insertTable = sqlalchemy.Table(table, self.metadata, autoload=True)

        if self.serverType == "oracle":
            self.session.execute(insertTable.insert(), insertData)
        else:
            self.session.execute(insertTable.insert().values(insertData))

    def update(self, table, data, setColumns, whereColumns, staticSetValues=None):
        """Used to update records for one table.

        When columns that are used in the where clause (whereColumns) are not indexed the update will take significantly longer.

        Args:
            table (str): The table to update.
            data (list, dict or df): List of records that will be updated.
                If a list is provided it needs to be a list of dictionaries (column names as keys). E.g. 
                [{'id':'1','name':'frodo','occ':'none'}, {'id':'2','name':'aragon','occ':'king'}]
                If a dictionary is provided it must contain columns (list) and rows (list of lists). E.g.
                {'columns' : ['id', 'name', 'occ'], 'rows' : [[1, 'frodo', 'none'], [2, 'aragon', 'king']]}
                If a pandas dataframe is provided the headers must be the column names. E.g.                                
                id  |  name  | occ 
                ----|--------|------ 
                1   | frodo  | none 
                2   | aragon | king
            setColumns (list): List of columns that are updated (used in set part of SQL statement)
            whereColumns (list): List of columns that are used to identify the records to update (used in where clause of SQL statement)
            staticSetValues (dict): Defaults to None. This can be used to define values that are the same for each record.
                The key has to match the column name and the value the desired record value. E.g. {'company_name' : 'Google'}

        Returns:
            No value
        """

        updateData = convertToListOfDicts(data)

        if staticSetValues:
            extendListOfDicts(updateData, staticSetValues)

        updateData = sanitizeColumnNames(updateData, setColumns + whereColumns)

        updateTable = sqlalchemy.Table(table, self.metadata, autoload=True)

        # Solution from stackoverflow.com/questions/48096902
        stmt = (
            updateTable.update()
            .where(
                sqlalchemy.and_(
                    *[
                        updateTable.c[col] == sqlalchemy.bindparam("b_" + col)
                        for col in whereColumns
                    ]
                )
            )
            .values({col: sqlalchemy.bindparam("b_" + col) for col in setColumns})
        )

        self.session.execute(stmt, updateData)

    def upsert(
        self,
        table,
        data,
        keyColumns,
        nonInsertColumns=None,
        staticUpdateValues=None,
        staticInsertValues=None,
    ):
        """Used to upsert records for one table.

        Compares the values of the provided records (data) to the values currently stored in the table.
        Updates records that exists in the table if at least one value is different.
        Inserts a new record if no record is found using the provided keys.
        When comparing the new data to the current data in the table the static values are not considered.

        Args:
            table (str): The table to perform upsert on.
            data (list, dict or df): List of records that will be upserted (updated or insered).
                If a list is provided it needs to be a list of dictionaries (column names as keys). E.g. 
                [{'id':'1','name':'frodo','occ':'none'}, {'id':'2','name':'aragon','occ':'king'}]
                If a dictionary is provided it must contain columns (list) and rows (list of lists). E.g.
                {'columns' : ['id', 'name', 'occ'], 'rows' : [[1, 'frodo', 'none'], [2, 'aragon', 'king']]}
                If a pandas dataframe is provided the headers must be the column names. E.g.                                
                id  |  name  | occ 
                ----|--------|------
                1   | frodo  | none 
                2   | aragon | king
            keyColumns (list): List of columns that are used to uniquely identify a record for the upsert.
                These columns don't have to be actual keys in the database.
            nonInsertColumns (list): Defaults to None. List of columns that will not be inserted for new records.
            staticUpdateValues (dict): Defaults to None. This can be used to define values that are the same for each record.
                The key has to match the column name and the value the desired record value. E.g. {'company_name' : 'Google'}
                Will be used for any records that are being updated. Will not be considered when comparing current to new data.
            staticInsertValues (dict): Defaults to None. This can be used to define values that are the same for each record.
                The key has to match the column name and the value the desired record value. E.g. {'company_name' : 'Google'}
                Will be used for any records that are being inserted. Will not be considered when comparing current to new data.

        Returns:
            dataRows (int): Number of records that were provided.
            insertedRows (int): Number of records that were inserted.
            updatedRows (int): Number of records that were updated.

        """

        newData = convertToListOfDicts(data)

        # Assumes that all dictionaries in the list have exactly the same keys
        allColumns = [key for key in newData[0]]

        upsertTable = sqlalchemy.Table(table, self.metadata, autoload=True)

        # Get current records
        if (
            self.serverType in ("postgresql", "mysql", "sqllite")
            and len(keyColumns) > 1
        ):
            # Filter records using tuple of keys (only supported by SQLAlchemy for PostgreSQL, MySQL, and SQLite)
            currentData = (
                self.session.query(*[upsertTable.c[col] for col in allColumns])
                .filter(
                    sqlalchemy.tuple_(*[upsertTable.c[col] for col in keyColumns]).in_(
                        [[row[keyCol] for keyCol in keyColumns] for row in newData]
                    )
                )
                .all()
            )

        else:
            # Filter records using multiple IN statements (one for each key)
            # This seems to run faster for mysql as well
            currentData = (
                self.session.query(*[upsertTable.c[col] for col in allColumns])
                .filter(
                    *[
                        upsertTable.c[col].in_([row[col] for row in newData])
                        for col in keyColumns
                    ]
                )
                .all()
            )

        # Compare current to new records
        insertData = []
        updateData = []

        if len(currentData) > 0:
            currentData = convertToListOfDicts(
                {"columns": allColumns, "rows": currentData}
            )

            # Generate dictionaries using a concatenation of the key values as unique key for each record
            newDataDict = {
                "_".join([str(row[key]) for key in keyColumns]): row for row in newData
            }
            currentDataDict = {
                "_".join([str(row[key]) for key in keyColumns]): row
                for row in currentData
            }

            for key, val in newDataDict.items():
                if key in currentDataDict:
                    if val != currentDataDict[key]:
                        updateData.append(val)
                else:
                    if nonInsertColumns:
                        for key in nonInsertColumns:
                            del val[key]
                    insertData.append(val)

        else:
            if nonInsertColumns:
                for row in newData:
                    for key in nonInsertColumns:
                        del row[key]

            insertData = newData

        # Insert new records
        insertedRows = len(insertData)
        if insertedRows > 0:
            self.insert(table, insertData, staticValues=staticInsertValues)

        # Update existing records
        updatedRows = len(updateData)
        if updatedRows > 0:
            updateColumns = list(set(allColumns) - set(keyColumns))
            self.update(
                table,
                updateData,
                updateColumns,
                keyColumns,
                staticSetValues=staticUpdateValues,
            )

        dataRows = len(data)

        return dataRows, insertedRows, updatedRows


def sanitizeColumnNames(data, keys=None):
    """Add b_ prefix to keys in data (list of dicts)
    
    Args: 
        data (list of dicts): List of records.
        keys (list): Defaults to None.
    
    Returns:
        data (list of dicts): Sanitized data

    """

    if keys is None:
        for row in data:
            for key in row:
                row["b_" + key] = row.pop(key)

    else:
        keys = list(set(keys))

        for row in data:
            for key in keys:
                row["b_" + key] = row.pop(key)

    return data


def convertToListOfDicts(data):
    """Converts the provided data to a list of dictionaries
    
    Args: 
        data (list, dict or df): List of records.
    
    Returns:
        data (list of dicts): Provided data converted to list of dictionaries.

    """

    if isinstance(data, dict):

        columns = data["columns"]
        rows = data["rows"]

        listOfDicts = [dict(zip(columns, values)) for values in rows]

    elif isinstance(data, list):

        listOfDicts = data

    elif isinstance(data, pd.DataFrame):

        # Only reset index if a named index exists
        if len(data.index.names) == 1 and data.index.name is None:
            pass
        else:
            data = data.reset_index()

        # Convert NaN to None. This is required because by default to_dict converts NaN to the string nan.
        data = data.replace({np.nan: None})
        listOfDicts = data.to_dict("records")

    else:
        raise Exception(
            "The provided type for data is not supported ({})".format(
                type(self.connectionDetails)
            )
        )

    return listOfDicts


def extendListOfDicts(data, extendDict):
    """Add key/value set to all dictionaries in list
    
    Args: 
        data (list of dicts): List of dictionaries.
    
    Returns:
        data (list of dicts): Provided data with additional keys/values sets.

    """

    for item in data:
        item.update(extendDict)

    return data
