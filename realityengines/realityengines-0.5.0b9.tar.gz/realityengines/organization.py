

class Organization():
    '''

    '''

    def __init__(self, client, organizationId=None, workspace=None, domain=None, name=None, picture=None, discoverable=None, joined=None, createdAt=None):
        self.client = client
        self.id = organizationId
        self.organization_id = organizationId
        self.workspace = workspace
        self.domain = domain
        self.name = name
        self.picture = picture
        self.discoverable = discoverable
        self.joined = joined
        self.created_at = createdAt

    def __repr__(self):
        return f"Organization(organization_id={repr(self.organization_id)}, workspace={repr(self.workspace)}, domain={repr(self.domain)}, name={repr(self.name)}, picture={repr(self.picture)}, discoverable={repr(self.discoverable)}, joined={repr(self.joined)}, created_at={repr(self.created_at)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'organization_id': self.organization_id, 'workspace': self.workspace, 'domain': self.domain, 'name': self.name, 'picture': self.picture, 'discoverable': self.discoverable, 'joined': self.joined, 'created_at': self.created_at}

    def refresh(self):
        self = self.describe()
        return self

    def join(self):
        return self.client.join_organization(self.organization_id)
