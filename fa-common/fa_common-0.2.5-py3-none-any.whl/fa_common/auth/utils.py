from typing import List, Optional

from fastapi import Depends
from fastapi.openapi.models import OAuthFlows
from fastapi.security import OAuth2, SecurityScopes
from jose import JWTError, jwt
from pydantic import ValidationError

from .models import AuthUser
from fa_common import (
    async_get,
    force_async,
    logger as LOG,
    ForbiddenError,
    UnauthorizedError,
    get_settings,
)

oauth2_scheme = OAuth2(
    flows=OAuthFlows(
        implicit={
            "authorizationUrl": get_settings().OAUTH2_AUTH_URL,
            "scopes": {"openid": "", "profile": "", "email": ""},
        }
    )
)


async def get_firebase_token(user: AuthUser) -> str:
    from firebase_admin import auth as fire_auth

    uid = user.sub

    # Potentially add scopes here
    # additional_claims = {
    #     "premiumAccount": True
    # }
    additional_claims: dict = {}
    return force_async(fire_auth.create_custom_token)(uid, additional_claims)


async def get_user_profile(url: str, auth: str) -> AuthUser:
    data = await async_get(url, auth)
    return AuthUser(**data)


def get_token_auth_header(auth: str) -> str:
    """Obtains the Access Token from the Authorization Header
    """
    if not auth:
        raise UnauthorizedError(detail="Authorization header is expected",)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise UnauthorizedError(detail="Authorization header must start with Bearer",)
    elif len(parts) == 1:
        raise UnauthorizedError(detail="Token not found",)
    elif len(parts) > 2:
        raise UnauthorizedError(detail="Authorization header must be Bearer token",)

    token = parts[1]
    return token


async def decode_token(auth: str):
    settings = get_settings()
    token = get_token_auth_header(auth)
    jwks = await async_get(f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json")

    unverified_header = jwt.get_unverified_header(token)
    rsa_key: dict = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=settings.JWT_ALGORITHMS,
                audience=settings.API_AUDIENCE,
                issuer="https://" + settings.AUTH0_DOMAIN + "/",
            )
        except jwt.ExpiredSignatureError:
            raise UnauthorizedError(detail="token is expired",)
        except jwt.JWTClaimsError:
            raise UnauthorizedError(
                detail="incorrect claims, please check the audience and issuer",
            )
        except Exception:
            raise UnauthorizedError(detail="Unable to parse authentication token.",)

        return payload

    raise UnauthorizedError(detail="Unable to find appropriate key",)


async def get_user(payload: dict, token: str) -> Optional[AuthUser]:
    user: Optional[AuthUser] = None
    token_scopes: List[str] = []

    if "permissions" in payload and payload.get("permissions") is not None:
        token_scopes = payload["permissions"]

    if "sub" in payload:
        if (
            "aud" in payload
            and len(payload["aud"]) > 1
            and "userinfo" in payload["aud"][1]
        ):
            user = await get_user_profile(payload["aud"][1], token)
        else:
            user = AuthUser(**payload)

        if len(token_scopes) > 0:
            user.scopes = token_scopes

    return user


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
) -> AuthUser:

    try:
        payload = await decode_token(token)
        user = await get_user(payload, token)

    except (JWTError, ValidationError) as e:
        LOG.error("Could not validate credentials. {}", str(e))
        raise UnauthorizedError(detail="Could not validate credentials.",)

    if not user:
        raise UnauthorizedError(detail="Invalid authentication credentials.",)

    for scope in security_scopes.scopes:
        if scope not in user.scopes:
            raise ForbiddenError(detail="Not enough permissions",)
    return user
