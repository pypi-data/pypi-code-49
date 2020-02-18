# -*- coding: utf-8 -*-

from kubernetes import client, config


def get_cluster_client(config_file, context=None):
    kwargs = {'config_file': config_file}
    if context:
        kwargs['context'] = context

    api_client = config.new_client_from_config(
        **kwargs
    )
    return api_client


def load_online_manifest(config_file, context, namespace):
    api_client = get_cluster_client(config_file, context=context)
    client_args = {
        'api_client': api_client
    }
    core_v1_api = client.CoreV1Api(**client_args)
    ext_v1_beta1_api = client.ExtensionsV1beta1Api(**client_args)
    apps_v1_api = client.AppsV1Api(**client_args)

    pods = core_v1_api.list_namespaced_pod(namespace)
    services = core_v1_api.list_namespaced_service(namespace)
    secrets = core_v1_api.list_namespaced_secret(namespace)
    config_maps = core_v1_api.list_namespaced_config_map(namespace)
    pvcs = core_v1_api.list_namespaced_persistent_volume_claim(namespace)

    deployments = ext_v1_beta1_api.list_namespaced_deployment(namespace)
    daemon_sets = ext_v1_beta1_api.list_namespaced_daemon_set(namespace)

    stateful_sets = apps_v1_api.list_namespaced_stateful_set(namespace)

    return {
        'pods': pods,
        'pvcs': pvcs,
        'secrets': secrets,
        'services': services,
        'deployments': deployments,
        'daemon_sets': daemon_sets,
        'config_maps': config_maps,
        'stateful_sets': stateful_sets,
    }
