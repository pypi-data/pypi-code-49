from kubernetes import client, config
from k9.pretty_object import PrettyObject
from k9.core import get_default_namespace
# po = PrettyObject()
# config.load_kube_config()
#
v1_rbac = client.RbacAuthorizationV1Api()



###########################################################################
# Roles
###########################################################################

def list_roles(namespace: str = None):
    """
    List all cluster roles
    :param namespace: Then namespace to list roles from.  If None, uses the default namespace.
    :return: A list of dictionary items with **name** and **created**.
    """
    if namespace is None:
        namespace = get_default_namespace()

    return [
        {
            'name': role.metadata.name,
            'created': role.metadata.creation_timestamp
        }
        for role in v1_rbac.list_namespaced_role(namespace).items
    ]


def create_role(body: dict, namespace: str = None):
    """
    Create a role from an object defining the role.

    :param body: The role definition object.
    :param namespace: Then namespace to create role in.  If None, uses the default namespace.
    :return: `V1Role <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Role.md>`_

    Example YAML file::

        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          name: ecr-login-role
        rules:
        - apiGroups: [""]
          resources: ["secrets"]
          verbs: ["create", "delete"]
        - apiGroups: [""]
          resources: ["serviceaccounts"]
          verbs: ["get", "patch"]


    Example Call::

        from k9.helper import (
            set_default_namespace,
            create_role,
            read_yaml
        )

        set_default_namespace('my-namespace')

        body = read_yaml('ecr-login-role.yml')
        result = create_role(body)

    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_rbac.create_namespaced_role(namespace, body)


def delete_role(name: str, namespace: str = None):
    """
    Deletes the specified cluster

    :param name: Name of cluster
    :param namespace: Then namespace to delete role from.  If None, uses the default namespace.
    :return: None if role exists, otherwise return `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if role_exists(name, namespace):
        return v1_rbac.delete_namespaced_role(name, namespace)
    else:
        return None


def get_role(name: str, namespace: str = None):
    """
    Gets the specified cluster role.

    :param name: Name of cluster role to retrieve.
    :param namespace: Then namespace to get role from.  If None, uses the default namespace.
    :return: `V1Role <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Role.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_rbac.read_namespaced_role(name, namespace)


def role_exists(name:str, namespace: str = None):
    """
    Checks for the cluster role's existence.

    :param name: Name of cluster role to look for.
    :param namespace: Then namespace to check for role.  If None, uses the default namespace.
    :return: True if specified cluster role exists.
    """
    try:
        if namespace is None:
            namespace = get_default_namespace()

        result = get_role(name, namespace)
        return result.metadata.name == name

    except:
        return False


def create_role_binding(name: str, role: str, sa: str, namespace: str = None):
    """
    Bind the specified role to the specified service account.

    :param name: Name of binding we are creating here
    :param role: The cluster role name to bind with.
    :param sa: The service account to bind this role to.
    :param namespace: The namespace of role and service account.  If namespace is None, then the binding will be performed in the default namespace.
    :return: `V1RoleBinding <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1RoleBinding.md>`_

    Example::

        result = create_role_binding(binding_name, role_name, sa_name)

    """
    if namespace is None:
        namespace = get_default_namespace()

    body =\
        {
            'apiVersion': 'rbac.authorization.k8s.io/v1',
            'kind': 'RoleBinding',
            'metadata': {
                'name': name,
                'namespace': namespace
            },
            'roleRef': {
                'apiGroup': 'rbac.authorization.k8s.io',
                'kind': 'Role',
                'name': role
            },
            'subjects': [{
                'kind': 'ServiceAccount',
                'name': sa,
                'namespace': namespace
            }]
        }
    return v1_rbac.create_namespaced_role_binding(namespace, body)


def get_role_binding(name: str, namespace: str = None):
    """
    Get cluster role binding information

    :param name: Name of cluster role binding
    :param namespace: Then namespace to get role binding from.  If None, uses the default namespace.
    :return: `V1RoleBinding <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1RoleBinding.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    return v1_rbac.read_namespaced_role_binding(name, namespace)


def role_binding_exists(name:str, namespace: str = None):
    """
    Checks for the existence of the cluster role binding.

    :param name: name of cluster role binding.
    :param namespace: Then namespace to check for role binding.  If None, uses the default namespace.
    :return: True if binding exists.
    """
    try:
        if namespace is None:
            namespace = get_default_namespace()

        result = get_role_binding(name, namespace)
        return result.metadata.name == name

    except:
        return False


def delete_role_binding(name: str, namespace: str = None):
    """
    Delete cluster role binding

    :param name: cluster role binding name
    :param namespace: Then namespace to delete role binding from.  If None, uses the default namespace.
    :return: `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if namespace is None:
        namespace = get_default_namespace()

    if role_binding_exists(name, namespace):
        return v1_rbac.delete_namespaced_role_binding(name, namespace)
    else:
        return None


###########################################################################
# Cluster Roles
###########################################################################

def list_cluster_roles():
    """
    List all cluster roles
    :return: A list of dictionary items with **name** and **created**.
    """
    return [
        {
            'name': role.metadata.name,
            'created': role.metadata.creation_timestamp
        }
        for role in v1_rbac.list_cluster_role().items
    ]


def create_cluster_role(body: dict):
    """
    Create a cluster role from an object defining the role.

    Example::

            role = {
                'apiVersion': 'rbac.authorization.k8s.io/v1',
                'kind': 'ClusterRole',
                'metadata': {'name': f'{role_name}'},
                'rules': [
                     {
                         'apiGroups': [''],
                         'resources': ['secrets'],
                         'verbs': ['create', 'delete']
                     },
                     {
                         'apiGroups': [''],
                         'resources': ['serviceaccounts'],
                         'verbs': ['get', 'patch']
                     }

                 ]
            }

            result = create_cluster_role(role)

    Result::

        {'aggregation_rule': None,
         'api_version': 'rbac.authorization.k8s.io/v1',
         'kind': 'ClusterRole',
         'metadata': {'annotations': None,
                      'cluster_name': None,
                      'creation_timestamp': datetime.datetime(2019, 10, 16, 17, 33, 28, tzinfo=tzutc()),
                      'deletion_grace_period_seconds': None,
                      'deletion_timestamp': None,
                      'finalizers': None,
                      'generate_name': None,
                      'generation': None,
                      'initializers': None,
                      'labels': None,
                      'managed_fields': None,
                      'name': 'ecr-login-role',
                      'namespace': None,
                      'owner_references': None,
                      'resource_version': '1901293',
                      'self_link': '/apis/rbac.authorization.k8s.io/v1/clusterroles/ecr-login-role',
                      'uid': '10ccdf2b-f03b-11e9-9956-025000000001'},
         'rules': [{'api_groups': [''],
                    'non_resource_ur_ls': None,
                    'resource_names': None,
                    'resources': ['secrets'],
                    'verbs': ['create', 'delete']}]}"

    :param body: The role definition object.
    :return: `V1ClusterRole <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ClusterRole.md>`_
    """
    return v1_rbac.create_cluster_role(body)


def delete_cluster_role(name: str):
    """
    Deletes the specified cluster

    :param name: Name of cluster
    :return: None if cluster role doesn't exist, otherwise returns `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_
    """
    if cluster_role_exists(name):
        return v1_rbac.delete_cluster_role(name)
    else:
        return None


def get_cluster_role(name: str):
    """
    Gets the specified cluster role.

    :param name: Name of cluster role to retrieve.
    :return: `V1ClusterRole <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ClusterRole.md>`_
    """
    return v1_rbac.read_cluster_role(name)


def cluster_role_exists(name:str):
    """
    Checks for the cluster role's existence.

    :param name: Name of cluster role to look for.
    :return: True if specified cluster role exists.
    """
    try:
        result = get_cluster_role(name)
        return result.metadata.name == name

    except:
        return False


def create_cluster_role_binding(name: str, role: str, sa: str, namespace: str = None):
    """
    Bind the specified role to the specified service account.

    :param name: Name of binding we are creating here.
    :param role: The cluster role name to bind with.
    :param sa: The service account to bind this role to.
    :param namespace: The namespace of the **service account**.  If namespace is None, then the binding will be performed on service account in the default namespace.
    :return: `V1ClusterRoleBinding <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ClusterRoleBinding.md>`_

    Example::

        result = create_cluster_role_binding(cr_bind_name, cr_name, sa_name)

    """
    if namespace is None:
        namespace = get_default_namespace()

    body =\
        {
            'apiVersion': 'rbac.authorization.k8s.io/v1',
            'kind': 'ClusterRoleBinding',
            'metadata': {'name': name},
            'roleRef': {
                'apiGroup': 'rbac.authorization.k8s.io',
                'kind': 'ClusterRole',
                'name': role
            },
            'subjects': [{
                'kind': 'ServiceAccount',
                'name': sa,
                'namespace': namespace
            }]
        }
    return v1_rbac.create_cluster_role_binding(body)


def get_cluster_role_binding(name: str):
    """
    Get cluster role binding information

    :param name: Name of cluster role binding
    :return: `V1ClusterRoleBinding <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ClusterRoleBinding.md>`_
    """
    return v1_rbac.read_cluster_role_binding(name)


def cluster_role_binding_exists(name:str):
    """
    Checks for the existence of the cluster role binding.

    :param name: name of cluster role binding.
    :return: True if binding exists.
    """
    try:
        result = get_cluster_role_binding(name)
        return result.metadata.name == name

    except:
        return False


def delete_cluster_role_binding(name: str):
    """
    Delete cluster role binding

    :param name: cluster role binding name
    :return: None if cluster role binding doesn't exist, otherwise returns `V1Status <https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Status.md>`_

    """
    if cluster_role_binding_exists(name):
        return v1_rbac.delete_cluster_role_binding(name)
    else:
        return None


