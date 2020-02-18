from ..utils import soap_body_builder


# Basic library for interfacing with the Salesforce Metadata API
# Currently only implements the necessary calls to retrieve metadata
# If further calls are made functionality should probably be split up under a few child repos
class Metadata:
    _CONNECTION = None
    _HEADERS = {'content-type': 'text/xml', 'SOAPAction': '""'}

    def __init__(self, connection):
        self._CONNECTION = connection
        self._ENDPOINT = self._CONNECTION.CONNECTION_DETAILS['metadata_server_url']
        self.VERSION = self._CONNECTION.VERSION

    def read(self, metadata_type, names):
        body = "".join([
            "<met:readMetadata>",
            "<met:type>" + metadata_type + "</met:type>",
            "<met:fullNames>" + names + "</met:fullNames>",
            "</met:readMetadata>"
        ])
        soap_body = soap_body_builder(self._CONNECTION.CONNECTION_DETAILS['session_id'], body)
        endpoint = self._CONNECTION.CONNECTION_DETAILS['metadata_server_url']
        return self._CONNECTION.send_http_request(endpoint, 'POST', self._HEADERS, body=soap_body.encode('utf-8'))

    ###
    # Three possible ways to make a request for this endpoint LN:13710
    # - List of package names
    # - A list of specific files
    # - Unpackaged a package xml representations
    # Options:
    # - Single package: boolean dictating whether a single package will be created
    #
    # ####
    def retrieve(self, body):
        endpoint = self._CONNECTION.CONNECTION_DETAILS['metadata_server_url']
        soap_body = soap_body_builder(self._CONNECTION.CONNECTION_DETAILS['session_id'], body)
        return self._CONNECTION.send_http_request(endpoint, 'POST', self._HEADERS, body=soap_body.encode('utf-8'))

    def check_retrieve_status(self, retrieve_id):
        endpoint = self._CONNECTION.CONNECTION_DETAILS['metadata_server_url']
        body = ''.join([
            '<met:checkRetrieveStatus>',
            '<met:asyncProcessId>',
            retrieve_id,
            '</met:asyncProcessId>',
            '<includeZip type="xsd:boolean">true</includeZip>',
            '</met:checkRetrieveStatus>'
        ])
        soap_body = soap_body_builder(self._CONNECTION.CONNECTION_DETAILS['session_id'], body)
        return self._CONNECTION.send_http_request(endpoint, 'POST', self._HEADERS, body=soap_body.encode('utf-8'))

    def list_metadata(self, metadata_queries):
        endpoint = self._CONNECTION.CONNECTION_DETAILS['metadata_server_url']
        retrieve_query_template = ''.join([
            '<met:queries>',
            '<folder>{}</folder>',
            '<type>{}</type>',
            '</met:queries>'
        ])
        list_metadata_request_template = ''.join([
            '<met:listMetadata>',
            '{}'
            '<met:asOfVersion>{}</met:asOfVersion>',
            '</met:listMetadata>',
        ])
        retrieve_query = ''
        for query in metadata_queries:
            folder_name = query['folder']
            meta_type = query['name']
            retrieve_query += retrieve_query_template.format(folder_name, meta_type)
        list_metadata_request = list_metadata_request_template.format(retrieve_query, self.VERSION)
        print(list_metadata_request)
        soap_body = soap_body_builder(self._CONNECTION.CONNECTION_DETAILS['session_id'], list_metadata_request)
        return self._CONNECTION.send_http_request(endpoint, 'POST', self._HEADERS, body=soap_body.encode('utf-8'))

    def describe_metadata(self):
        describe_metadata_template = ''.join([
            '<met:describeMetadata>',
            '<met:asOfVersion>{}</met:asOfVersion>'
            '</met:describeMetadata>'
        ]).format(self.VERSION)
        print(describe_metadata_template)
        soap_body = soap_body_builder(self._CONNECTION.CONNECTION_DETAILS['session_id'], describe_metadata_template)
        return self._CONNECTION.send_http_request(self._ENDPOINT, 'POST', self._HEADERS, body=soap_body.encode('utf-8'))

    def describe_value_type(self, value_type_name):
        describe_value_type_template = ''.join([
            '<met:describeValueType>',
            '<met:type>{}</met:type>',
            '</met:describeValueType>'
        ])
        describe_value_type_request = describe_value_type_template.format(value_type_name)
        soap_body = soap_body_builder(self._CONNECTION.CONNECTION_DETAILS['session_id'], describe_value_type_request)
        return self._CONNECTION.send_http_request(self._ENDPOINT, 'POST', self._HEADERS, body=soap_body.encode('utf-8'))
