# -*- coding: utf-8 -*-
"""Class file for settings."""

import json
import sys
import yaml

from bits.google import Google
from oauth2client import client
from googleapiclient.errors import HttpError

google = Google()


class Settings(object):
    """Settings class."""

    def __init__(
        self,
        bucket=None,
        filename='etc/config.yaml',
        verbose=False
    ):
        """Initialize a Settings class instance."""
        self.default_bucket = bucket
        self.filename = filename
        self.verbose = verbose

        # read settings from local config file
        self.local_settings = self.read_local_config()

        # get configuration
        self.configuration = self.local_settings.get('configuration')
        self.type = self.get_configuration_type()

        # display configuration
        if self.verbose:
            self.display_configuration()

        # generating settings based on config
        self.settings = self.generate_settings()

    def display_configuration(self):
        """Display the configuration."""
        print('Configuration:')
        print(json.dumps(self.configuration, indent=2, sort_keys=True))

    def generate_settings(self):
        """Generate settings based on config."""
        # pull all settings from local config, ignore cloud
        if self.type == 'local':
            settings = self.local_settings

        # pull all settings from cloud based on app/environment
        elif self.type == 'cloud':
            settings = self.get_cloud_settings()

        # use local config as template and pull settings from master cloud config
        elif self.type == 'template':
            settings = self.get_template_settings()

        # unknown type, fail
        else:
            error = 'ERROR: Unsupported type: %s' % (self.type)
            sys.exit(error)

        return settings

    def get(self, key=None):
        """Return the settings."""
        # if a key is provided, only provide the settings for that key
        if key:
            return self.settings.get(key, {})
        # otherwise, provide all settings
        return self.settings

    def get_cloud_settings(self):
        """Return the settings from the cloud based on the local config."""
        # get the cloud configuration
        app = self.configuration.get('app')
        bucket = self.configuration.get('bucket')
        environment = self.configuration.get('environment')
        # set the object name based on the app end environment
        objectName = '%s-%s/config.yaml' % (app, environment)
        # create the path using the bucket and object name
        path = 'gs://%s/%s' % (bucket, objectName)
        # authenticate with google application default credentials
        google.credentials = self.get_google_credentials()
        try:
            # get the contents of the object
            media = google.storage().get_object_media(bucket, objectName)
            # return the yaml as a dictionary
            return self.parse_yaml(media.getvalue())
        except HttpError as e:
            print('ERROR: Failed to get settings object: %s' % (path))
            print(e)

    def get_configuration_type(self):
        """Return the configuration type."""
        # default type is local if not specified
        if 'configuration' not in self.local_settings:
            return 'local'
        return self.configuration.get('type', 'local')

    def get_master_settings(self):
        """Return the master settings file."""
        # use default bucket name if not found in config
        bucket = self.configuration.get('bucket', self.default_bucket)
        # set the object name to the master config file
        objectName = 'master/config.yaml'
        # set path based on bucket/objectName
        path = 'gs://%s/%s' % (bucket, objectName)
        # authenticate with googel application default credentials
        google.credentials = self.get_google_credentials()
        try:
            # get contents of the object
            media = google.storage().get_object_media(bucket, objectName)
            # return the yaml as a dictionary
            return self.parse_yaml(media.getvalue())
        except HttpError as e:
            print('ERROR: Failed to get settings object: %s' % (path))
            print(e)

    def get_google_credentials(self):
        """Return application default credentials."""
        scopes = ['https://www.googleapis.com/auth/cloud-platform']
        credentials = client.GoogleCredentials.get_application_default()
        credentials = credentials.create_scoped(scopes)
        return credentials

    def get_template_settings(self):
        """Return the settings processed as a template from a master."""
        # get the master settings from the bucket
        master = self.get_master_settings()
        # apply the local template to the master settings
        return self.parse_template(master)

    def get_template_value(self, app, template, master):
        """Return the right settings for a given template value."""
        # apps with just one config
        if 'config' in template:
            config = template.get('config')
            keys = config.split('.')
            for k in keys:
                # skip the local config entry
                if k == 'configuration':
                    continue
                if k in master:
                    master = master[k]
                else:
                    print('WARNING: Key "{}" not found in master config!'.format(k))
            return master
        # apps with multiple configs
        else:
            parent = {}
            for s in template:
                config = template[s].get('config')
                keys = config.split('.')
                server = master.copy()
                for k in keys:
                    try:
                        server = server[k]
                    except Exception as e:
                        print('ERROR: No such configuration item: %s' % (config))
                        print(e)
                parent[s] = server
            return parent

    def read_local_config(self):
        """Read the initial config from a local file."""
        # open the local config file
        f = open(self.filename, 'r')
        try:
            # return the yaml as a dictionary
            return self.parse_yaml(f)
        except Exception as e:
            print('ERROR reading configuration from: %s! Exiting.' % (
                self.filename
            ))
            print(e)

    def parse_template(self, master):
        """Return a parsed template config file."""
        settings = {}
        for app in self.local_settings:
            # skip the configuration item as that is only for local
            # we should probably move all the other options down so
            # there are only "configuration" and "template" at the top level
            if app == 'configuration':
                settings[app] = self.local_settings['configuration']
                continue
            template = self.local_settings[app]
            settings[app] = self.get_template_value(app, template, master)
        return settings

    def parse_yaml(self, stream):
        """Parse a stream of YAML."""
        # yaml docs
        docs = yaml.load_all(stream, Loader=yaml.Loader)
        # settings
        settings = {}
        for doc in docs:
            for key, value in doc.items():
                settings[key] = value
        return settings
