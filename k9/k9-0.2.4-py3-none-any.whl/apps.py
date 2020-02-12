from kubernetes import client, config
from k9.core import *

v1_apps = client.AppsV1Api()

###########################################################################
# Deployments
###########################################################################

def list_deployments(namespace: str = None):
    """
    Lists deployments in a given namespace.

    :param namespace: Namespace you want to search.  If None, the default namespace is used.
    :return: A list of deployment names.
    """
    if namespace is None:
        namespace = get_default_namespace()

    return [
        {
            'name': deployment.metadata.name,
            'ready': f'{deployment.status.ready_replicas}/{deployment.status.replicas}',
            'available': deployment.status.available_replicas,
            'up-to-date': deployment.status.updated_replicas,
            'age': get_age(deployment.metadata.creation_timestamp)
        }
        for deployment in v1_apps.list_namespaced_deployment(namespace).items
    ]


def deployment_exists(name: str, namespace: str = None):
    """
    Returns True if the specified deployment exists.
    
    :param name: The name of the deployment
    :param namespace: The namespace to search in. If none, we use the default namespace.
    :return: True if the deployment exists in the specified namespace (or default if not provided).
    """
    try:
        if namespace is None:
            namespace = get_default_namespace()

        result = get_deployment(name, namespace)
        return result.metadata.name == name

    except:
        return False

def get_deployment(name: str, namespace: str = None):
    """
    Get a specific deployment by name.

    :param name: Name of deployment to retrieve.
    :param namespace:  Namespace to search.  If None, the default namespace is used.

    :return: `V1Deployment <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Deployment.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_apps.read_namespaced_deployment(name, namespace)


def create_deployment(body: dict, namespace: str = None):
    """
    Create a deployment from a definition file:

    :param body: Deployment Description - https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/AppsV1beta1Deployment.md
    :param namespace: Namespace to create Deployment in.  If None, the default namespace is used.
    :return: `V1Deployment <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Deployment.md>`_

    You'll most likely create a deployment configuration file and import that in as follows:

    Sample YAML file::

        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: tomcat-dev
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: tomcat
              env: dev
          strategy:
            type: RollingUpdate
            rollingUpdate:
              maxSurge: 1
              maxUnavailable: 1
          minReadySeconds: 5
          template:
            metadata:
              labels:
                app: tomcat
                env: dev
            spec:
              containers:
              - name: tomcat
                image: tomcat:7
                ports:
                  - containerPort: 8080
                env:
                  - name: DS_URL
                    valueFrom:
                      secretKeyRef:
                        name: tomcat-dev
                        key: ds-url
                  - name: DS_USR
                    valueFrom:
                      secretKeyRef:
                        name: tomcat-dev
                        key: username
                  - name: DS_PWD
                    valueFrom:
                      secretKeyRef:
                        name: tomcat-dev
                        key: password

    Example::

        import k9.helper as k9

        body = k9.read_yaml('tomcat-deploy-dev.yml')
        k9.create_deployment(body)


    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_apps.create_namespaced_deployment(namespace, body)

def delete_deployment(name: str, namespace: str = None):
    """
    Delete the specified deployment.

    :param name: Name of deployment to remove.
    :param namespace: Namespace to remove deployment from.   If None, the default namespace is used.
    :return: None if deployment did not exist, otherwise `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if deployment_exists(name, namespace):
        return v1_apps.delete_namespaced_deployment(name, namespace)
    else:
        return None


def update_deployment_image(name: str, container: str, image: str, namespace: str = None):
    """
    Updates the specified deployment name with a new image tag for the container.  The container name must
    match the container name specified in the original deployment.

    This will perform a rolling update if  max_unavailable replicas is less than the total number of replicas
    for the cluster.

    :param name: Name of the deployment to update
    :param container: Name of the container within the deployment to update.
    :param image: The image and tag of the image to update the container to.
    :param namespace: The namespace to find the deployment in.  If None, the default namespace is used.
    :return: `V1Deployment <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Deployment.md>`_

    The following example results in a rolling update to to Tomcat 8::

            update_deployment_image(deploy_name, 'tomcat', 'tomcat:8')

    Note that the container name matches the specification of the deployment YAML shown above
    and changes the version of Tomcat from version 7 to version 8.
    """
    if namespace is None:
        namespace = get_default_namespace()

    body = {
        'apiVersion': "apps/v1",
        'kind': "Deployment",
        'metadata': {
            'name': name
        },
        'spec': {
            'template': {
                'spec': {
                    'containers': [
                        {
                            'name': container,
                            'image': image
                        }
                    ]
                }
            }
        }
    }

    return v1_apps.patch_namespaced_deployment(name, namespace, body)

def scale_deployment(name: str, spec: str, namespace:str = None):
    """
    Updates the scaling specification for this deployment.

    :param name: Name of deployment to update.
    :param spec: The updated specification of the scaling parameters.
    :param namespace: The namespace to update the deployment in.  If namespace is None, the default namespace is used.
    :return: `V1Scale <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Scale.md>`_

    Other useful references: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#scaling-a-deployment

    Example to scale up the deployment to 3 replicas::

            spec = {
                'replicas': 3
            }
            scale_deployment(deploy_name, spec)

    """

    if namespace is None:
        namespace = get_default_namespace()
    body = {
        'apiVersion': "apps/v1",
        'kind': "Deployment",
        'metadata': {
            'name': "tomcat-dev"
        },
        'spec': spec
    }

    return v1_apps.patch_namespaced_deployment_scale(name, namespace, body)
