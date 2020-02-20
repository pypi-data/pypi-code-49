# -*- coding: utf-8 -*-
"""SecretManager Class file."""

import base64

from bits.google.services.base import Base
from google.cloud import secretmanager_v1beta1
from google.protobuf import json_format
from googleapiclient.discovery import build


class SecretManager(Base):
    """SecretManager class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        # google-python-api-client
        self.credentials = credentials
        self.sm = build('secretmanager', 'v1beta1', credentials=credentials)

        # google-cloud-secret-manager
        self.secretmanager_v1beta1 = secretmanager_v1beta1
        self.client = secretmanager_v1beta1.SecretManagerServiceClient()
        self.json_format = json_format

    #
    # Secrets
    #
    def add_version(self, parent, secret_id, text):
        """Add a Secret Version."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        name = '{}/{}'.format(parent, secret_id)

        secret = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        body = {
            'payload': {
                'data': secret,
            }
        }
        params = {
            'parent': name,
            'body': body,
        }
        return self.sm.projects().secrets().addVersion(**params).execute()

    def create_secret(self, parent, secret_id, labels=None, locations=None):
        """Create a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        # check for replica locations
        if locations:
            replicas = []
            for location in locations:
                replicas.append({'location': location})
            body = {'replication': {'userManaged': {'replicas': replicas}}}
        else:
            body = {'replication': {'automatic': {}}}
        # check for labels
        if labels:
            body['labels'] = labels
        params = {
            'parent': parent,
            'body': body,
            'secretId': secret_id,
        }
        return self.sm.projects().secrets().create(**params).execute()

    def delete_secret(self, parent, secret_id):
        """Delete a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        name = '{}/{}'.format(parent, secret_id)
        return self.sm.projects().secrets().delete(name=name).execute()

    def get_iam_policy(self, parent, secret_id):
        """Return the IAM Policy for a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        name = '{}/{}'.format(parent, secret_id)
        return self.sm.projects().secrets().getIamPolicy(resource=name).execute()

    def get_secret(self, parent, secret_id):
        """Return a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        name = '{}/{}'.format(parent, secret_id)
        return self.sm.projects().secrets().get(name=name).execute()

    def get_secrets(self, parent):
        """List Secrets in a Project."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        secrets = self.sm.projects().secrets()
        request = secrets.list(parent=parent)
        return self.get_list_items(secrets, request, 'secrets')

    def patch_secret(self, parent, secret_id, body, update_mask=None):
        """Patch a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        name = '{}/{}'.format(parent, secret_id)
        params = {
            'name': name,
            'body': body,
            'updateMask': update_mask,
        }
        return self.sm.projects().secrets().patch(**params).execute()

    def set_iam_policy(self, parent, secret_id, body):
        """Return the IAM Policy for a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        name = '{}/{}'.format(parent, secret_id)
        return self.sm.projects().secrets().setIamPolicy(resource=name, body=body).execute()

    #
    # Versions
    #
    def access_version(self, parent, secret_id, version='latest'):
        """Return a Version of a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        if 'versions/' not in version:
            version = 'versions/{}'.format(version)
        name = '{}/{}/{}'.format(parent, secret_id, version)
        return self.sm.projects().secrets().versions().access(name=name).execute()

    def access_version_value(self, parent, secret_id, version='latest'):
        """Return the string value of a Version of a Secret."""
        version = self.access_version(parent, secret_id, version)
        payload_data = version['payload']['data']
        return base64.b64decode(payload_data.encode('utf-8')).decode('utf-8')

    def destroy_version(self, parent, secret_id, version):
        """Destroy a Version of a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        if 'versions/' not in version:
            version = 'versions/{}'.format(version)
        name = '{}/{}/{}'.format(parent, secret_id, version)
        return self.sm.projects().secrets().versions().destroy(name=name).execute()

    def disable_version(self, parent, secret_id, version):
        """Disable a Version of a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        if 'versions/' not in version:
            version = 'versions/{}'.format(version)
        name = '{}/{}/{}'.format(parent, secret_id, version)
        return self.sm.projects().secrets().versions().disable(name=name).execute()

    def enable_version(self, parent, secret_id, version):
        """Enable a Version of a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        if 'versions/' not in version:
            version = 'versions/{}'.format(version)
        name = '{}/{}/{}'.format(parent, secret_id, version)
        return self.sm.projects().secrets().versions().enable(name=name).execute()

    def get_version(self, parent, secret_id, version):
        """Return a Version of a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        if 'versions/' not in version:
            version = 'versions/{}'.format(version)
        name = '{}/{}/{}'.format(parent, secret_id, version)
        return self.sm.projects().secrets().versions().get(name=name).execute()

    def get_versions(self, parent, secret_id):
        """List Versions of a Secret."""
        if 'projects/' not in parent:
            parent = 'projects/{}'.format(parent)
        if 'secrets/' not in secret_id:
            secret_id = 'secrets/{}'.format(secret_id)
        name = '{}/{}'.format(parent, secret_id)
        versions = self.sm.projects().secrets().versions()
        request = versions.list(parent=name)
        return self.get_list_items(versions, request, 'versions')
