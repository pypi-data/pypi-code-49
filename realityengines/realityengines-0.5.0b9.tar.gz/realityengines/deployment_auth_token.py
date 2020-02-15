

class DeploymentAuthToken():
    '''

    '''

    def __init__(self, client, authToken=None, projectId=None, createdAt=None):
        self.client = client
        self.id = authToken
        self.auth_token = authToken
        self.project_id = projectId
        self.created_at = createdAt

    def __repr__(self):
        return f"DeploymentAuthToken(auth_token={repr(self.auth_token)}, project_id={repr(self.project_id)}, created_at={repr(self.created_at)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'auth_token': self.auth_token, 'project_id': self.project_id, 'created_at': self.created_at}

    def refresh(self):
        self = self.describe()
        return self
