import os
from datetime import datetime
import json
import logging
import argparse

import requests


class UnityCloudException(Exception):
    pass


class UnityCloud:
    def __init__(self, org_id, project_name):
        self.base_url = 'https://build-api.cloud.unity3d.com/api/v1'
        self.api_key = os.getenv("UNITY_API_KEY")
        if not self.api_key:
            raise UnityCloudException("setup UNITY_API_KEY env var")
        self.auth_headers = {
            'Authorization': 'Basic ' + self.api_key
        }
        self.org_id = org_id
        self.project_name = project_name
        self.project_id = None
        self._set_project_id()
        self.build_targets = None

    def run_build(self, target_name, clean=False):
        self._set_targets()
        target_id = self._get_target_id(target_name)
        url = f'{self.base_url}/orgs/{self.org_id}/projects/{self.project_id}/buildtargets/{target_id}/builds'
        data = {
            "clean": clean
        }
        resp = requests.post(url, headers=self.auth_headers, json=data)
        if resp.status_code == 202:
            raise UnityCloudException("Cant create build")


    def list_projects(self):
        url = f'{self.base_url}/orgs/{self.org_id}/projects'
        req = requests.get(url, headers=self.auth_headers)
        return req.json()

    def upload_ios_credentials(self, cert_file, prov_file, cert_secret):
        url = f'{self.base_url}/orgs/{self.org_id}/projects/{self.project_id}/credentials/signing/ios'
        label = f'{datetime.now().strftime("%Y-%m-%d")}-{self.project_name}'
        print(url)
        print(label)
        files = {
            'fileCertificate': open(cert_file, 'rb'),
            'fileProvisioningProfile': open(prov_file, 'rb')
        }
        data = {
            "label": label,
            "certificatePass": cert_secret,
        }
        resp = requests.post(url, data=data, files=files, headers=self.auth_headers)
        if resp.status_code != 201:
            raise UnityCloudException("Error create iOS credentials")
        return resp.json()["credentialid"]

    def update_ios_app_creds(self, target_name, creds_id):
        if not self.build_targets:
            self._set_targets()
        buildtargetid = self._get_target_id(target_name)
        print(f"target_name:{target_name}, target_id: {buildtargetid}")
        # PUT /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}
        url = f'{self.base_url}/orgs/{self.org_id}/projects/{self.project_id}/buildtargets/{buildtargetid}'
        headers = self.auth_headers
        headers.update({
            'Content-Type': 'application/json'
        })
        data = {
            "credentials": {
                "signing": {
                    "credentialid": creds_id
                }
            }
        }
        req = requests.put(url, json=data, headers=headers)
        if req.status_code != 200:
            logging.error(req.json())
            raise UnityCloudException("Error update apps creds")

    def _get_target_id(self, target_name):
        return [bt for bt in self.build_targets if bt['name'] == target_name][0]["buildtargetid"]
        
    def _set_targets(self):
        url = f'{self.base_url}/orgs/{self.org_id}/projects/{self.project_id}/buildtargets'
        req = requests.get(url, headers=self.auth_headers)
        self.build_targets = req.json()

    def _set_project_id(self):
        projects = self.list_projects()
        self.project_id = [p for p in projects if p['name'] == self.project_name][0]["projectid"]


def run_build():
    parser = argparse.ArgumentParser()
    parser.add_argument('--org-id', required=True)
    parser.add_argument('--project', required=True)
    parser.add_argument('--target', required=True)
    parser.add_argument('--clean', default=False)
    args = parser.parse_args()
    uc = UnityCloud(args.org_id, args.project)
    uc.run_build(args.target, clean=args.clean)
