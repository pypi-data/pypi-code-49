from .organization import Organization


class User():
    '''

    '''

    def __init__(self, client, userId=None, userHandle=None, name=None, email=None, picture=None, emailValidated=None, admin=None, createdAt=None, organization={}):
        self.client = client
        self.id = userId
        self.user_id = userId
        self.user_handle = userHandle
        self.name = name
        self.email = email
        self.picture = picture
        self.email_validated = emailValidated
        self.admin = admin
        self.created_at = createdAt
        self.organization = Organization(
            client, **organization) if organization else None

    def __repr__(self):
        return f"User(user_id={repr(self.user_id)}, user_handle={repr(self.user_handle)}, name={repr(self.name)}, email={repr(self.email)}, picture={repr(self.picture)}, email_validated={repr(self.email_validated)}, admin={repr(self.admin)}, created_at={repr(self.created_at)}, organization={repr(self.organization)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'user_id': self.user_id, 'user_handle': self.user_handle, 'name': self.name, 'email': self.email, 'picture': self.picture, 'email_validated': self.email_validated, 'admin': self.admin, 'created_at': self.created_at, 'organization': self.organization.to_dict() if self.organization else None}

    def refresh(self):
        self = self.describe()
        return self

    def add_organization_admin(self):
        return self.client.add_organization_admin(self.user_id)

    def remove_from_organization(self):
        return self.client.remove_user_from_organization(self.user_id)
