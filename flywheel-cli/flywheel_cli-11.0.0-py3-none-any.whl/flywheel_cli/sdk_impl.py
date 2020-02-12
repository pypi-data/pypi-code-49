"""Provides flywheel-sdk implementations of common abstract classes"""
import copy
import json
import logging
import os
import sys
import time
from urllib.parse import urlparse

import flywheel
import requests

from .importers import ContainerResolver, Uploader
from .util import perror, pluralize, FLYWHEEL_USER_HOME, get_cli_version


CONFIG_PATH = os.path.join(FLYWHEEL_USER_HOME, '.config/flywheel/user.json')
CONFIG = None

TICKETED_UPLOAD_PATH = '/{ContainerType}/{ContainerId}/files'

log = logging.getLogger(__name__)

def status(*args):  # pylint: disable=unused-argument
    """Login status check"""
    fw = create_flywheel_client(require=False)
    if not fw:
        perror('You are not currently logged in.')
        perror('Try `fw login` to login to Flywheel.')
        sys.exit(1)

    try:
        login_info = get_login_info(fw)

        # Print out status and site
        host_url = fw.api_client.configuration.host
        hostname = urlparse(host_url).hostname

    except (flywheel.rest.ApiException, ValueError) as exc:
        perror(f'{exc}\n')
        perror('Could not authenticate - are you sure your API key is up to date?')
        perror('Try `fw login` to login to Flywheel.')
        sys.exit(1)

    return login_info.label, hostname


class LoginInfo:
    """Log info class"""
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.user = None
        self.device = None
        self.is_device = False
        self.root = False
        self.label = None


def load_config():
    """Load config from file"""
    global CONFIG  # pylint: disable=global-statement
    if CONFIG is None:
        path = os.path.expanduser(CONFIG_PATH)
        try:
            with open(path, 'r') as f:
                CONFIG = json.load(f)
        except (IOError, json.decoder.JSONDecodeError):
            CONFIG = {}
    return CONFIG


def create_flywheel_client(require=True):
    """Create flywheel client"""
    config = load_config()
    if config is None or config.get('key') is None:
        if require:
            print('Not logged in, please login using `fw login` and your API key', file=sys.stderr)
            sys.exit(1)
        return None
    result = flywheel.Flywheel(config['key'], minimum_supported_major_version=11)
    result.api_client.user_agent = f'Flywheel CLI/{get_cli_version()} ' + result.api_client.user_agent
    log.debug(f'SDK Version: {flywheel.flywheel.SDK_VERSION}')  # pylint: disable=no-member
    log.debug(f'Flywheel Site URL: {result.api_client.configuration.host}')
    return result


def save_api_key(api_key, root=False):
    """Save the given api key to the user's config file.

    If api_key is None, then remove it from the file.
    """
    config = load_config()
    if config is None:
        config = {}

    if api_key is None:
        config.pop('key', None)
        config.pop('root', None)
    else:
        config['key'] = api_key
        config['root'] = root

    path = os.path.expanduser(CONFIG_PATH)

    # Ensure directory exists
    config_dir = os.path.dirname(path)
    if not os.path.isdir(config_dir):
        os.makedirs(config_dir)

    with open(path, 'w') as f:
        json.dump(config, f)


def parse_resolver_path(path):
    """Split out a string path, keeping analyses and files paths"""
    # TODO: Port this to SDK?
    if not path:
        return []

    if path.startswith('fw://'):
        path = path[5:]

    path = (path or '').strip('/')

    if '/files/' in path:
        path, file_path = path.split('/files/')
        file_path = ['files', file_path]
    else:
        file_path = []

    if '/analyses/' in path:
        path, analysis_path = path.split('/analyses/')
        analysis_path = ['analyses', analysis_path]
    else:
        analysis_path = []

    path = path.split('/') or []
    path = path + analysis_path + file_path

    return [path_el for path_el in path if path_el]

def get_login_id(fw):
    """Get a readable login id for the current api key"""
    status = fw.get_auth_status()  # pylint: disable=redefined-outer-name

    if status.is_device:
        device = fw.get_device(status.origin.id)
        return f'{device.get("type", "device")} - {device.get("name", status.origin.id)}'

    user = fw.get_current_user()
    return f'{user.firstname} {user.lastname}'

def get_login_info(fw):
    """Get a readable login id for the current api key"""
    status = fw.get_auth_status()  # pylint: disable=redefined-outer-name

    info = LoginInfo()
    info.is_device = status.is_device

    if status.is_device:
        device = fw.get_device(status.origin.id)
        info.device = device
        info.label = f'{device.get("type", "device")} - {device.get("name", status.origin.id)}'
        info.root = True

    else:
        user = fw.get_current_user()
        info.user = user
        info.label = f'{user.firstname} {user.lastname}'
        info.root = user['root']

    return info

def get_site_name(fw):
    """Get site name"""
    config = fw.get_config()
    name = config.site.get('name')
    url = config.site.get('api_url', fw.api_client.configuration.host)
    hostname = None

    if url:
        try:
            parts = urlparse(url)
            hostname = parts.hostname
        except ValueError:
            pass

    if name:
        if hostname:
            return f'{name} ({hostname})'
        return name
    if hostname:
        return hostname
    return 'Unknown Site'

class SdkUploadWrapper(Uploader, ContainerResolver):
    """SDK upload wrapper class

    For now we skip subjects, replacing them (effectively) with the project layer,
    and treating them as if they always exist.
    """
    def __init__(self, fw):
        # pylint: disable=super-init-not-called
        self.fw = fw
        self.fw.api_client.set_default_header('X-Accept-Feature', 'Subject-Container')
        self._supports_signed_url = None
        # Session for signed-url uploads
        self._upload_session = requests.Session()

    def supports_signed_url(self):
        """Get signed url feature"""
        if self._supports_signed_url is None:
            config = self.fw.get_config()

            # Support the new and legacy method of feature advertisement, respectively
            # Ref: https://github.com/flywheel-io/core/pull/1503
            features = config.get('features')
            f1 = features.get('signed_url', False) if features else False
            f2 = config.get('signed_url', False)

            self._supports_signed_url = f1 or f2
        return self._supports_signed_url

    def resolve_path(self, container_type, path):
        """Resolve path"""
        parts = path.split('/')

        try:
            result = self.fw.resolve(parts)
            container = result.path[-1]
            log.debug(f'Resolve {container_type}: {path} - returned: {container.id}')
            return container.id, container.get('uid')
        except flywheel.ApiException:
            log.debug(f'Resolve {container_type}: {path} - NOT FOUND')
            return None, None

    def resolve_children(self, container_type, path):
        """Resolve children path"""
        parts = path.split('/')

        try:
            result = self.fw.resolve(parts)
            log.debug(f'Resolve {container_type}: {path} - returned: {len(result.children)} children')
            return result.children
        except flywheel.ApiException:
            log.debug(f'Resolve {container_type}: {path} - NOT FOUND')
            return []

    def create_container(self, parent, container):
        """Create container"""
        create_fn = getattr(self.fw, f'add_{container.container_type}', None)
        if not create_fn:
            raise ValueError(f'Unsupported container type: {container.container_type}')
        create_doc = copy.deepcopy(container.context[container.container_type])

        if container.container_type == 'session':
            # Add subject to session
            create_doc['project'] = parent.parent.id
            create_doc['subject'] = copy.deepcopy(container.context['subject'])
            create_doc['subject']['_id'] = parent.id
            # Copy subject label to code
            create_doc['subject'].setdefault('code', create_doc['subject'].get('label', None))
        elif parent:
            create_doc[parent.container_type] = parent.id

        new_id = create_fn(create_doc)
        log.debug(f'Created container: {create_doc} as {new_id}')
        return new_id

    def check_unique_uids(self, request):
        try:
            return self.fw.check_uids_exist(request)
        except flywheel.ApiException as exc:
            if exc.status == 404:
                raise NotImplementedError('Unique UID check is not supported by the server')
            raise

    def upload(self, container, name, fileobj, metadata=None):
        upload_fn = getattr(self.fw, f'upload_file_to_{container.container_type}', None)

        if not upload_fn:
            print(f'Skipping unsupported upload to container: {container.container_type}')
            return

        log.debug(f'Uploading file {name} to {container.container_type}={container.id}')
        if self.supports_signed_url():
            self.signed_url_upload(container, name, fileobj, metadata=metadata)
        else:
            upload_fn(container.id, flywheel.FileSpec(name, fileobj), metadata=json.dumps(metadata))

    def file_exists(self, container, name):
        cont = self.fw.get(container.id)
        if not cont:
            return False
        for file_entry in cont.get('files', []):
            if file_entry['name'] == name:
                return True
        return False

    def signed_url_upload(self, container, name, fileobj, metadata=None):
        """Upload fileobj to container as name, using signed-urls"""
        # Create ticketed upload
        path_params = {
            'ContainerType': pluralize(container.container_type),
            'ContainerId': container.id
        }
        ticket, upload_url = self.create_upload_ticket(path_params, name, metadata=metadata)

        log.debug(f'Upload url for {name} on {container.container_type}={container.id}: {ticket} (ticket={upload_url})')

        # Perform the upload
        resp = self._upload_session.put(upload_url, data=fileobj)
        max_retries = 3
        retry_num = 0
        if resp.status_code == 429 or 500 <= resp.status_code < 600:
            while retry_num < max_retries:
                log.info('Upload failed, retrying...')
                time.sleep(2 ** retry_num)
                retry_num += 1
                resp = self._upload_session.put(upload_url, data=fileobj)

        resp.raise_for_status()
        resp.close()

        # Complete the upload
        self.complete_upload_ticket(path_params, ticket)

    def create_upload_ticket(self, path_params, name, metadata=None):
        """Create upload ticket"""
        body = {
            'metadata': metadata or {},
            'filenames': [name]
        }

        response = self.call_api(TICKETED_UPLOAD_PATH, 'POST',
                                 path_params=path_params,
                                 query_params=[('ticket', '')],
                                 body=body,
                                 response_type=object)

        return response['ticket'], response['urls'][name]

    def complete_upload_ticket(self, path_params, ticket):
        """Complete upload ticket"""
        self.call_api(TICKETED_UPLOAD_PATH, 'POST',
                      path_params=path_params,
                      query_params=[('ticket', ticket)])

    def call_api(self, resource_path, method, **kwargs):
        """Call api"""
        kwargs.setdefault('auth_settings', ['ApiKey'])
        kwargs.setdefault('_return_http_data_only', True)
        kwargs.setdefault('_preload_content', True)

        return self.fw.api_client.call_api(resource_path, method, **kwargs)
