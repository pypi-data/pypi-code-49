import os

import requests 
import platform
from pprint import pformat
from json.decoder import JSONDecodeError
from uuid import uuid4

from functools import partial
from ..errors import SpintopException

from ..auth import AuthModule

from ..logs import _logger
from ..compat import VERSION
from ..storage import TEMP_DIR

logger = _logger('spinhub-client')

TEMPORARY_DOWNLOAD_FOLDER = os.path.join(TEMP_DIR, '.spinhub-download-cache')
if not os.path.exists(TEMPORARY_DOWNLOAD_FOLDER):
    os.makedirs(TEMPORARY_DOWNLOAD_FOLDER)
    
class SpinHubClientError(SpintopException):
    pass

class SpinHubAPIError(SpintopException):
    def __init__(self, resp):
        try:
            json = resp.json()
        except JSONDecodeError:
            json = {}
        
        error_type = json.get('error_type', 'UNKNOWN')
        error_messages = json.get('error_messages', {})
        messages_as_string = '\n\t'.join(['%s: %s' % (key, value) for key, value in error_messages.items()])
        
        if not messages_as_string:
            messages_as_string = json.get('error_message') # singular, the direct exception message
            
        message = 'A {status} error of type "{error_type}" occured while contacting API.\n\t{messages}'.format(
            status=resp.status_code, 
            error_type=error_type,
            messages=messages_as_string
        )
        super(SpinHubAPIError, self).__init__(message)
        self.resp = resp

# def SpinHubClient(spinhub_url=None, auth=None, org=None):
#     if auth is None:
#         auth = AuthModule()
#     return SpinHubAPIModule(spinhub_url, auth, org=org)

def SpinHubSession(prefix, auth_module):
    if prefix is None:                                                                                                                                                                                                                                                                                                                             
        prefix = ""                                                                                                                                                                                                                                                                                                                                
    else:                                                                                                                                                                                                                                                                                                                                          
        prefix = prefix.rstrip('/')                                                                                                                                                                                                                                                                                                      

    def attempt_request(f, method, url, *args, **kwargs):
        if 'headers' not in kwargs: kwargs['headers'] = {}
        kwargs['headers'].update(auth_module.get_auth_headers())
        resp = f(method, prefix + url, *args, **kwargs)           
        if resp.status_code >= 400:
            raise SpinHubAPIError(resp)
        return resp
    
    def new_request(prefix, *args, **kwargs):
        try:
            resp = attempt_request(*args, **kwargs)  
        except SpinHubAPIError as e:
            if e.resp.status_code == 401:
                # Attempt ONCE to refresh the credentials and retry.
                auth_module.refresh_credentials()
                resp = attempt_request(*args, **kwargs)
            else:
                raise
        return resp
    
    s = requests.Session()                                                                                                                                                                                                                                                                                                                     
    s.request = partial(new_request, prefix, s.request)                                                                                                                                                                                                                                                                                            
    return s  

class SpinHubClientModule(object):
    def __init__(self, config, auth):
        self.config = config
        
        self._session = None
        
        self.auth = auth
        
        self.default_org_id = None
        
        self._user_info = None
        self._default_org = None
        self._machine = None
    
    @property
    def session(self):
        if not self._session:
            profile = self.config.get_selected_profile()
            url = profile['spinhub_url']
            self.default_org_id = profile.get('org_id')
            self._session = SpinHubSession(url, self.auth)
        return self._session
    
    def test_private_endpoint(self):
        resp = self.session.get('/private')
        return resp
    
    @property
    def user_info(self):
        if self._user_info is None:
            self._user_info = self.session.get('/userinfo').json()
        return self._user_info
    
    @property
    def default_org(self):
        if self._default_org is None:
            possible_orgs = self.user_info['organizations']
            selected_org = None
            if self.default_org_id:
                for org in possible_orgs:
                    if org['uuid'].startswith(self.default_org_id):
                        selected_org = org
                        break
                else:
                    raise SpinHubClientError('Unable to find org with ID %s associated with this machine.' % self.default_org_id)
            else:
                selected_org = possible_orgs[0]
                logger.info('No org specified, using the default defined by SpinHub for this user: %s' % selected_org['key'])
            self._default_org = selected_org
        
        return self._default_org
    
    def get_this_machine_id(self):
        return self.config.get_selected_profile()['machine_id']
    
    def get_token(self):
        token_url = self._get_org_urls('token')
        return self.session.get(token_url).text
    
    @property
    def machine(self):
        if self._machine is None:
            machines_url = self._get_org_urls('machines')
            this_machine_id = self.get_this_machine_id()
            logger.info('Local machine ID is %s' % this_machine_id)
            self._machine = self.session.get(machines_url + '/' + this_machine_id).json()
        return self._machine
    

    def create_task(self, task_type, user_id=None):
        if user_id is None:
            user_id = self.get_this_machine_id()
        machines_url = self._get_org_urls('machines')
        self.session.post(machines_url + '/' + user_id + '/tasks', json=dict(
            task_type=task_type
        ))
    
    def task_acknowledged(self, task_id):
        return self.update_task_status(task_id, 'ACKNOWLEDGED')
    
    def task_started(self, task_id):
        return self.update_task_status(task_id, 'IN_PROGRESS')
    
    def task_done(self, task_id, success=True):
        return self.update_task_status(task_id, 'DONE', task_success=success)
        
    def update_task_status(self, task_id, task_status, task_success=None):
        user_id = self.get_this_machine_id()
        machines_url = self._get_org_urls('machines')
        self.session.put(machines_url + '/' + user_id + '/tasks', json=dict(
            uuid=task_id,
            task_status=task_status,
            task_success=task_success
        ))
        
    
    def get_tasks(self, **query_params):
        machines_url = self._get_org_urls('machines')
        this_machine_id = self.get_this_machine_id()
        return self.session.get(machines_url + '/' + this_machine_id + '/tasks', params=query_params).json()
    
    def _get_org_urls(self, sub_key):
        return self.default_org['_links'][sub_key]
    
    def register_machine(self, name, token, org_id=None):
        if org_id:
            machines_url = '/orgs/%s/machines' % org_id
        else:
            machines_url = self._get_org_urls('machines')
            
        logger.info('Registering machine')
        
        params = {}
        if token:
            params.update({'secret_code': token})
        
        response = self.session.put(machines_url + '/register', json=dict(
            nickname= name,
            hostname= platform.node(),
            client_version=VERSION
        ), params=params)
        
        data = response.json()
        self.config.update_profile(machine_id= data['uuid'])
        self.config.save()
    
    def upload_file(self, object_key, version, filepath, checksums={}):
        objects_url = self._get_org_urls('objects')
        logger.info('Asking SpinHub to upload new file %s @ %s' % (filepath, object_key))
        # Generate a new URL for upload.
        
        _, filename = os.path.split(filepath)
        response = self.session.put(objects_url, json=dict(
            object_key=object_key,
            version_name=version,
            filename=filename,
            checksums=checksums
        ))
        response_data = response.json()
        upload_uri = response_data['upload_uri']
        upload_fields = response_data['upload_fields']
        
        logger.info('Beginning upload at SpinHub provided URI')
        with open(filepath, 'rb') as file_to_upload:
            files = {'file': file_to_upload}
            resp = requests.post(upload_uri, files=files, data=upload_fields)
        
        self.confirm_uploaded_file(response_data)
        return response_data
    
    def confirm_uploaded_file(self, upload_response):
        confirm_uri = self.get_data_blob_uri(upload_response['data_blob'], key='confirm')
        self.session.put(confirm_uri)
    
    def download_uploaded_file(self, upload_response, stream):
        download_uri = self.get_data_blob_uri(upload_response['data_blob'])
        return self.download_data_blob(download_uri, stream)
    
    def get_data_blob_uri(self, data_blob, key='download'):
        return data_blob['_links'][key]
    
    def get_tag_download_uri(self, tag):
        return tag['_links']['download']
    
    def download_file(self, object_key, target_folder=TEMPORARY_DOWNLOAD_FOLDER, index=0):
        objects_url = self._get_org_urls('objects')
        response = self.session.get(objects_url + '/' + object_key)
        object_details = response.json()
        tag = object_details['tags'][index]
        
        logger.debug(pformat(tag))
        logger.info('Downloading {object_key} [version={tagname}][{index}]'.format(
            object_key=object_key,
            tagname=tag['tagname'],
            index=index
        ))
        download_uri = self.get_tag_download_uri(tag)
        
        return self.download_data_blob(download_uri, target_folder=target_folder)
        
    def download_data_blob(self, download_uri, target_folder=None, stream=None):
        data_object = self.session.get(download_uri).json()
        url = data_object['download_uri']
        filename = data_object['filename']
        resp = requests.get(url, allow_redirects=True)
        
        if stream:
            stream.write(resp.content)
            return None
        else:
            filepath = os.path.join(target_folder, filename)
            with open(filepath, 'wb+') as writefile:
                writefile.write(resp.content)
            return filepath
        
        