import configparser
import os
import platform
import signal
import socket
import sys

from glob import glob

import requests
from celery import Celery, bootsteps
from celery.bin import worker as cworker
from celery.utils.log import get_logger

from .api_client import NjinnAPI
from .utils import get_config_path
from .packinstall import PackInstallation


def get_celery_app():
    worker = NjinnWorker()
    return worker.celery_app


class NjinnWorkerStep(bootsteps.StartStopStep):
    requires = {'celery.worker.components:Pool'}

    def __init__(self, worker, **kwargs):
        self.njinnworker = kwargs.get('njinnworker', self)

    def create(self, worker):
        pass

    def start(self, worker):
        """ Called when the celery worker is started """
        self.log = get_logger(__name__)
        self.log.info('Starting Njinn Worker')
        self.log.info('Using config from %s', self.njinnworker.config_path)
        self.log.info('Njinn API at %s', self.njinnworker.njinn_api.njinn_api)
        self.log.info('Worker PID %s', os.getpid())
        # Update base dependencies in all pack virtualenvs - these are worker specific
        for filename in glob("bundle_status/*/*/*"):
            try:
                installation = PackInstallation(
                    PackInstallation.identifier_from_status_filename(filename), self.njinnworker.njinn_api)
                installation.get_metadata()
                self.log.info("Updating base dependencies for pack %s", installation.display_name)
                try:
                    installation.install_requests_jwt_and_cryptography(log=self.log)
                except Exception as e:
                    self.log.warning("Could not update base dependencies for %s: %s", installation.display_name, e)
            except Exception as e:
                self.log.warning("Could not retrieve pack metadata for pack with status file %s", filename)

    def stop(self, worker):
        """ Called when the celery worker stops """
        pass


class NjinnWorker():

    def __init__(self, registration_token=None):
        # Setup worker dir as working dir
        self.working_dir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(self.working_dir)

        self.load_config()

        if not self.config_is_valid() and not registration_token:
            print("Could not find a required configuration. Please try to register the worker again.", file=sys.stderr)
            sys.exit(3)

        if not self.config_is_valid() and registration_token is not None:
            print("Registering the worker using the provided")
            self.register(registration_token)

        self.njinn_api = self.set_njinn_api()

        if not self.config_is_valid():
            print(
                "Configuration is invalid. Please contact Njinn Support.", file=sys.stderr)
            sys.exit(1)
        else:
            self.config_update()

        self.setup_logging()
        self.celery_app = self.load_celery_app()
        self.update_worker_details()

    def set_njinn_api(self):
        """
        Set the NjinnAPI class to make authenticated calls.
        """

        njinn_api = self.config['DEFAULT']['njinn_api']
        secret = self.config['DEFAULT']['secret']
        worker_name = self.config['DEFAULT']['name']

        njinn_api = NjinnAPI(njinn_api, secret, worker_name)
        return njinn_api

    def config_update(self):
        worker_name = self.config['DEFAULT']['name']
        url = f'/api/v1/workercom/config/{worker_name}'

        try:
            response = self.njinn_api.get(url)
        except requests.ConnectionError as e:
            print(
                f"Problem trying to connect to: {self.njinn_api.njinn_api}. Error: {e}", file=sys.stderr)
            sys.exit(6)

        if response.status_code != 200:
            if response.status_code == 404:
                print("Could not authenticate the worker.", file=sys.stderr)
                sys.exit(2)
            else:
                print(
                    f'Error when calling the API ({self.njinn_api.get_url(url)}). Returned with status code {response.status_code}: {response.text}', file=sys.stderr)
                sys.exit(9)
        else:
            self.config['DEFAULT']['id'] = str(response.json()['id'])
            self.config['DEFAULT']['name'] = response.json()['name']
            self.config['DEFAULT']['queues'] = response.json()['queues']
            self.config['DEFAULT']['messaging_url'] = response.json()[
                'messaging_url']
            self.config['DEFAULT']['secrets_key'] = response.json()[
                'secrets_key']

        self.save_config_to_file()

    def register(self, registration_token):
        try:
            name = self.config['DEFAULT']['name']
        except KeyError:
            name = None

        if not name:
            name = socket.gethostname()
            self.config['DEFAULT']['name'] = name

        api_base = os.environ.get('NJINN_URL', 'https://api.njinn.io')
        if api_base.endswith("/"):
            api_base = api_base[:-1]
        url = api_base + '/api/v1/workercom/register'

        data = {
            "registration_token": registration_token,
            "name": name
        }
        try:
            response = requests.post(url, data)
        except requests.ConnectionError as e:
            print(
                f"Problem trying to connect to: {api_base}. Error: {e}", file=sys.stderr)
            sys.exit(6)

        if response.status_code != 200:
            if response.status_code == 401:
                print("The provided registration key is invalid.", file=sys.stderr)
                sys.exit(5)
            else:
                print(
                    f'Error when calling the API ({url}). Returned with status code {response.status_code}: {response.text}', file=sys.stderr)
                sys.exit(9)
        else:
            self.config['DEFAULT']['njinn_api'] = 'https://' \
                + response.json()['domain_url']
            self.config['DEFAULT']['secret'] = response.json()['secret']
            self.config['DEFAULT']['name'] = response.json()['name']

        self.save_config_to_file()

    def save_config_to_file(self):
        try:
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)
        except OSError:
            print("Could not write to the configuration file.", file=sys.stderr)
            sys.exit(4)

    def config_is_valid(self):
        api = self.config.get('DEFAULT', 'njinn_api', fallback='')
        secret = self.config.get('DEFAULT', 'secret', fallback='')
        name = self.config.get('DEFAULT', 'name', fallback='')

        if not api.strip() or not secret.strip() or not name.strip():
            return False

        return True

    def load_config(self):

        self.config_path = get_config_path()

        config_dir = os.path.dirname(os.path.realpath(self.config_path))
        os.makedirs(config_dir, exist_ok=True)

        config = configparser.ConfigParser()
        config.read(self.config_path)

        config['DEFAULT']['njinn_api'] = os.getenv(
            "NJINN_WORKER_API", config.get('DEFAULT', 'njinn_api', fallback=''))
        config['DEFAULT']['secret'] = os.getenv(
            "NJINN_WORKER_SECRET", config.get('DEFAULT', 'secret', fallback=''))
        config['DEFAULT']['name'] = os.getenv(
            "NJINN_WORKER_NAME", config.get('DEFAULT', 'name', fallback=''))

        self.config = config
        self.save_config_to_file()

        return config

    def setup_logging(self):
        if not self.config.has_section('logging'):
            self.config.add_section('logging')
            log_conf = self.config['logging']
            log_conf['log_level'] = 'INFO'
            self.save_config_to_file()

    def update_worker_details(self):
        worker_id = self.config['DEFAULT']['id']
        url = f'/api/v1/workers/{worker_id}'

        platform_info = os.getenv("NJINN_WORKER_PLATFORM",
                                  f"{platform.system()} ({platform.release()})")

        data = {
            "platform": platform_info
        }

        try:
            response = self.njinn_api.patch(url, data)
        except requests.ConnectionError as e:
            print(
                f"Problem trying to connect to: {self.njinn_api.njinn_api}. Error: {e}", file=sys.stderr)
            sys.exit(6)

        if response.status_code != 200:
            print(
                f'Error when calling the API ({self.njinn_api.get_url(url)}). Returned with status code {response.status_code}: {response.text}', file=sys.stderr)
            sys.exit(9)

    def load_celery_app(self):
        app = Celery('NjinnWorker')
        app.steps['worker'].add(NjinnWorkerStep)

        broker_url = self.config['DEFAULT']['messaging_url']

        app.conf.update(
            enable_utc=True,
            accept_content=['json'],
            imports=('worker.tasks',),
            broker_url=broker_url
        )

        return app

    def start(self):
        conf = self.config['DEFAULT']
        hostname = conf.get('name', 'worker@%%n')
        queues = conf.get('queues', 'default')
        pidfile = conf.get('pid_file', './worker.pid')

        loglevel = self.config['logging'].get('log_level')

        celery_worker = cworker.worker(app=self.celery_app)
        options = {
            'optimization': 'fair',
            'O': 'fair',
            'queues': queues,
            'loglevel': loglevel,
            'hostname': hostname,
            'njinnworker': self,
            'pidfile': pidfile
        }

        def sigint_handler(sig, frame):
            sys.exit(0)

        signal.signal(signal.SIGINT, sigint_handler)
        signal.signal(signal.SIGTERM, sigint_handler)

        celery_worker.run(**options)


def main():
    # windows celery fix: https://github.com/celery/celery/issues/4081
    os.environ["FORKED_BY_MULTIPROCESSING"] = "1"
    os.environ["GIT_TERMINAL_PROMPT"] = "0"

    registration_token = sys.argv[1] if len(
        sys.argv) > 1 else os.getenv("NJINN_WORKER_TOKEN")
    print("Config file:", get_config_path())
    worker = NjinnWorker(registration_token=registration_token)
    print("Working Directory:", worker.working_dir)
    worker.start()


if __name__ == "__main__":
    main()
