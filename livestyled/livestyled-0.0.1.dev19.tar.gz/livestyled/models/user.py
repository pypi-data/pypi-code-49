class User:
    def __init__(
            self,
            id: int or None,
            email: str or None,
            auth_type: str or None
    ):
        self.id = id
        self.email = email
        self.auth_type = auth_type

    @classmethod
    def create_new(
            cls,
            email: str,
            auth_type: str
    ):
        return User(
            id=None,
            email=email,
            auth_type=auth_type
        )

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            email=None,
            auth_type=None
        )

    def diff(self, other):
        differences = {}
        fields = (
            'email', 'auth_type'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences


class UserSSO:
    def __init__(
            self,
            id,
            user_id,
            access_token,
            refresh_token,
            expires,
            sub
    ):
        self.id = id
        self.user_id = user_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires = expires
        self.sub = sub
        self._user = User.placeholder(user_id)

    @classmethod
    def create_new(
            cls,
            user,
            access_token,
            refresh_token,
            expires,
            sub
    ):
        user_sso = UserSSO(
            id=None,
            user_id=None,
            access_token=access_token,
            refresh_token=refresh_token,
            expires=expires,
            sub=sub
        )
        user_sso._user = user

    def diff(self, other):
        differences = {}
        fields = (
            'access_token', 'refresh_token', 'expires', 'sub', 'user_id'
        )
        for field in fields:
            if getattr(self, field) != getattr(other, field):
                differences[field] = getattr(self, field)
        return differences
