from collections import namedtuple

from kubernetes import client, config
from k9.pretty_object import PrettyObject

from datetime import datetime, timezone
import os
import pprint
import subprocess
import time
import yaml

po = PrettyObject()
config.load_kube_config()

v1_core = client.CoreV1Api()

default_namespace = None


###########################################################################
# Utility Functions
###########################################################################
CommandResult = namedtuple('CommandResult', 'args returncode stdout stderr')
output_on = True


def set_run_output(output_mode=True):
    """
    Sets flag to indicate whether outputs from the run_command should be printed
    to the console or not.
    :param output_mode: True if stdout should be printed to console.  Default is True
    """
    global output_on
    output_on = output_mode


def run_command(*params):
    """
    This is a helper function to make it easier to run shell commands in
    a consistent manner.

    Calls the subprocess.run() command with the following options:

    capture_output=True  Which provides **stdout** and **stderr**
    check=True           Which throws an exception if an error occurs.  The exception
                         type `subprocess.CalledProcessError <https://docs.python.org/3/library/subprocess.html#subprocess.SubprocessError>`_

    :param params: a variable list of parameters
    :return: A named tuple version of `subprocess.CompletedProcess <https://docs.python.org/3/library/subprocess.html>`_
             that translates the stdout and stderr with str( 'utf-8')

    Example Call::
        result = run_command('ls', '-la')
        print(f'result.args: {result.args}')
        print(f'result.returncode: {result.returncode}')
        print(f'result.stdout: {result.stdout}')
        print(f'result.stderr: {result.stderr}')


    """
    result = subprocess.run(params, capture_output=True, check=True)

    stdout = ""
    if result.stdout:
        stdout = str(result.stdout, 'utf-8')
        if output_on:
            print(stdout)

    stderr = ""
    if result.stderr:
        stderr = str(result.stderr, 'utf-8')

    return CommandResult(
        args=result.args,
        returncode=result.returncode,
        stdout=stdout,
        stderr=stderr
    )

def last_word(value: str):
    """
    Splits out the word after the last slash in a string.  K8
    objects are expressed in a path style name

    Example
    -------

    >>> last_word('pods/my-pod')
    'my-pod'
    """
    return value.split('/')[-1:][0]


def view_yaml(fn: str):
    """
    Dumps out yaml file in JSON format for easy viewing. This
    is useful when constructing the body of a request that matches a known yaml format.

    Example
    -------

    >>> view_yaml('tomcat-deploy-dev.yml')
    """
    file = None
    try:
        file = open(fn)
        pprint.pprint(yaml.safe_load(file))

    finally:
        if file is not None:
            file.close()


def read_yaml(fn: str):
    """
    Reads a YAML file and returns the resulting the object.

    Example
    -------

    >>> read_yaml('tomcat-deploy-dev.yml')

    """
    file = None
    try:
        file = open(fn)
        return yaml.safe_load(file)

    finally:
        if file is not None:
            file.close()


def get_age(creation_time: datetime):
    """
    Given a creation timestamp, return the difference in time from now.

    :param creation_time: The time we want to measure age from
    :return: timedelta - the amount of time since creation_time
    """
    now = datetime.now(timezone.utc)
    delta = now - creation_time

    if delta.days > 0:
        return f'{delta.days}d'

    hours = delta.seconds/3600

    seconds = delta.seconds%3600

    minutes = seconds/60
    seconds = seconds % 60

    return '%02d:%02d:%02d' % (hours, minutes, seconds)


def abs_path(file: str):
    """
    Sets an absolute path relative to the **k9** package directory.

    Example::
        result = abs_path('myfile)

    Result::
        /Users/simon/git/k9/k9/myfile


    This is used primarily for building unit tests within the K9 package
    and is not expected to be useful to K9 library users.

    :param file: File or directory to attach absolute path with
    :return: absolute path to specified file or directory
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, file)

###########################################################################
# Namespaces
###########################################################################

def set_default_namespace(namespace: str = None):
    """
    Sets the default namespace for all functions that need namespace.

    Most of the functions in this library will require a namespace parameter.
    If the namespace is not provided, the default namespace you set will
    be used instead, simplifying the call.

    Typically, this should be one of the first calls you make when
    working with this library.

    :param: The name of the default namespace. If none, we use "default"
    """
    global default_namespace
    if namespace is None:
      namespace = 'default'
    default_namespace = namespace


def get_default_namespace():
    """
    Gets the default namespace set using set_default_namespace().

    :return: The default namespace's name
    """
    global default_namespace
    if default_namespace is None:
        raise Exception("You must call set_default_namespace() first before using most of the K9 API functions.")

    return default_namespace


def list_namespaces():
    """
    Retrieves a list of namespaces and associated status.  Returns same
    information as `kubectl get namespaces`

    :return: list of dictionaries with **name** and **status**
    """

    return [
        {
            'name': namespace.metadata.name,
            'status': namespace.status.phase,
            'age': get_age(namespace.metadata.creation_timestamp)
        }
        for namespace in v1_core.list_namespace().items
    ]

def get_namespace(namespace: str = None):
    """
    Gets an object that holds detailed information about the supplied namespace.

    :param namespace: Namespace to retrieve.  If None, will use default namespace.
    :return: `V1Namespace <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Namespace.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_core.read_namespace(namespace)


def namespace_exists(namespace: str = None):
    """
    Determines if the specified namespace exists.

    :param namespace: The namespace to check for.  If None, then the default namespace is used.
    :return: bool - True if namespace exists
    """
    try:
        if namespace is None:
            namespace = get_default_namespace()

        result = get_namespace(namespace)
        return result.status.phase == 'Active' and result.metadata.name == namespace

    except:
        return False

def create_namespace(namespace: str = None):
    """
    Creates the specified namespace.

    :param namespace: Specifies the namespace to create.  If None, then the default namespace is used.
    :return: `V1Namespace <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Namespace.md>`_
    """

    if namespace is None:
        namespace = get_default_namespace()

    body = \
        {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": namespace,
            }
        }

    return v1_core.create_namespace(body)

def delete_namespace(namespace: str = None):
    """
    Deletes the specified namespace.

    :param namespace: Namespace to delete.  If None, the default namespace is used.
    :return: None if namespace doesn't exist, otherwise `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if not namespace_exists(namespace):
        return None

    result = v1_core.delete_namespace(namespace)

    # wait for namespace to be gone
    try:
        while get_namespace(namespace) is not None:
           time.sleep(1)

    except client.rest.ApiException as e:
        # spec found here: https://github.com/kubernetes-client/python/blob/master/kubernetes/client/rest.py
        if not "Not Found" in e.reason:
            raise


###########################################################################
# Nodes
###########################################################################

def list_nodes():
    """
    Retrieve a list of nodes
    
    :return: Return a list of nodes - each node represented by a dictionary with **name**, **status**, **ip**, **label**, **reason**, and **start_time**
    """
    return [
        {
            'name': node.metadata.name,
            'status': node.status.phase,
            'info': node.status.node_info
        }
        for node in v1_core.list_node().items
    ]

def get_node(name: str):
    """

    :param name: The name of the node
    :return: Return information related to the node
    """
    selector = 'metadata.name=' + name
    return [
        {
            'name': node.metadata.name,
            'status': node.status.phase,
            'info': node.status.node_info
        }

        for node in v1_core.list_node(field_selector=selector).items
    ]

###########################################################################
# Pods
###########################################################################

def list_pods(namespace: str = None):
    """
    List all pods in a given namespace

    :param namespace: Namespace to search.  If None, uses the default namespace
    :return: Returns a list of pods - each pod represented by a dictionary with **name**, **status**, **ip**, **node**, **labels**, **reason**, and **start_time**
    """
    if namespace is None:
        namespace = get_default_namespace()

    pod_list = v1_core.list_namespaced_pod(namespace)
    return [
        {
            'name': pod.metadata.name,
            'status': pod.status.phase,
            'ip': pod.status.pod_ip,
            'labels': pod.metadata.labels,
            'reason': pod.status.reason,
            'node': pod.spec.node_name,
            'age': get_age(pod.status.start_time)
        }
        for pod in pod_list.items
    ]

def copy_to_pod(pod: str, host_fn: str, dest_fn: str, namespace: str = None):
    """
    Copies a file to the specified pod.
    
    Example::
        copy_to_pod('jenkins-12345', '.output/jenkins_config.xml', '/var/jenkins_home/some_config.xml')
    
    :param pod: The name of the pod you're copying the file into
    :param namespace: The namespace the pod is found in (if not present, we search in the default ns)
    :param host_fn: The filename, relative to the execution folder
    :param dest_fn: The desired location + filename on the pod.

    This function doesn't return anything if successful. It throws errors if the file does not exist on the host, the file already exists on the pod, or if the pod name is invalid.
    """
    try:
        if not namespace:
            namespace = get_default_namespace()
        run_command('kubectl', 'cp', host_fn, f'{namespace}/{pod}:{dest_fn}')
    except Exception as e:
        print(e)

def copy_from_pod(pod: str, host_fn: str, dest_fn: str, namespace: str = None):
    """
    This is used for copying a file from inside a pod to the host machine.
    
    Example::
        copy_from_pod('jenkins-12345', '/var/jenkins_home/some_config.xml', '.output/jenkins_config.xml')

    :param pod: The name of the pod you're copying the file from
    :param namespace: The namespace the pod is found in (if not present, we search in the default ns)
    :param host_fn: The location + filename on the pod.
    :param dest_fn: The destination file relative to the folder we're executing from.

    This function doesn't return anything if successful. It throws errors if the pod or file (on the pod) doesn't exist. This overwrites files on the host machine, unlike copy_to_pod()
    """
    try:
        if not namespace:
            namespace = get_default_namespace()
        run_command('kubectl', 'cp', f'{namespace}/{pod}:{host_fn}', dest_fn)
    except Exception as e:
        print(e)

def wait_for_pod(pod: str, namespace: str = None, interval: int = 10, timeout: int = 240):
    """
    Waits for a pod to be ready. Generally used when we need to use an API or get a file to/from the pod for configuration.

    Example::
        wait_for_pod('jenkins-asdf123')
    
    :param pod: The name of the pod we're waiting on
    :param namespace: The namespace the pod is found in (if not present, we search in the default ns)
    :param interval: How long to wait between checks (in seconds)
    :param timeout: How many seconds to wait (in total) before timing out the operation

    :return: If the pod is ready/running (True) or if it isn't ready by the timeout (False)
    """
    time.sleep(5)
    status = 'NotRunning'
    for i in range(timeout // interval + 1):
        pods = list_pods(namespace)
        for p in pods:
            if p['name'] == pod:
                status = p['status']
        if status == 'Running':
            return True
        if i <= timeout // interval:
            print(f'waiting for {pod} to be ready')
            time.sleep(interval)
    return False

###########################################################################
# Secrets
###########################################################################

def list_secrets(namespace: str = None):
    """
    Lists secrets in a given namespace.

    :param namespace: Namespace you want to search.  If None, the default namespace is used.
    :return: A list of dictionaries with **name**, **type**, **data** (for number of entries), and **age**
    """
    if namespace is None:
        namespace = get_default_namespace()

    return [
        {
            'name': secret.metadata.name,
            'type': secret.type,
            'data': len(secret.data),
            'age': get_age(secret.metadata.creation_timestamp)
        }
        for secret in v1_core.list_namespaced_secret(namespace).items
    ]


def secret_exists(name: str, namespace: str = None):
    """
    Determines if a secret exists.

    :param name: Name of secret
    :param namespace: Namespace to search, if None, uses default namespace
    :return: True if specfied secret exists.
    """
    if namespace is None:
        namespace = get_default_namespace()

    try:
        result = get_secret(name, namespace)
        return result.metadata.name == name

    except:
        return False


def get_secret(name: str, namespace: str = None):
    """
    Gets a secret's metadata and value(s).

    :param name: Name of secret
    :param namespace: Namespace to search, if None, uses default namespace
    :return: None if not found, otherwise `V1Secret <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Secret.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_core.read_namespaced_secret(name, namespace)


def create_secret(name: str, secrets: dict, namespace: str = None):
    """
    Creates a secret.

    :param name: Name of secret
    :param secrets: Dictionary containing name value pairs of secrets
    :param namespace:
    :return: `V1Secret <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Secret.md>`_

    Example::

        # Note that you should not embed secrets in your source code, this is
        # simply to illustrate how the function call works.
        secret_name = "tomcat-dev"
        secrets = {
            'ds-url': 'https://some/url',
            'password': 'My1SecretPassword',
            'username': 'postgres'
        }

        # Test create_secret()
        result = create_secret(secret_name, secrets)

    Output::

        {'api_version': 'v1',
         'data': {'ds-url': 'aHR0cHM6Ly9zb21lL3VybA==',
                  'password': 'TXkxU2VjcmV0UGFzc3dvcmQ=',
                  'username': 'cG9zdGdyZXM='},
         'kind': 'Secret',
         'metadata': {'annotations': None,
                      'cluster_name': None,
                      'creation_timestamp': datetime.datetime(2019, 10, 17, 17, 20, 56, tzinfo=tzutc()),
                      'deletion_grace_period_seconds': None,
                      'deletion_timestamp': None,
                      'finalizers': None,
                      'generate_name': None,
                      'generation': None,
                      'initializers': None,
                      'labels': None,
                      'managed_fields': None,
                      'name': 'tomcat-dev',
                      'namespace': 'default',
                      'owner_references': None,
                      'resource_version': '2053051',
                      'self_link': '/api/v1/namespaces/default/secrets/tomcat-dev',
                      'uid': '7ab378c0-f102-11e9-a715-025000000001'},
         'string_data': None,
         'type': 'Opaque'}
    """
    if namespace is None:
        namespace = get_default_namespace()

    body = client.V1Secret()
    body.api_version = 'v1'
    body.kind = 'Secret'
    body.metadata = {'name': name}
    body.string_data = secrets
    body.type = 'Opaque'

    return v1_core.create_namespaced_secret(namespace, body)


def delete_secret(name: str, namespace: str = None):
    """
    Delete specified secret.

    :param name: Name of secret to delete.
    :param namespace: Namespace to delete from.  If None, default namespace is used.
    :return: `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_ if secret exists, if not, None.
    """
    if namespace is None:
        namespace = get_default_namespace()

    if secret_exists(name, namespace):
        return v1_core.delete_namespaced_secret(name, namespace)
    else:
        return None


###########################################################################
# Services
###########################################################################

def list_services(namespace: str = None):
    """
    Lists the services in the namespace.

    :param namespace: Namespace to list services from.  If None, default namespace will be used.
    :return: List of dictionaries with **name**, **type**, **cluster-ip**, **external-ips**, **ports**, and **age**
    """
    if namespace is None:
        namespace = get_default_namespace()

    return [
        {
            'name': svc.metadata.name,
            'type': svc.spec.type,
            'cluster-ip': svc.spec.cluster_ip,
            'external-ips': svc.spec.external_i_ps,
            'ports': [
                f'{port.target_port}/{port.protocol}'
                for port in svc.spec.ports
            ],
            'age': get_age(svc.metadata.creation_timestamp)
        }
        for svc in v1_core.list_namespaced_service(namespace).items
    ]


def service_exists(name: str, namespace: str = None):
    """
    Checks existence of specified service.

    :param name: Name of service.
    :param namespace: Namespace to get service from.  If None, will use default namespace.
    :return: True if service exists.
    """
    if namespace is None:
        namespace = get_default_namespace()
    try:
        result = get_service(name, namespace)

        return result.metadata.name == name
    except:

        return False;

def get_service(name: str, namespace: str = None):
    """
    Retrieves details on the specified service.

    :param name: Name of service to get.
    :param namespace: Namespace to get service from.  If None, will use default namespace.
    :return: `V1Service <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Service.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_core.read_namespaced_service(name, namespace)

def create_service(body: dict, namespace: str = None):
    """
    Creates a service based on definition provided by **body**.

    :param body:  Service description: https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Service.md
    :param namespace: Namespace to create service in.  If None, will use default namespace.
    :return: `V1Service <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Service.md>`_

    You'll most likely create a YAML file to describe your service and read that in.  You can use
    read_yaml() to generate the body as follows:

    Example::

        result = create_service(read_yaml('my-service.yaml'))

    Sample YAML file::

        apiVersion: v1
        kind: Service
        metadata:
          name: tomcat-svc-dev
          labels:
                svc: tomcat
                env: dev
        spec:
          type: ClusterIP
          ports:
          - port: 8080
            targetPort: 8080
            protocol: TCP
          selector:
                app: tomcat
                env: dev
    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_core.create_namespaced_service(namespace=namespace, body=body)


def delete_service(name: str, namespace: str = None):
    """
    Deletes the specified service.  This function will check whether the service exists before attempting the delete.

    :param name: Name of service to delete
    :param namespace: Namespace to delete from.  If None, default namespace is used.
    :return: None if service doesn't exist, otherwise `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if service_exists(name, namespace):
        return v1_core.delete_namespaced_service(name, namespace)
    else:
        return None



###########################################################################
# Service Accounts
###########################################################################

def list_service_accounts(namespace: str = None):
    """
    Lists service accounts in a namespace.

    :param namespace: The namespace to list accounts from. If None, we use the default namespace.
    :return: A list of every service account in the namespace.

    Example Output::
    
        [
          {
            'name': 'elastic-sa',
            'age': 123456789
          },
          {
            'name': 'fluent-sa',
            'age': 123456999
          }
        ]
    """
    if namespace is None:
        namespace = get_default_namespace()

    result = v1_core.list_namespaced_service_account(namespace)

    return [
        {
            'name': sa.metadata.name,
            'age': get_age(sa.metadata.creation_timestamp)
        }
        for sa in result.items
    ]


def create_service_account(name: str, namespace: str = None):
    """
    Create a service account.

    :param name: Name of service account.
    :param namespace: namespace to create service account in.  If None, create service account in default namespace
    :return: `V1ServiceAccount <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ServiceAccount.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    body =\
        { 'apiVersion': 'v1',
          'kind': 'ServiceAccount',
          'metadata' : { 'name': name }
        }

    return v1_core.create_namespaced_service_account(namespace, body)

def get_service_account(name: str, namespace: str = None):
    """
    Get details of specified service account

    :param name: Name of service account to retrieve.
    :param namespace: Namespace to retrieve service account from. If None, retrieve from default namespace.
    :return: `V1ServiceAccount <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ServiceAccount.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()
    pass

    return v1_core.read_namespaced_service_account(name, namespace)


def service_account_exists(name: str, namespace: str = None):
    """
    Checks for existence of service account

    :param name: Name of service account to look for.
    :param namespace: Namespace to look in.  If None, look in default namespace.
    :return: True if specified account exists.
    """
    if namespace is None:
        namespace = get_default_namespace()

    try:
        result = get_service_account(name, namespace)
        return result.metadata.name == name

    except:
        return False


def delete_service_account(name: str, namespace: str = None):
    """
    Delete specified service account.

    :param name: Name of service account to delete.
    :param namespace: Namespace to delete from.  If None, delete from default namespace.
    :return: None if service account doesn't exists, otherwise returns `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if service_account_exists(name, namespace):
        return v1_core.delete_namespaced_service_account(name, namespace)
    else:
        return None
