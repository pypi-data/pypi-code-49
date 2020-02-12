import requests
import yaml

__version__ = '0.0.1'


class ApiClient(object):

    def __init__(self, url, version='api'):

        if not url:
            raise RuntimeError('WAVES_URL environment variable not set')

        self.waves_url = url
        self.api_version = version
        self.session = requests.Session()
        # login salvando token

    def register_businesstask(self, btask_content):
        url = self._build_url('business-tasks')
        response = requests.post(
            url,
            headers=self._get_headers(),
            data=btask_content.encode('utf-8'))
        if not response.status_code == 201:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()

    def publish_businesstask(self, btask_content):

        definition = yaml.load(btask_content, Loader=yaml.FullLoader)
        identifier = '{}@{}'.format(
            definition.get('name'), definition.get('version', 'latest'))

        url = self._build_url('business-tasks/{}/publish'.format(identifier))

        response = requests.put(
            url,
            headers=self._get_headers())

        if not response.status_code == 200:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()

    def create_workflow(self, workflow_content):
        url = self._build_url('workflows')
        response = requests.post(
            url,
            headers=self._get_headers(),
            data=workflow_content.encode('utf-8'))
        if not response.status_code == 201:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()

    def run(self, workflow_identifier, inputs):
        """
        Create a new execution for the workflow identifier
        """
        url = self._build_url('executions')
        new_execution = {
            "workflow_identifier": workflow_identifier,
            "inputs": inputs,
        }
        response = requests.post(
            url,
            headers=self._get_headers(content_type='application/json'),
            json=new_execution)

        if not response.status_code == 201:
            return "Erro : {}: {}".format(response, response.content)
        return response.json()

    def list_workers(self):
        """
        list active workers
        """
        url = self._build_url('workers')
        response = requests.get(
            url,
            headers=self._get_headers(),
        )

        if not response.status_code == 200:
            return "Erro: {}: {}".format(response, response.content)
        return response.json()

    def _get_headers(self, content_type='application/x-yaml'):
        headers = {
            'User-Agent': 'wavescli/{}'.format(__version__),
            'Content-Type': content_type,
        }
        # token = getattr(self, 'token', None)
        # if token:
        #     headers['Authorization'] = token
        return headers

    def _build_url(self, endpoint):
        return '/'.join([self.waves_url, self.api_version, endpoint])


class ApiError(RuntimeError):

    def __init__(self, response):
        message = 'status={} data={}'.format(
            response.status_code, response.json())
        super(ApiError, self).__init__(message)
