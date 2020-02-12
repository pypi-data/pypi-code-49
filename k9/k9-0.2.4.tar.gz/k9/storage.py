import json

from k9.core import run_command


def create_storage_class(fn: str):
    """
    :param fn: Filename of storage class description
    :return: `subprocess.CompletedProcess <https://docs.python.org/3/library/subprocess.html>`_

    Example::

        from k9.storage import create_storage_class
        result = create_storage_class('storage.yaml')

    Sample YAML file::

        kind: StorageClass
        apiVersion: storage.k8s.io/v1
        metadata:
          name: aws-storage-clas
        provisioner: kubernetes.io/aws-ebs
        parameters:
          type: gp2
          fsType: ext4
        volumeBindingMode: Immediate
        reclaimPolicy: Retain
        allowVolumeExpansion: true

    """

    return run_command('kubectl', 'create', '-f', fn)


def delete_storage_class(name: str):
    """
    Deletes the specfied storage class.

    :param name: Name of storage class
    :return: `subprocess.CompletedProcess <https://docs.python.org/3/library/subprocess.html>`_
    """
    return run_command('kubectl', 'delete', 'storageclass', name)


def list_storage_classes():
    """
    List all storage class

    :return: Returns a list of storage classes.

    Example Output::

        {
            "apiVersion": "v1",
            "items": [
                {
                    "allowVolumeExpansion": true,
                    "apiVersion": "storage.k8s.io/v1",
                    "kind": "StorageClass",
                    "metadata": {
                        "creationTimestamp": "2019-12-20T14:18:10Z",
                        "name": "aws-storage-class",
                        "resourceVersion": "3708823",
                        "selfLink": "/apis/storage.k8s.io/v1/storageclasses/aws-storage-class",
                        "uid": "8d3a7012-2333-11ea-b829-025000000001"
                    },
                    "parameters": {
                        "fsType": "ext4",
                        "type": "gp2"
                    },
                    "provisioner": "kubernetes.io/aws-ebs",
                    "reclaimPolicy": "Retain",
                    "volumeBindingMode": "Immediate"
                },
                {
                    "apiVersion": "storage.k8s.io/v1",
                    "kind": "StorageClass",
                    "metadata": {
                        "annotations": {
                            "storageclass.kubernetes.io/is-default-class": "true"
                        },
                        "creationTimestamp": "2019-10-01T23:34:49Z",
                        "name": "hostpath",
                        "resourceVersion": "527",
                        "selfLink": "/apis/storage.k8s.io/v1/storageclasses/hostpath",
                        "uid": "0f5bccbc-e4a4-11e9-90c3-025000000001"
                    },
                    "provisioner": "docker.io/hostpath",
                    "reclaimPolicy": "Delete",
                    "volumeBindingMode": "Immediate"
                }
            ],
            "kind": "List",
            "metadata": {
                "resourceVersion": "",
                "selfLink": ""
            }
        }
    """

    result = run_command('kubectl', 'get', 'storageclass', '-o', 'json')
    list = json.loads(result.stdout)
    return [
        {
            'name': c['metadata']['name'],
            'allow_volume_expansion': c.get('allowVolumeExpansion'),
            'api_version': c['apiVersion'],
            'provisioner': c['provisioner'],
            'reclaim_policy': c['reclaimPolicy'],
            'volume_binding_mode': c['volumeBindingMode']
        }
        for c in list['items']
    ]


def storage_class_exists(name: str):
    """
    :param name: Storage class name
    :return: True if specified storage class exists.
    """

    list = list_storage_classes()
    found = [
        c['name']
        for c in list
        if c['name'] == name
    ]

    return len(found) > 0

