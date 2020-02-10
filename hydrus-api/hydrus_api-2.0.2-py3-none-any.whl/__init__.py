import enum
import io
import json
from typing import List, Optional, Dict, Union

import requests

DEFAULT_API_URL = "http://127.0.0.1:45869/"
HYDRUS_METADATA_ENCODING = "UTF-8"
_AUTHENTICATION_TIMEOUT_CODE = 419


class HydrusAPIException(Exception):
    pass


# noinspection PyShadowingBuiltins
class ConnectionError(HydrusAPIException, requests.ConnectTimeout):
    pass


class APIError(HydrusAPIException):
    def __init__(self, response):
        super().__init__(response.text)
        self.response = response


class MissingParameter(APIError):
    pass


class InsufficientAccess(APIError):
    pass


class ServerError(APIError):
    pass


class Permission(enum.IntEnum):
    ImportURLs = 0
    ImportFiles = 1
    AddTags = 2
    SearchFiles = 3
    ManagePages = 4
    ManageCookies = 5


class URLType(enum.IntEnum):
    PostURL = 0
    FileURL = 2
    GalleryURL = 3
    WatchableURL = 4
    UnknownURL = 5


class ImportStatus(enum.IntEnum):
    Importable = 0
    Success = 1
    Exists = 2
    PreviouslyDeleted = 3
    Failed = 4
    Vetoed = 7


class TagAction(enum.IntEnum):
    Add = 0
    Delete = 1
    Pend = 2
    RescindPending = 3
    Petition = 4
    RescindPetition = 5


class TagStatus(enum.IntEnum):
    Current = 0
    Pending = 1
    Deleted = 2
    Petitioned = 3


class PageType(enum.IntEnum):
    GalleryDownloader = 1
    SimpleDownloader = 2
    HardDriveImport = 3
    Petitions = 5
    FileSearch = 6
    URLDownloader = 7
    Duplicates = 8
    ThreadWatcher = 9
    PageOfPages = 10


# Complex or reused type annotations
_PermissionsType = List[Permission]
_PathOrFileType = Union[str, io.BytesIO]
_CookiesType = List[List[Union[str, int]]]
_ServiceNamesToTagsType = Dict[str, List[str]]
_ServiceNamesToActionToTagsType = Dict[str, Dict[TagAction, List[str]]]
_ServiceNamesToStatusesToTagsType = Dict[str, Dict[TagStatus, List[str]]]
_VerifyAccessKeyResultType = Dict[str, Union[_PermissionsType, str]]
_AddFileResultType = Dict[str, Union[ImportStatus, str]]
_GetTagServicesResultType = Dict[str, List[str]]
_UrlFilesResultType = Dict[str, Union[str, Dict[str, Union[ImportStatus, str]]]]
_GetURLInfoResultType = Dict[str, Union[str, URLType]]
_PagesResultType = Dict[str, Union[str, PageType, bool, List["_PagesResult"]]]
_FlatPagesResultType = List[Dict[str, Union[str, PageType, bool]]]
_PageInfoResultType = Dict[
    str,
    Union[
        str,
        PageType,
        Dict[
            str,
            Dict[
                str, List[Dict[str, Union[str, int, bool, Dict[str, Union[str, int]]]]]
            ],
        ],
        Dict[str, int],
    ],
]
_FileMetadataResultType = List[
    Dict[str, Union[int, str, None, List[str], _ServiceNamesToStatusesToTagsType]]
]


class RawClient:
    VERSION = 11

    _API_VERSION_ROUTE = "/api_version"
    _REQUEST_NEW_PERMISSIONS_ROUTE = "/request_new_permissions"
    _SESSION_KEY_ROUTE = "/session_key"
    _VERIFY_ACCESS_KEY_ROUTE = "/verify_access_key"
    _ADD_FILE_ROUTE = "/add_files/add_file"

    _CLEAN_TAGS_ROUTE = "/add_tags/clean_tags"
    _GET_TAG_SERVICES_ROUTE = "/add_tags/get_tag_services"
    _ADD_TAGS_ROUTE = "/add_tags/add_tags"

    _GET_URL_FILES_ROUTE = "/add_urls/get_url_files"
    _GET_URL_INFO_ROUTE = "/add_urls/get_url_info"
    _ADD_URL_ROUTE = "/add_urls/add_url"
    _ASSOCIATE_URL_ROUTE = "/add_urls/associate_url"

    _GET_COOKIES_ROUTE = "/manage_cookies/get_cookies"
    _SET_COOKIES_ROUTE = "/manage_cookies/set_cookies"

    _GET_PAGES_ROUTE = "/manage_pages/get_pages"
    _GET_PAGE_INFO_ROUTE = "/manage_pages/get_page_info"
    _FOCUS_PAGE_ROUTE = "/manage_pages/focus_page"

    _SEARCH_FILES_ROUTE = "/get_files/search_files"
    _FILE_METADATA_ROUTE = "/get_files/file_metadata"
    _FILE_ROUTE = "/get_files/file"
    _THUMBNAIL_ROUTE = "/get_files/thumbnail"

    def __init__(
        self, access_key: Optional[str] = None, api_url: str = DEFAULT_API_URL,
    ) -> None:
        """
        See https://hydrusnetwork.github.io/hydrus/help/client_api.html for more
        information.
        """

        self._session = requests.session()
        self._access_key = access_key
        self._api_url = api_url.rstrip("/")

    @property
    def api_url(self):
        return self._api_url

    @property
    def access_key(self):
        return self._access_key

    def _api_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        if self._access_key is not None:
            kwargs.setdefault("headers", {}).update(
                {"Hydrus-Client-API-Access-Key": self._access_key}
            )

        try:
            response = self._session.request(method, self._api_url + endpoint, **kwargs)
        except requests.RequestException as error:
            # Re-raise connection and timeout errors as hydrus.ConnectionErrors so these
            # are more easy to handle for client applications
            raise ConnectionError(*error.args)

        try:
            response.raise_for_status()
        except requests.HTTPError:
            if response.status_code == requests.codes.bad_request:
                raise MissingParameter(response)
            elif response.status_code in {
                requests.codes.unauthorized,
                requests.codes.forbidden,
                _AUTHENTICATION_TIMEOUT_CODE,
            }:
                raise InsufficientAccess(response)
            elif response.status_code == requests.codes.server_error:
                raise ServerError(response)
            raise APIError(response)

        return response

    def api_version(self) -> int:
        """
        Gets the current API version. I will increment this every time I alter the API.
        """

        response = self._api_request("GET", self._API_VERSION_ROUTE)
        return response.json()["version"]

    def request_new_permissions(self, name: str, permissions: _PermissionsType) -> str:
        """
        Register a new external program with the client. This requires the 'add from api
        request' mini-dialog under services->review services to be open, otherwise it
        will 403.

        Arguments:
            name: descriptive name of your access
            permissions: A list of numerical permission identifiers you want to
                request
        """

        response = self._api_request(
            "GET",
            self._REQUEST_NEW_PERMISSIONS_ROUTE,
            params={"name": name, "basic_permissions": json.dumps(permissions)},
        )
        return response.json()["access_key"]

    def session_key(self) -> str:
        """Get a new session key."""

        response = self._api_request("GET", self._SESSION_KEY_ROUTE)
        return response.json()["session_key"]

    def verify_access_key(self) -> _VerifyAccessKeyResultType:
        """Check your access key is valid."""

        response = self._api_request("GET", self._VERIFY_ACCESS_KEY_ROUTE)
        return response.json()

    def add_file(self, path_or_file: _PathOrFileType) -> _AddFileResultType:
        """
        Tell the client to import a file.

        Arguments:
            path_or_file: A path to a file or a readable file object
        """

        if isinstance(path_or_file, str):
            response = self._api_request(
                "POST", self._ADD_FILE_ROUTE, json={"path": path_or_file}
            )
        elif isinstance(path_or_file, io.BytesIO):
            response = self._api_request(
                "POST",
                self._ADD_FILE_ROUTE,
                data=path_or_file.read(),
                headers={"Content-Type": "application/octet-stream"},
            )
        else:
            raise ValueError("Value must be file object or path")

        return response.json()

    def clean_tags(self, tags: List[str]) -> List[str]:
        """
        Ask the client about how it will see certain tags.

        Arguments:
            tags: a list of the tags you want cleaned
        """

        response = self._api_request(
            "GET", self._CLEAN_TAGS_ROUTE, params={"tags": json.dumps(tags)}
        )
        return response.json()["tags"]

    def get_tag_services(self) -> _GetTagServicesResultType:
        """Ask the client about its tag services."""

        response = self._api_request("GET", self._GET_TAG_SERVICES_ROUTE)
        return response.json()

    def add_tags(
        self,
        hashes: List[str],
        service_to_tags: Optional[_ServiceNamesToTagsType] = None,
        service_to_action_to_tags: Optional[_ServiceNamesToActionToTagsType] = None,
        add_siblings_and_parents: bool = True,
    ) -> None:
        """
        Make changes to the tags that files have.

        Arguments:
            hashes: a list of SHA256 hashes
            service_to_tags: a dict of service names to lists of tags to be
                'added' to the files
            service_to_action_to_tags: a dict of service names to content update
                actions to lists of tags
            add_siblings_and_parents: an optional boolean, defaulting to true
        """

        if service_to_tags is None and service_to_action_to_tags is None:
            raise RuntimeError(
                "Pass at least one of: service_to_tags, service_to_action_to_tags"
            )

        json_ = {"hashes": hashes, "add_siblings_and_parents": add_siblings_and_parents}
        if service_to_tags:
            json_["service_names_to_tags"] = service_to_tags
        if service_to_action_to_tags:
            json_["service_names_to_actions_to_tags"] = service_to_action_to_tags

        self._api_request("POST", self._ADD_TAGS_ROUTE, json=json_)

    def get_url_files(self, url: str) -> _UrlFilesResultType:
        """
        Ask the client about an URL's files.

        Arguments:
            url: the url you want to ask about
        """

        response = self._api_request(
            "GET", self._GET_URL_FILES_ROUTE, params={"url": url}
        )
        return response.json()

    def get_url_info(self, url: str) -> _GetURLInfoResultType:
        """
        Ask the client for information about a URL.

        Arguments:
            url: the url you want to ask about
        """

        response = self._api_request(
            "GET", self._GET_URL_INFO_ROUTE, params={"url": url}
        )
        return response.json()

    def add_url(
        self,
        url: str,
        page_key: Optional[str] = None,
        page_name: Optional[str] = None,
        show_page: bool = False,
        service_names_to_tags: Optional[_ServiceNamesToTagsType] = None,
    ) -> Dict[str, str]:
        """
        Tell the client to 'import' a URL. This triggers the exact same routine as
        drag-and-dropping a text URL onto the main client window.

        Arguments:
            url: the url you want to add
            page_key: optional page identifier for the page to receive the url
            page_name: optional page name to receive the url
            show_page : optional, defaulting to false, controls whether the UI will
                change pages on add
            service_names_to_tags: optional tags to give to any files imported from this
                url
        """

        if page_key is not None and page_name is not None:
            raise RuntimeError("Pass exactly one of: page_key, page_name")

        json_ = {"url": url, "show_destination_page": show_page}
        if page_key:
            json_["destination_page_key"] = page_key
        if page_name:
            json_["destination_page_name"] = page_name
        if service_names_to_tags:
            json_["service_names_to_tags"] = service_names_to_tags

        response = self._api_request("POST", self._ADD_URL_ROUTE, json=json_)
        return response.json()

    def associate_url(
        self,
        hashes: List[str],
        add: Optional[List[str]] = None,
        delete: Optional[List[str]] = None,
    ) -> None:
        """
        Manage which URLs the client considers to be associated with which files.

        Arguments:
            hashes: an SHA256 hash for a file in 64 characters of hexadecimal
            add: a list of urls you want to associate with the file(s)
            delete: a list of urls you want to disassociate from the file(s)
        """
        if add is None and delete is None:
            raise RuntimeError("Pass at least one of: add, delete")

        json_ = {"hashes": hashes}
        if add:
            json_["urls_to_add"] = add
        if delete:
            json_["urls_to_delete"] = delete

        self._api_request("POST", self._ASSOCIATE_URL_ROUTE, json=json_)

    def get_cookies(self, domain: str) -> _CookiesType:
        """
        Get the cookies for a particular domain.

        Arguments:
            domain
        """
        response = self._api_request(
            "GET", self._GET_COOKIES_ROUTE, params={"domain": domain}
        )
        return response.json()["cookies"]

    def set_cookies(self, cookies: _CookiesType) -> None:
        """
        Set some new cookies for the client. This makes it easier to 'copy' a
        login from a web browser or similar to hydrus if hydrus's login system
        can't handle the site yet.

        Arguments:
            cookies: a list of cookie rows in the same format as returned by
                get_cookies()
        """
        self._api_request("POST", self._SET_COOKIES_ROUTE, json={"cookies": cookies})

    def get_pages(self) -> _PagesResultType:
        """
        Get the page structure of the current UI session.
        """
        response = self._api_request("GET", self._GET_PAGES_ROUTE)
        return response.json()["pages"]

    def get_page_info(self, page_key: str, simple: bool = False) -> _PageInfoResultType:
        """
        Arguments:
            page_key: hexadecimal page_key as stated in /manage_pages/get_pages
            simple: true or false
        """
        response = self._api_request(
            "GET",
            self._GET_PAGE_INFO_ROUTE,
            params={"page_key": page_key, "simple": json.dumps(simple)},
        )
        return response.json()

    def focus_page(self, page_key: str) -> None:
        """
        'Show' a page in the main GUI, making it the current page in view. If it is
        already the current page, no change is made.

        Arguments:
            page_key : the page key for the page you wish to show
        """
        self._api_request("POST", self._FOCUS_PAGE_ROUTE, json={"page_key": page_key})

    def search_files(
        self, tags: List[str], inbox: bool = False, archive: bool = False
    ) -> List[int]:
        """
        Search for the client's files.

        Arguments:
            tags: a list of tags you wish to search for
            inbox: true or false (optional, defaulting to false)
            archive: true or false (optional, defaulting to false)
        """
        response = self._api_request(
            "GET",
            self._SEARCH_FILES_ROUTE,
            params={
                "tags": json.dumps(tags),
                "system_inbox": json.dumps(inbox),
                "system_archive": json.dumps(archive),
            },
        )
        return response.json()["file_ids"]

    def file_metadata(
        self,
        hashes: Optional[List[str]] = None,
        file_ids: Optional[List[int]] = None,
        only_identifiers: bool = False,
    ) -> _FileMetadataResultType:
        """
        Get metadata about files in the client.

        Arguments:
            hashes: a list of hexadecimal SHA256 hashes
            file_ids: a list of numerical file ids
            only_identifiers: true or false (optional, defaulting to false)
        """
        if not bool(hashes) ^ bool(file_ids):
            raise RuntimeError("Pass exactly one of: hashes, file_ids")

        params = {}
        if hashes:
            params["hashes"] = json.dumps(hashes)
        if file_ids:
            params["file_ids"] = json.dumps(file_ids)
        if only_identifiers:
            params["only_return_identifiers"] = json.dumps(only_identifiers)

        response = self._api_request("GET", self._FILE_METADATA_ROUTE, params=params)
        return response.json()["metadata"]

    def get_file(
        self, hash_: Optional[str] = None, file_id: Optional[int] = None
    ) -> requests.Response:
        """
        Get a file.

        Arguments:
            hash_: a hexadecimal SHA256 hash for the file
            file_id: numerical file id for the file
        """
        if not bool(hash_) ^ bool(file_id):
            raise RuntimeError("Pass exactly one of: hash, file_id")

        params: Dict[str, Union[str, int]] = {}
        if hash_:
            params["hash"] = hash_
        elif file_id:
            params["file_id"] = file_id

        return self._api_request("GET", self._FILE_ROUTE, params=params, stream=True)

    def get_thumbnail(
        self, hash_: Optional[str] = None, file_id: Optional[int] = None
    ) -> requests.Response:
        """
        Get a file's thumbnail.

        Arguments:
            hash_: a hexadecimal SHA256 hash for the file
            file_id: numerical file id for the file
        """
        if not bool(hash_) ^ bool(file_id):
            raise RuntimeError("Pass exactly one of: hash, file_id")

        params: Dict[str, Union[str, int]] = {}
        if hash_:
            params["hash"] = hash_
        elif file_id:
            params["file_id"] = file_id

        return self._api_request(
            "GET", self._THUMBNAIL_ROUTE, params=params, stream=True
        )


class Client(RawClient):
    def add_and_tag_files(
        self,
        paths_and_files: List[_PathOrFileType],
        tags: List[str],
        services: Optional[List[str]] = None,
    ) -> List[_AddFileResultType]:
        services = ["my tags"] if services is None else ["my tags"]

        results = []
        hashes = set()
        for path_or_file in paths_and_files:
            result = self.add_file(path_or_file)
            results.append(result)
            if result["status"] != ImportStatus.Failed:
                hash_ = result["hash"]
                hashes.add(hash_)

        self.add_tags(list(hashes), {service: tags for service in set(services)})
        return results

    def get_pages(
        self, flatten: bool = False
    ) -> Union[_PagesResultType, _FlatPagesResultType]:
        """
        Get the page structure of the current UI session.

        Arguments:
            flatten: Collapse the page tree into a list of pages
        """

        tree = super().get_pages()
        if not flatten:
            return tree

        pages = []

        def iterate_tree(page):
            pages.append(page)
            for sub_page in page.get("pages", []):
                iterate_tree(sub_page)

        iterate_tree(tree)
        return pages
