class Bitbucket:

    def __init__(self, api_server_url, workspace_id, username, password):
        self.api_server_url = api_server_url
        self.workspace_id = workspace_id
        self.username = username
        self.password = password
        self.header_content_type_json = {"Content-Type": "application/json"}
        self.credentials = (self.username, self.password)
