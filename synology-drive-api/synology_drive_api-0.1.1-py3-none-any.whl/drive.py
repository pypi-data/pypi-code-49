import functools
import urllib.parse
from pathlib import Path

import simplejson as json

from synology_drive_api.base import SynologySession, color_name_to_id


def form_urlencoded(data):
    """
    Generate urlencoded data
    :param data:
    :return: return form data
    """
    data_list = []
    for key, value in data.items():
        value_encode = urllib.parse.quote(json.dumps(value), safe='') if not isinstance(value, str) else value
        # [key, '=', value_encode]
        data_list.append(f"{key}={value_encode}")
    urlencoded_data = '&'.join(data_list)
    return urlencoded_data


def concat_drive_path(dest_path, end_point, default_folder='mydrive'):
    """
    Generate file path
    :param dest_path: parent path
    :param end_point: file_name or folder_name
    :param default_folder
    :return:
    """
    if dest_path is None:
        display_path = f"/{default_folder}/{end_point}"
    elif dest_path.startswith('id'):
        display_path = f"{dest_path}/folder_name"
    else:
        # add start position /
        dest_path = f"/{dest_path}" if not dest_path.startswith('/') else dest_path
        # add end position /
        dest_path = f"{dest_path}/" if not dest_path.endswith('/') else dest_path
        display_path = f"{dest_path}{end_point}"
    return display_path


class SynologyDrive:

    def __init__(self, username, password, ip_address=None, port=None, nas_domain=None, https=True):
        self.session = SynologySession(username, password, ip_address, port, nas_domain, https)
        self._path_dict = {}

    def __enter__(self):
        self.login()
        self._label_dict = self.get_labels()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logout()

    def login(self):
        return self.session.login('SynologyDrive')

    def logout(self):
        return self.session.logout('SynologyDrive')

    def get_teamfolder_info(self):
        """
        :return: {folder_name: folder_id, ...}
        """
        api_name = 'SYNO.SynologyDrive.TeamFolders'
        endpoint = 'entry.cgi'
        params = {'api': api_name, 'version': 1, 'method': 'list', 'filter': {}, 'sort_direction': 'asc',
                  'sort_by': 'owner', 'offset': 0, 'limit': 1000}
        resp = self.session.http_get(endpoint, params=params)

        if not resp['success']:
            raise Exception('Get teamfolder info failed.')

        if resp['data']['total'] == 0:
            return {}

        return {folder_info['name']: folder_info['file_id'] for folder_info in resp['data']['items']}

    @functools.lru_cache()
    def get_folder_info(self, dir_path):
        """
        :param dir_path: '/team-folders/folder_name/folder_name1' or 'id:430167496067125111'
        :return:
        """
        # add start position /
        dest_path = f"/{dir_path}" if not dir_path.startswith('/') else dir_path
        api_name = 'SYNO.SynologyDrive.Files'
        endpoint = 'entry.cgi'
        params = {'api': api_name, 'version': 2, 'method': 'list', 'filter': {}, 'sort_direction': 'asc',
                  'sort_by': 'owner', 'offset': 0, 'limit': 1000, 'path': dest_path}
        return self.session.http_get(endpoint, params=params)

    def get_info(self):
        api_name = 'SYNO.SynologyDrive.Info'
        info = self.session.get_api_list(api_name)
        endpoint = info['path']
        params = {'api': api_name, 'version': info['maxVersion'], 'method': 'get', '_sid': self.session.sid}
        return self.session.http_get(endpoint, params=params)

    def get_labels(self, name=None):
        """
        get label name and label id
        :param name:
        :return: {name: label_id, ...}
        """
        api_name = 'SYNO.SynologyDrive.Labels'
        endpoint = 'entry.cgi'
        params = {'api': api_name, 'version': 1, 'method': 'list'}
        req = self.session.http_get(endpoint, params=params)
        label_items = req['data']['items']

        if not label_items:
            return {}

        label_dict = {item['name']: item['label_id'] for item in label_items}
        if name is None:
            return label_dict
        else:
            return {name: label_dict[name]}

    def create_label(self, name, color='gray'):
        """
        :param name: label name
        :param color: color name gray/red/orange/yellow/green/blue/purple
        :return:
        """
        color = color_name_to_id(color_name=color)
        if name in self.get_labels():
            raise Exception('Label_name already exists, please use another one!')
        api_name = 'SYNO.SynologyDrive.Labels'
        endpoint = 'entry.cgi'
        params = {'api': api_name, 'version': 1, 'method': 'create',
                  'name': name, 'color': color}
        ret_label = self.session.http_put(endpoint, params=params)
        self.set_label_dict(name, ret_label['data']['label_id'])
        return ret_label

    def delete_label(self, name=None, label_id=None):
        """
        :param name:
        :param label_id:
        :return:
        """
        if label_id is None:
            label = self.get_labels(name)
            label_id = label[name]
        api_name = 'SYNO.SynologyDrive.Labels'
        endpoint = 'entry.cgi'
        params = {'api': api_name, 'version': 1, 'method': 'delete', 'label_id': label_id}
        return self.session.http_delete(endpoint, params=params)

    def set_files_label(self, files, labels):
        """
        set file or folder labels
        :param files: ["id:505415003021516807", "id:525657984139799470", "id:525657984810888112"]
        :param labels: [{"action": "add", "label_id": "15"}, {"action": "add", "label_id": "16"}]
        :return:
        """
        api_name = 'SYNO.SynologyDrive.Files'
        endpoint = 'entry.cgi'
        data = {'files': files, 'labels': labels, 'api': api_name, 'method': 'label', 'version': '2'}
        urlencoded_data = form_urlencoded(data)
        params = {'_sid': self.session.sid}
        return self.session.http_post(endpoint, data=urlencoded_data, params=params)

    def add_file_labels(self, file_path, label):
        """
        add labels to file
        :param file_path: '/team-folders/test_drive/SCU285/test.xls'
        :param label: label
        :return:
        """
        if isinstance(label, list):
            label = [{'action': 'add', 'label_id': self.label_dict.get(single_label)} for single_label in label]
        else:
            label = [{'action': 'add', 'label_id': self.label_dict.get(label)}]
        if file_path.isdigit():
            file_path_params = f"id:{file_path}"
        else:
            file_path_params = file_path
        return self.set_files_label([file_path_params], label)

    def create_folder(self, folder_name, dest_folder_path=None):
        """
        Create folder in dest_folder, default location is 'mydrive'. If folder in path does not exist
        :param dest_folder_path: 'id:433415919843151874/folder1', '/mydrive/', 'mydrive/', 'team-folder/folder2/'
        :param folder_name: created folder name
        :return:
        """
        display_path = concat_drive_path(dest_folder_path, folder_name)
        api_name = 'SYNO.SynologyDrive.Files'
        endpoint = 'entry.cgi'
        params = {'path': display_path, 'version': 2, 'api': api_name,
                  'type': 'folder', 'conflict_action': 'autorename', 'method': 'create'}
        return self.session.http_put(endpoint, params=params)

    def upload_file(self, file, dest_folder_path=None):
        """
        upload file to drive
        :param file: binary_file
        :param dest_folder_path: upload folder
        :return:
        """
        file_name = file.name
        display_path = concat_drive_path(dest_folder_path, file_name)
        api_name = 'SYNO.SynologyDrive.Files'
        endpoint = 'entry.cgi'
        params = {'api': api_name, 'method': 'upload', 'version': 2, 'path': display_path,
                  'type': 'file', 'conflict_action': 'version'}
        files = {'file': file}
        return self.session.http_post(endpoint, params=params, files=files)

    def get_file_or_folder_info(self, file_path):
        """
        file_path
        :param file_path:
        :return:
        """
        file_path_obj = Path(file_path)
        parent_path = file_path_obj.parent.as_posix()
        files = self.get_folder_info(parent_path)
        if files['data']['total'] == 0:
            return {file_path: None}
        for file in files['data']['items']:
            if file['name'] == file_path_obj.name:
                return {file['name']: {'id': file['file_id']}}

    def set_label_dict(self, label_name, label_id):
        self._label_dict[label_name] = label_id

    @property
    def path_dict(self):
        return self._path_dict

    @property
    def label_dict(self):
        return self._label_dict
