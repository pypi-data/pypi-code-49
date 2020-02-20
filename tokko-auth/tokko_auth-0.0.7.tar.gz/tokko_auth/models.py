from typing import Any, Callable, Dict
import json

from arrow import get as _


def value_as_callable(value) -> Callable:
    def func():
        return value

    return func


class MemoryModel:
    def __init__(self, **raw_data):
        self.__data__ = raw_data
        self.load(**raw_data)

    def load(self, **raw_data):
        for m, value in raw_data.items():
            setattr(self, f"resolve_{m}", value_as_callable(value))

    def get_resolvers(self) -> Dict:
        _resolvers = {}
        for method in dir(self):
            if method.startswith("resolve_"):
                field_name = method.replace("resolve_", "")
                _resolvers.update({field_name: getattr(self, method)})
        return _resolvers

    def get_field_resolver(self, field_name) -> Callable:
        resolvers = self.get_resolvers()
        try:
            return resolvers[field_name]
        except KeyError:
            raise AttributeError(f'has not method "{field_name}"')

    def __getattr__(self, item) -> Any:
        field_resolver = self.get_field_resolver(item)
        return field_resolver()

    def __str__(self) -> str:
        # TODO: resolve -> Complexity too high!
        fields = {
            name: func() if not isinstance(func, type(self)) else f"{func()}"
            for name, func in self.get_resolvers().items()
        }
        return json.dumps(fields)


class Profile(MemoryModel):
    """User profile model"""


class User(MemoryModel):
    """User memory model"""

    scopes: list = None
    token: str = None
    is_anonymous: bool = True
    has_all_api_scopes: bool = None
    token_expire_at: str = None
    token_created_at: str = None
    profile: dict = None

    def resolve_has_all_api_scopes(self) -> bool:
        required_als = getattr(self, "api_level_required_scopes", [])
        if not required_als:
            return True
        scopes = self.resolve_scopes()
        return required_als in scopes

    def resolve_token_expire_at(self) -> (str, None):
        """Parse token expiration date"""
        claims = self.resolve_claims()
        if claims:
            expiration_date = claims.get("exp")
            if expiration_date:
                return _(expiration_date).format("YYYY-MM-DD HH:mm:ss")
        return self.token_expire_at

    def resolve_token_created_at(self) -> (str, None):
        """Parse token creation date"""
        claims = self.resolve_claims()
        if claims:
            expiration_date = claims.get("iat")
            if expiration_date:
                return _(expiration_date).format("YYYY-MM-DD HH:mm:ss")
        return None

    def resolve_scopes(self) -> list:
        """Get token scopes"""
        claims = getattr(self, "claims", {})
        scopes = claims.get("scope", "")
        return scopes.split(",") if scopes else []

    def resolve_is_anonymous(self) -> list:
        """Is anonymous session"""
        return self.resolve_token() is None

    def resolve_profile(self) -> Profile:
        if self.profile:
            return Profile(**self.profile)
