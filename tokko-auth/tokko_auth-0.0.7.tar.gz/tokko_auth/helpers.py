from typing import Dict, List

from requests.exceptions import ConnectionError, Timeout, HTTPError
from jose.exceptions import JWTError
from requests import Session
from jose import jwt

# App settings
from tokko_auth import settings


from tokko_auth.exceptions import (
    TokenNotFound,
    UnableDecodeToken,
    ClaimsNotFound,
    ProviderHttpError,
    ProviderUnreachable,
    JSONResponseExpected,
    EnvVarNotInitialized,
    MustBeBearerToken,
    MustStartWithBearer,
    ScopesNotFound,
    InsufficientScopes,
)

# Connections Pool
# I think this not has sense at all ...
# I make just one request ¯\_(ツ)_/¯
pool_conns = Session()

# Types
List_or_Str = (List[str], str)


class AuthorizationHelper:
    """Authorization helper"""

    def namespaces(self, token) -> List[str]:
        scopes = self.scopes(token)
        return [s.split(":")[0] for s in scopes]

    def has_namespace(self, namespace, token) -> bool:
        """Checks: "namespace" is in "token".claims.scopes.namespaces"""
        if not namespace:
            return True
        return namespace in self.namespaces(token)

    def has_required_scopes(self, token: str, required_scopes: List_or_Str, require_all=True) -> bool:
        """Scopes validation"""
        scopes = self.scopes(token)
        if not isinstance(required_scopes, (list, tuple)):
            required_scopes = [required_scopes]
        if scopes:
            required_vs_provided = [scope in scopes for scope in required_scopes]
            if require_all and not all(required_vs_provided):
                raise InsufficientScopes
            elif not require_all and not any(required_vs_provided):
                raise InsufficientScopes
            return True
        else:
            raise ScopesNotFound

    def get_token(self, headers: dict) -> str:
        """Get token from "Authorization" header"""
        auth = self.get_authorization_header(headers)
        parts = auth.split()
        if len(parts) == 1 or len(parts) > 2:
            raise MustStartWithBearer
        # Semantic Token validations
        if not parts[0].lower() == "bearer":
            raise MustBeBearerToken
        return parts[1]

    @staticmethod
    def get_authorization_header(headers: dict) -> str:
        """Get "Authorization" header"""
        if not hasattr(headers, "get"):
            raise TokenNotFound
        auth = headers.get("Authorization") or headers.get("tokko_auth")
        # Syntactic Token validations
        if not auth:
            raise TokenNotFound
        return auth

    def scopes(self, token) -> List[str]:
        """Get Scopes list from claims"""
        claims = self.claims(token)
        scopes = claims.get("permissions")
        if scopes:
            return scopes
        raise ScopesNotFound

    @staticmethod
    def claims(token: str) -> Dict:
        """Get token's unverified claims"""
        try:
            unverified_claims = jwt.get_unverified_claims(token)
        except JWTError:
            raise UnableDecodeToken
        if not unverified_claims:
            raise ClaimsNotFound
        return unverified_claims

    @staticmethod
    def user_properties(token: str) -> Dict:
        """Get user info by token"""
        try:
            auth0_domain = settings.AUTH0_DOMAIN
            if not auth0_domain:
                # Blow up!
                raise EnvVarNotInitialized
            res = pool_conns.get(
                f"https://{auth0_domain}/userinfo",
                headers={"Authorization": f"Bearer {token}"},
            )
            res.raise_for_status()
            content_type = res.headers.get("Content-Type")
            if "application/json" not in content_type:
                raise JSONResponseExpected
            return res.json()
        except (ConnectionError, Timeout):
            raise ProviderUnreachable
        except HTTPError:
            raise ProviderHttpError
