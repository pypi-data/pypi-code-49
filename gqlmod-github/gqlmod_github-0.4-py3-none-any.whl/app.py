"""
Utilities for acting as an app and dealing with installations.

This is basically a dramatically reduced v3 REST client focusing just on the app
and installation features.
"""
import contextlib
import json
import re
import time
from urllib.request import urlopen, Request
import urllib.error

import dateutil.parser
import gqlmod
import jwcrypto.jwt
import jwcrypto.jwk


# From https://github.com/psf/requests/blob/f5dacf84468ab7e0631cc61a3f1431a32e3e143c/requests/utils.py#L580-L611
def parse_header_links(value):
    """Return a dict of parsed link headers proxies.

    i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

    """

    replace_chars = " '\""

    for val in re.split(", *<", value):
        try:
            url, params = val.split(";", 1)
        except ValueError:
            url, params = val, ''

        link = {}
        link["url"] = url.strip("<> '\"")

        for param in params.split(";"):
            try:
                key, value = param.split("=")
            except ValueError:
                break

            link[key.strip(replace_chars)] = value.strip(replace_chars)

        yield link


def _build_accept(preview):
    if isinstance(preview, (list, tuple)):
        return ', '.join(
            f"application/vnd.github.{p}+json"
            for p in preview
        )
    elif isinstance(preview, str):
        return f"application/vnd.github.{preview}+json"
    else:
        raise TypeError("Can't handle preview {preview!r}")


def call_rest(method, url, *, body=None, preview=None, bearer=None):
    """
    Performs an API request, in the form of GitHub v3 API.
    """
    # FIXME: Handle API request throttling
    if method == 'GET' and body:
        raise ValueError("Can't send a body in a GET")

    if url.startswith('/'):
        url = f"https://api.github.com{url}"

    headers = {}

    if body:
        data = json.dumps(body).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    else:
        data = None

    if preview:
        headers['Accept'] = _build_accept(preview)

    if bearer:
        headers['Authorization'] = f"Bearer {bearer}"

    req = Request(url, method=method, data=data, headers=headers)

    try:
        resp = urlopen(req)
    except urllib.error.HTTPError as exc:
        print(exc.read())  # FIXME: Actual log
        raise

    data = resp.read()
    if data:
        rbody = json.loads(data.decode('utf-8'))
    else:
        rbody = None

    return resp.getcode(), resp.info(), rbody


def iter_pages(url, *, preview=None, bearer=None):
    """
    Run a request, and follow the "next" URL in the Link header, recursively.

    Note that only GET requests are supported due to the nature of pagination.

    Produces 3-tuples of (code, info, body).
    """
    nextpage = url
    while nextpage:
        code, info, body = call_rest('GET', url, preview=preview, bearer=bearer)
        yield code, info, body
        link_header = info.get('Link', None)
        if not link_header:
            break

        links = {
            link['rel']: link['url']
            for link in parse_header_links(link_header)
            if 'rel' in link
        }

        nextpage = links.get('next', None)


class GithubApp:
    """
    Your Github Application

    Please note: Not thread safe.
    """
    # Lifespan of generated tokens
    LIFESPAN = 10 * 60  # 10min, documented maxmimum

    _token = None
    _expiration = None

    def __init__(self, app_id, pem_data):
        self.app_id = app_id
        self.key = jwcrypto.jwk.JWK.from_pem(pem_data)

    @property
    def token(self):
        """
        Returns the JWT-based App Token for calling GitHub as an application.

        This transparently manages expiration, so call directly for every use.
        (Do not cache.)

        This is per https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/
        """
        now = time.time()
        if self._token is None or self._expiration <= now:
            self._expiration = now + self.LIFESPAN
            jwt = jwcrypto.jwt.JWT(
                header={
                    "alg": "RS256",  # Hard coded
                },
                claims={
                    "iat": int(now),
                    "exp": int(self._expiration),
                    "iss": self.app_id,
                },
            )
            jwt.make_signed_token(self.key)
            self._token = jwt.serialize()

        return self._token

    def get_app(self, slug):
        """
        Get the app information, by slug

        https://developer.github.com/v3/apps/#get-a-single-github-app
        """
        code, headers, body = call_rest(
            'GET', f'/apps/{slug}', bearer=self.token, preview='machine-man-preview'
        )
        assert code == 200
        return body

    def get_this_app(self):
        """
        Get the app information for the current app

        https://developer.github.com/v3/apps/#get-the-authenticated-github-app
        """
        code, headers, body = call_rest(
            'GET', '/app', bearer=self.token, preview='machine-man-preview',
        )
        assert code == 200
        return body

    def iter_installations(self):
        """
        Generate all installations.

        Traverses pagination.

        https://developer.github.com/v3/apps/#list-installations
        """
        for code, info, page in iter_pages('/app/installations', bearer=self.token, preview='machine-man-preview'):
            assert code == 200
            yield from page

    def get_installation(self, installation_id):
        """
        Get an installation, by ID.

        https://developer.github.com/v3/apps/#get-an-installation
        """
        code, headers, body = call_rest(
            'GET', f'/app/installations/{installation_id}',
            bearer=self.token, preview='machine-man-preview',
        )
        assert code == 200
        return body

    def delete_installation(self, installation_id):
        """
        Delete an installation, by ID.

        https://developer.github.com/v3/apps/#delete-an-installation
        """
        code, headers, body = call_rest(
            'DELETE', f'/app/installations/{installation_id}',
            bearer=self.token, preview=['machine-man-preview', 'gambit-preview'],
        )
        assert code == 204

    def make_installation_token(self, installation_id, *, repository_ids=None, permissions=None):
        """
        Produce an installation token.

        repository_ids and permissions may be used to reduce the permissions of
        the token.

        https://developer.github.com/v3/apps/#create-a-new-installation-token
        """
        params = {}
        if repository_ids:
            params['repository_ids'] = repository_ids
        if permissions:
            params['permissions'] = permissions
        code, headers, body = call_rest(
            'POST', f'/app/installations/{installation_id}/access_tokens',
            body=params, bearer=self.token, preview='machine-man-preview',
        )
        assert code == 201
        return body

    def get_org_installation(self, org):
        """
        Get an installation, by organization.

        https://developer.github.com/v3/apps/#get-an-organization-installation
        """
        code, headers, body = call_rest(
            'GET', f'/orgs/{org}/installation',
            bearer=self.token, preview='machine-man-preview',
        )
        assert code == 200
        return body

    def get_repo_installation(self, owner, repo):
        """
        Get an installation, by owner and repository.

        https://developer.github.com/v3/apps/#get-a-repository-installation
        """
        code, headers, body = call_rest(
            'GET', f'/repos/{owner}/{repo}/installation',
            bearer=self.token, preview='machine-man-preview',
        )
        assert code == 200
        return body

    def get_user_installation(self, username):
        """
        Get an installation, by user

        https://developer.github.com/v3/apps/#get-a-user-installation
        """
        code, headers, body = call_rest(
            'GET', f'/users/{username}/installation',
            bearer=self.token, preview='machine-man-preview',
        )
        assert code == 200
        return body

    @staticmethod
    def create_app_from_manifest(code):
        """
        Create a new application from a previously-submitted manifest.

        https://developer.github.com/v3/apps/#create-a-github-app-from-a-manifest
        """
        code, headers, body = call_rest(
            'POST', f'/app-manifests/{code}/conversions',
            preview='fury-preview',
        )
        assert code == 200
        return body

    def token_for_repo(self, owner_or_repo, repo=None, *, repo_id=None, permissions=None):
        """
        ga.token_for_repo("owner/repo") -> str
        ga.token_for_repo("owner", "repo") -> str

        Convenience shortcut to call get_repo_installation() and
        make_installation_token() in one go.

        Returns the token and expiration datetime

        The permissions for the token may be passed in.

        If the repo_id is passed in, the token will be scoped to it.
        """
        if repo is None:
            assert '/' in owner_or_repo
            owner, repo = owner_or_repo.split('/', 1)
        else:
            owner, repo = owner_or_repo, repo

        inst = self.get_repo_installation(owner, repo)

        if repo_id is None:
            repository_ids = None
        else:
            repository_ids = [repo_id]

        token = self.make_installation_token(
            inst['id'], permissions=permissions, repository_ids=repository_ids,
        )

        t = token['token']
        exp = dateutil.parser.isoparse(token['expires_at'])
        return t, exp

    @contextlib.contextmanager
    def for_app(self):
        """
        Convenience shortcut to make this app the current github credentials.
        """
        # FIXME: What if it expires?
        with gqlmod.with_provider('github', token=self.token):
            yield

    @contextlib.contextmanager
    def for_repo(self, *pargs, **kwargs):
        """
        Convenience shortcut to make a repo the current github credentials.

        Passes arguments to token_for_repo()
        """
        # FIXME: What if it expires?
        token, exp = self.token_for_repo(*pargs, **kwargs)
        with gqlmod.with_provider('github', token=token):
            yield

# TODO: Write class for interrogating installations, using an installation token.
