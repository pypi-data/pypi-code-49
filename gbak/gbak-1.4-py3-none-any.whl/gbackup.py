import os
import io
import pickle
import json
import argparse
import base64
import logging
from logging.handlers import RotatingFileHandler
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import crypto

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(thread)d %(funcName)s %(message)s')
file_handler = RotatingFileHandler('debug.log', maxBytes=(1024 * 1024 * 128), backupCount=1)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Client(object):
    def __init__(self, config_file, action, input_val, output_dir):
        self.action = action
        self.input_val = input_val
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if output_dir:
            self.output_dir = os.path.join(base_dir, output_dir)
            os.makedirs(self.output_dir, exist_ok=True)
        try:
            with open(config_file) as f:
                self.config = json.load(f)
        except IOError:
            print('`config.json` file not found')
        creds = None
        if os.path.exists(self.config['TOKEN_FILE']):
            with open(self.config['TOKEN_FILE'], 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.config['CRED_FILE'], self.config['SCOPES'])
                creds = flow.run_local_server(port=0)
            with open(self.config['TOKEN_FILE'], 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('drive', 'v3', credentials=creds)

    def create_folder(self, name, folder_id=None):
        logger.info(f'--> Get or create Google Drive folder: {name}')
        results = self.service.files().list(q=f"name='{name}' and mimeType='application/vnd.google-apps.folder'",
                                            spaces='drive',
                                            fields='files(id, name)').execute()
        items = results.get('files', [])
        if not items:
            file_metadata = {'name': name, 'mimeType': 'application/vnd.google-apps.folder'}
            if folder_id:
                file_metadata.update({'parents': [folder_id]})
            file = self.service.files().create(body=file_metadata, fields='id').execute()
            return file.get('id', None)
        for item in items:
            return item.get('id',  None)

    def upload_file(self, filename, file_path, folder_id=None):
        logger.info(f'--> Upload file to Google Drive: {file_path}')
        file_metadata = {'name': filename}
        if folder_id:
            file_metadata.update({'parents': [folder_id]})
        media = MediaFileUpload(file_path, resumable=True)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id', None)

    def share_file(self, file_id):
        logger.info(f'--> Share Google Drive file or folder: {file_id}')
        permissions = {
            'type': 'anyone',
            'role': 'reader'
        }
        self.service.permissions().create(fileId=file_id, body=permissions, fields='id').execute()

    def search(self, query_term):
        logger.info(f'--> Search on Google Drive by q: {query_term}')
        results = []
        page_token = None
        while True:
            response = self.service.files().list(q=query_term,
                                                 spaces='drive',
                                                 fields='nextPageToken, files(id, name, mimeType, originalFilename)',
                                                 pageToken=page_token).execute()
            results += response.get('files', [])
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return results

    def download_file(self, file_id, file_path):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO(file_path, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            logger.info('Download %d%%.' % int(status.progress() * 100))
        return file_path

    def get_file_info(self, file_id, field):
        logger.info(f'--> Get Google Drive file info: {file_id}')
        file_info = self.service.files().get(fileId=file_id, fields=field).execute()
        return file_info.get(field, None)

    def run(self):
        try:
            buffer_size = 64 * 1024
            if self.action == 'upload':
                logger.info(f'=== gbackup [UPLOAD]: {self.input_val} ===')
                parent_folder_id = self.create_folder(self.config['DRIVE_FOLDER_ROOT'])
                self.share_file(parent_folder_id)
                filename = os.path.basename(self.input_val)
                b64_filename = base64.b64encode(bytes(filename, 'utf-8')).decode('ascii')
                local_dir = os.path.dirname(self.input_val)
                password = self.config['DRIVE_SERVER'] + self.config['KEY'] + filename
                crypt_path = os.path.join(local_dir, b64_filename)
                if self.config['IS_CRYPT'] == 'True':
                    logger.info(f'--> gbackup encrypt file: {self.input_val}')
                    crypto.encryptFile(self.input_val, crypt_path, password, buffer_size, self.config)
                    file_id = self.upload_file(b64_filename, crypt_path, parent_folder_id)
                    if file_id:
                        os.remove(crypt_path)
                        print(file_id)
            else:
                logger.info(f'=== gbackup [DOWNLOAD]: {self.input_val} ===')
                b64_filename = self.get_file_info(self.input_val, 'name')
                filename = base64.b64decode(b64_filename).decode('utf-8')
                dl_path = os.path.join(self.output_dir, b64_filename)
                dl_file = self.download_file(self.input_val, dl_path)
                decrypt_path = os.path.join(self.output_dir, filename)
                password = self.config['DRIVE_SERVER'] + self.config['KEY'] + filename
                if self.config['IS_CRYPT'] == 'True':
                    logger.info(f'--> gbackup decrypt file: {dl_file}')
                    crypto.decryptFile(dl_file, decrypt_path, password, buffer_size, self.config)
                    if os.path.exists(decrypt_path):
                        os.remove(dl_file)
                        print(decrypt_path)
        except Exception as e:
            logger.error(f'[Run Error] {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, help='Config path')
    parser.add_argument('--action', type=str, help='Action name (upload/download)')
    parser.add_argument('--input', type=str, help='Input value (path/file_id)')
    parser.add_argument('--output', type=str, help='Output dir')
    args = parser.parse_args()

    c = Client(args.config, args.action, args.input, args.output)
    c.run()