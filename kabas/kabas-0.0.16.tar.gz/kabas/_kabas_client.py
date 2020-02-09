from string import Template
import os
import json

import requests

from kabas._kabas_cache import KabasCache
from kabas.kabas_file_details import KabasFileDetails
from kabas.kabas_project_details import KabasProjectDetails

class KabasClient:

    def __init__(self, project_key = None):

        self._session = requests.session()

        config_file_name = 'config.json'

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), config_file_name), "r", encoding = 'utf-8-sig') as f:

            config = json.load(f)

            self._base_url = config['api']['api_base_url']
            self._session.verify = config['api']['api_verify_cert']

        if project_key is not None:

            self._session.headers.update({'x-kabas-key' : project_key})

        self._cache = KabasCache.getInstance()

    def __enter__(self):

        return self

    def _verify_response(self, response, expected_status_code):

        if response.status_code != expected_status_code:
        
            try:
                error_code = response.json().get('errorCode')
                error_message = response.json().get('errorMessage')

                if (error_code is not None and error_message is not None):
                    
                    raise KabasClientError(error_code, error_message)
                
                else:

                    raise KabasClientError("FailedRequest", "Something went wrong... HTTP status code: {0}".format(response.status_code))

            except:
                raise KabasClientError("FailedRequest", "Something went wrong... HTTP status code: {0}".format(response.status_code))

    def get_project(self, project_id):

        url = Template('$base_url/projects/$project_id').substitute(base_url = self._base_url, project_id = project_id)

        with self._session.get(url) as response:

            self._verify_response(response, 200)

            return KabasProjectDetails.from_json(response.json())

    def delete_project(self, project_id):

        url = Template('$base_url/projects/$project_id').substitute(base_url = self._base_url, project_id = project_id)

        with self._session.delete(url) as response:

            self._verify_response(response, 204)

    def find_project(self, project_name):

        url = Template('$base_url/projects/find').substitute(base_url = self._base_url)

        with self._session.get(url, params = {"name": project_name}) as response:

            self._verify_response(response, 200)

            return response.json()

    def get_public_projects(self):

        url = Template('$base_url/projects').substitute(base_url = self._base_url)

        with self._session.get(url) as response:

            self._verify_response(response, 200)

            return list(map(lambda x: KabasProjectDetails.from_json(x), response.json()))

    def get_file(self, project_id, file_name):

        all_files = self.get_project(project_id).files

        filtered_files = list(filter(lambda x: x.file_name == file_name, all_files))

        if len(filtered_files) != 1:

            raise Exception("File not found")

        return filtered_files[0]

    def download_file(self, project_id, file_name, target_directory = None):

        if target_directory is None:
            target_directory = os.path.dirname(self._cache.get_cache_location(project_id, file_name))

        target_path = os.path.join(target_directory, file_name)

        if not os.path.exists(target_directory):

            os.makedirs(target_directory)

        file_detail = self.get_file(project_id, file_name)

        if self._cache.get_lookup_version(project_id, file_name) == file_detail.latest_version_id:

                self._cache.retrieve_from_cache(project_id, file_name, target_directory)

        else:

            with requests.get(file_detail.url, stream=True) as response:

                self._verify_response(response, 200)

                with open(target_path, 'wb') as fd:

                    for chunk in response.iter_content(chunk_size = 128):
                        fd.write(chunk)

                self._cache.add_to_cache(file_detail, target_path)

        return target_path

    def upload_file(self, project_id, file_path):

        with open(file_path, "rb") as f:

            files = { 'formFile': f}

            url = Template('$base_url/projects/$project_id/files').substitute(base_url = self._base_url, project_id = project_id)

            with self._session.post(url, files = files) as response:

                self._verify_response(response, 200)

                file_detail = KabasFileDetails.from_json(project_id, response.json())

                self._cache.add_to_cache(file_detail, file_path)

                return file_detail

    def update_file(self, project_id, file_name, file_path = None):

        if file_path is None:

            file_path = self._cache.get_cache_location(project_id, file_name)

        file_detail = self.get_file(project_id, file_name)

        with open(file_path, "rb") as f:

            files = { 'formFile': f}

            url = Template('$base_url/projects/$project_id/files/$file_id').substitute(
                                                                                base_url = self._base_url, 
                                                                                project_id = project_id,
                                                                                file_id = file_detail.file_id)

            with self._session.put(url, files = files) as response:

                self._verify_response(response, 200)

                file_detail = KabasFileDetails.from_json(project_id, response.json())

                self._cache.add_to_cache(file_detail, file_path)

                return file_detail
   
    def delete_file(self, project_id, file_name):
    
        file_detail = self.get_file(project_id, file_name)

    
        url = Template('$base_url/projects/$project_id/files/$file_id').substitute(    
                                                               base_url = self._base_url,    
                                                               project_id = project_id,    
                                                               file_id = file_detail.file_id)

    
        with self._session.delete(url) as response:
   
            self._verify_response(response, 204)
            self._cache.delete_from_cache(project_id, file_name)

    # def create_new(self, project_name, public = False):

    #     url = Template('$base_url/projects').substitute(base_url = self._base_url)

    #     data = {
    #         "name": project_name,
    #         "public": public
    #     }

    #     with self._session.post(url, json = data) as response:

    #         self._verify_response(response, 200)

    #         return response.json()

    def close(self):

        self._session.close()

    def __exit__(self, exc_type, exc_value, traceback):

        self.close()

class KabasClientError(Exception):

    def __init__(self, error_code, error_message):

        self.error_code = error_code
        self.error_message = error_message

    def __str__(self):

        return Template("Kabas request was unsuccesful ($error_code): $error_message ").substitute(error_code = self.error_code, error_message = self.error_message)