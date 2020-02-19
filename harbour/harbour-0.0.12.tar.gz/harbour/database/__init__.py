import boto3
import json
import pymysql

from botocore.exceptions import ClientError
from harbour.database.table import Table

class Database:

    DATABASE_MAP = {
        'mysql': pymysql.connect,
    }

    def __init__(self, engine, alias, user):

        # Default parameters
        self.engine = engine
        self.alias = alias
        self.user = user

        self.credentials = None

        # Default resources
        self.client = boto3.client('secretsmanager')

    def get_connection(self):
        """Gets the credentials stored in AWS Secrets manager"""

        try:

            # Requests secrets manager for the credentials
            response = self.client.get_secret_value(
                SecretId="{}/{}/{}".format(
                    self.engine,
                    self.alias,
                    self.user
                )
            )

        except ClientError as exc:

            code = exc.response['Error']['Code']

            messages = {

                # Secrets Manager can't decrypt the protected secret text using
                # the provided KMS key.
                'DecryptionFailureException': 'Failed to decrypt the secret',
                'InternalServiceErrorException': 'Internal server error',
                'InvalidParameterException': 'Invalid parameter',
                'InvalidRequestException': 'Invalid request',
                'ResourceNotFoundException': 'Resource not found.',
                'AccessDeniedException': 'Access denied',

            }

            # Change this to logging
            print(messages.get(code))

            raise exc

        else:

            # Parses the secret
            secret = json.loads(response['SecretString'])

            # Stores the credentials
            self.credentials = {
                'host': secret['host'],
                'user': secret['username'],
                'password': secret['password'],
                'db': secret['dbname'],
                'port': int(secret['port']),
            }

            # Sets the SSDictCursor from MySQL connections
            if self.engine == 'mysql':
                self.credentials['cursorclass'] = pymysql.cursors.SSDictCursor

            # Builds the connection class, connection object and cursor object
            connect = self.DATABASE_MAP.get(self.engine)

            # Connects to the database and creates a cursor
            self.conn = connect(**self.credentials)

            self.curs = self.conn.cursor()

            return self.conn, self.curs

    def table(self, table, *args, **kwargs):
        """Returns a Table object with the Database object injected"""

        if self.credentials is None:
            self.get_connection()

        return Table(self, table)
