'''
API Paths
'''
DEFAULT_HOST = "https://streamsql.io"
RESOURCE_PATH = '/api/resource'
TRANSFORM_PATH = '/api/transform'
STATUS_PATH = TRANSFORM_PATH + '/status'
INGEST_SINGLE = '/api/send/single'
INGEST_BATCH = '/api/send/batch'
GET_TABLE = '/api/get'

'''
APIKEY Header
'''
APIKEY_HEADER = 'X-StreamSQL-Key'

'''
Patterns
'''
RE_TABLE_NAME = '^[a-zA-Z0-9]+$'
RE_ALIAS_NAME = RE_TABLE_NAME
RE_RESOURCE_NAME = RE_TABLE_NAME
RE_TRANSFORM_NAME = RE_TABLE_NAME
RE_API_KEY = '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'

'''
TYPES
'''
SQL_TYPES = [
    "STRING",
    "BOOLEAN",
    "BYTE",
    "SHORT",
    "INT",
    "LONG",
    "FLOAT",
    "DOUBLE",
    "ROW",
    "DECIMAL",
    "SQL_DATE",
    "SQL_TIME",
    "SQL_TIMESTAMP"
]

'''
Resource Types
'''
STREAM_RESOURCE = 'STREAM_RESOURCE'
LOOKUP_RESOURCE = 'LOOKUP_RESOURCE'

RESOURCE_TYPES = [
    STREAM_RESOURCE,
    LOOKUP_RESOURCE
]

'''
Ingestion Formats
'''
JSON = 'JSON'

FORMAT_TYPES = [
    JSON
]
