import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse, urljoin, quote
import os
import json

# display messages when in a interactive context (IPython or Jupyter)
try:
    get_ipython()
except Exception:
    VERBOSE = False
else:
    VERBOSE = True


class ETH_IAM_conn():
    def __init__(self, admin_username, admin_password, hostname, endpoint_base):
        self._admin_username = admin_username
        self._admin_password = admin_password
        self.hostname = hostname
        self.endpoint_base = endpoint_base
        self.verify_certificates = True
        self.timeout=600

    def _delete_request(self, endpoint):
        full_url = urljoin(self.hostname, self.endpoint_base+endpoint)
        resp = requests.delete(
            full_url,
            headers={'Accept': 'application/json'},
            auth=(self._admin_username, self._admin_password),
            verify=self.verify_certificates,
            timeout=self.timeout,
        )
        return resp

    def _post_request(self, endpoint, body):
        full_url = urljoin(self.hostname, self.endpoint_base+endpoint)
        resp = requests.post(
            full_url,
            json.dumps(body),
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            auth=(self._admin_username, self._admin_password),
            verify=self.verify_certificates,
            timeout=self.timeout,
        )
        return resp

    def _put_request(self, endpoint, body):
        full_url = urljoin(self.hostname, self.endpoint_base+endpoint)
        resp = requests.put(
            full_url,
            json.dumps(body),
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            auth=(self._admin_username, self._admin_password),
            verify=self.verify_certificates,
            timeout=self.timeout,
        )
        return resp

    def _get_request(self, endpoint):
        full_url = urljoin(self.hostname, self.endpoint_base+endpoint)
        resp = requests.get(
            full_url,
            headers={'Accept': 'application/json'},
            auth=(self._admin_username, self._admin_password),
            verify=self.verify_certificates,
            timeout=self.timeout,
        )
        return resp


    def new_person(self, firstname, lastname):
        raise Exception("not implemented yet")
        return Person(conn=self, firstname=firstname, lastname=lastname)
    
    def get_person(self, identifier=None, **kwargs):
        if identifier is not None:
            endpoint = '/usermgr/person/{}'.format(identifier)
        elif kwargs:
            args = "&".join("{}={}".format(key, val) for key, val in kwargs.items())
            endpoint = '/usermgr/person?{}'.format(args)
        else:
            raise ValueError("please provide an identifier")

        resp = self._get_request(endpoint)
        data = json.loads(resp.content.decode())
        if resp.ok:
            return Person(conn=self, data=data)
        else:
            raise ValueError(data['message'])

    def get_user(self, identifier):
        endpoint = '/usermgr/user/{}'.format(identifier)
        resp = self._get_request(endpoint)
        data = json.loads(resp.content.decode())
        if resp.ok:
            return User(conn=self, data=data)
        else:
            raise ValueError(data['message'])


    def get_groups(self, **kwargs):
        """
        agroup=<Admin Group>  -- Get all groups of a given admin group
        name=group_name*      -- all groups starting with «group_name*»
        """
        if kwargs:
            args = "&".join("{}={}".format(key, val) for key, val in kwargs.items())
            endpoint = '/groupmgr/groups?{}'.format(args)
        else:
            raise ValueError("please provide a name or agroup parameter (or both)")

        resp = self._get_request(endpoint)
        data = json.loads(resp.content.decode())
        if resp.ok:
            groups = []
            for item in data:
                groups.append(Group(conn=self, data=item))

            return groups
        else:
            raise ValueError(data['message'])

    
    def get_group(self, identifier=None, **kwargs):
        if identifier is not None:
            endpoint = '/groupmgr/group/{}'.format(identifier)
        elif kwargs:
            args = "&".join("{}={}".format(key, val) for key, val in kwargs.items())
            endpoint = '/groupmgr/group/?{}'.format(args)
        else:
            raise ValueError("please provide an identifier")
        resp = self._get_request(endpoint)
        data = json.loads(resp.content.decode())
        if resp.ok:
            return Group(conn=self, data=data)
        else:
            raise ValueError(data['message'])


class Person():
    def __init__(self, conn, data=None):
        self.conn = conn
        self.data = data
        if data:
            for key in data:
                setattr(self, key, data[key])
        
    def new_user(self, username, password, description=None):
        endpoint = '/usermgr/person/{}'.format(self.npid)
        body = {
            "username": username,
            "init_passwd": password,
            "memo": description,
        }
        resp = self.conn._post_request(endpoint, body) 
        if resp.ok:
            user = self.conn.get_user(username) 
            if VERBOSE: print("new user {} was successfully created".format(username))
            return user
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])
    

class User():
    def __init__(self, conn, data):
        self.conn = conn
        self.data = data
        if data:
            for key in data:
                setattr(self, key, data[key])

    def delete(self):
        endpoint = '/usermgr/user/{}'.format(self.username)
        resp = self.conn._delete_request(endpoint)
        if resp.ok:
            if VERBOSE: print("User {} deleted.".format(self.username))
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])

    def get_person(self):
        endpoint = '/usermgr/person/{}'.format(self.npid)
        resp = self.conn._get_request(endpoint)
        data = json.loads(resp.content.decode())
        if resp.ok:
            return Person(conn=self, data=data)
        else:
            raise ValueError(data['message'])

    def _to_from_group(self, group_name, action='add', mess="{} {}"):
        endpoint = '/groupmgr/group/{}/members/{}'.format(group_name, action)
        body = [ self.username ]
        resp = self.conn._put_request(endpoint, body)
        if resp.ok:
            if VERBOSE: print(mess.format(self.username, group_name))
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])

    def add_to_group(self, group_name):
        self._to_from_group(group_name, action='add_forgiving', mess="Added user {} to group {}")

    def remove_from_group(self, group_name):
        self._to_from_group(group_name, 'del', mess="Removed user {} from group {}")


    def grant_service(self, service_name):
        endpoint = '/usermgr/user/{}/service/{}'.format(self.username, service_name)
        resp = self.conn._post_request(endpoint, {})
        if resp.ok:
            if VERBOSE: print("Service {} granted to {}".format(service_name, self.username))
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])

    def revoke_service(self, service_name):
        endpoint = '/usermgr/user/{}/service/{}'.format(self.username, service_name)
        resp = self.conn._delete_request(endpoint)
        if resp.ok:
            if VERBOSE: print("Service {} revoked from {}".format(service_name, self.username))
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])

    def get_service(self, service_name):
        # TODO: API is not implemented yet
        endpoint = '/usermgr/user/{}/service/{}'.format(self.username, service_name)
        resp = self.conn._get_request(endpoint)
        data = json.loads(resp.content.decode())
        if resp.ok:
            return Service(conn=self.conn, data=data)
        else:
            raise ValueError(data['message'])

    def set_password(self, password, service_name="LDAPS"):
        """Sets a password for a given service
        """
        endpoint = '/usermgr/user/{}/service/{}'.format(self.username, service_name)
        body = { "password": password }
        resp = self.conn._put_request(endpoint, body) 

        if resp.ok:
            if VERBOSE: print(
                "password for user {} and service {} has been successfully changed.".format(
                    self.username, service_name
                )
            )
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])


class Service():
    def __init__(self, conn, data):
        self.conn = conn
        self.data = data
        if data:
            for key in data:
                setattr(self, key, data[key])


class Group():
    def __init__(self, conn, data):
        self.conn = conn
        self.data = data
        if data:
            for key in data:
                setattr(self, key, data[key])

    def set_members(self, members):
        if not isinstance(members, list):
            members = [members]

    def add_members(self, members):
        if not isinstance(members, list):
            members = [members]
        self._to_from_group(members, action='add_forgiving', mess="Added members to group {}")

    def del_members(self, members):
        if not isinstance(members, list):
            members = [members]
        self._to_from_group(members, action='del', mess="Removed members from group {}")

    def _to_from_group(self, members, action='add', mess="{}"):
        endpoint = '/groupmgr/group/{}/members/{}'.format(self.name, action)
        resp = self.conn._put_request(endpoint, members)
        if resp.ok:
            if VERBOSE: print(mess.format(self.name))
            self.data = json.loads(resp.content.decode())
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])

    def delete(self):
        endpoint = '/groupmgr/group/{}'.format(self.name)
        resp = self.conn._delete_request(endpoint)
        if resp.ok:
            if VERBOSE: print("Group {} deleted.".format(self.name))
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data['message'])


def _load_configuration(paths, filename='.ethz_iam_webservice'):
    if paths is None:
        paths = [os.path.expanduser("~")]

    # look in all config file paths 
    # for configuration files and load them
    admin_accounts = []
    for path in paths:
        abs_filename = os.path.join(path, filename)
        if os.path.isfile(abs_filename):
            with open(abs_filename, 'r') as stream:
                try:
                    config = yaml.safe_load(stream)
                    for admin_account in config['admin_accounts']:
                        admin_accounts.append(admin_account)
                except yaml.YAMLexception as e:
                    print(e)
                    return None

    return admin_accounts


def login(admin_username=None, admin_password=None):
    hostname = "https://iam.passwort.ethz.ch"
    endpoint_base = "/iam-ws-legacy"

    config_path = os.path.join(
        os.path.expanduser("~"),
        '.ethz_iam'
    )
    if os.path.exists(config_path):
        import configparser
        raise Exception("not yet implemented")

    if admin_username is None:
        admin_username = input("Enter the admin username: ".format(admin_username))

    if admin_password is None:
        import getpass
        admin_password = getpass.getpass("Enter the password for admin user {}".format(admin_username))

    return ETH_IAM_conn(admin_username, admin_password, hostname, endpoint_base)
