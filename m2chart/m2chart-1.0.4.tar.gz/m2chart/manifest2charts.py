# -*- coding: utf-8 -*-

from copy import deepcopy
from collections import defaultdict


def is_subset_dict(a, b):
    ''' a is b subset '''
    if not a:
        return False
    if not b:
        return False
    return all(b.get(k) == v for k, v in a.items())


class Manifest2Charts:

    def __init__(self, manifests, components):
        self.manifests = manifests
        self.components = components
        self.services = {}
        self.services_sel = {}

        self.svc_dict = {}
        self.svc_dict_sel = {}

        self.config_maps = {}
        self.secrets = {}

        self.pvcs = {}

        self.used_config_maps = defaultdict(list)
        self.used_secrets = defaultdict(list)
        self.used_pvcs = defaultdict(list)

        self.global_section = {}

    def _set_global_env(self, envs):
        if not envs:
            return None
        for env in envs:
            if env.name == 'PRO_NAME':
                self.global_section['projectname'] = env.value
            if env.name == 'PRO_ENV':
                self.global_section['git_branch'] = env.value

    def _get_configmap_files(self):
        cms = []
        ret = []
        raw_ret = []
        for svc_name, cm_names in self.used_config_maps.items():
            cms += cm_names
        cms = list(set(cms))
        for cm in cms:
            cm_data = self.config_maps.get(cm)
            if not cm_data:
                continue
            cm_item = {'name': cm, 'files': []}
            raw_cm_item = {'name': cm, 'files': []}
            for key, value in cm_data.items():
                cm_item['files'].append({'name': key})
                raw_cm_item['files'].append({'name': key, 'value': value})
            ret.append(cm_item)
            raw_ret.append(raw_cm_item)
        return ret, raw_ret

    def _get_secrets_files(self):
        secrets = []
        ret = []
        raw_ret = []
        for svc_name, sec_names in self.used_config_maps.items():
            secrets += sec_names
        sec_names = list(set(secrets))
        for sec in sec_names:
            sec_data = self.secrets.get(sec)
            if not sec_data:
                continue
            sec_item = {'name': sec, 'files': []}
            raw_sec_item = {'name': sec, 'files': []}
            for key, value in sec_data.items():
                sec_item['files'].append({'name': key})
                raw_sec_item['files'].append({'name': key, 'value': value})
            ret.append(sec_item)
            raw_ret.append(raw_sec_item)
        return ret, raw_ret

    def _get_requirements(self):
        ret = {'dependencies': []}
        for service, v in self.services.items():
            ret['dependencies'].append({
                'name': service,
                'version': 'v0'
            })
        return ret

    def _convert_values(self):
        values = deepcopy(self.services)
        values['global'] = self.global_section

        global_config_maps, raw_configmaps = self._get_configmap_files()
        global_secrets, raw_secrets = self._get_secrets_files()

        values['global']['configmap'] = global_config_maps
        values['global']['secret'] = global_secrets
        requirements = self._get_requirements()
        return {
            'values': values,
            'configmaps': raw_configmaps,
            'secrets': raw_secrets,
            'requirements': requirements
        }

    def convert(self):
        self.get_services()
        self.get_pvcs()
        self.get_config_maps()
        self.get_secrets()

        self.get_deployments()
        self.get_stateful_sets()
        self.get_daemon_sets()

        return self._convert_values()

    def convert_pod(self, obj):
        pod_spec = obj.spec.template.spec
        container = pod_spec.containers[0]
        ret = {
            'name': container.name
        }
        if ':' in container.image:
            repository, tag = container.image.split(':')
        else:
            repository, tag = container.image, 'leatest'
        ret['image'] = {
            'repository': repository,
            'tag': tag,
            'pullPolicy': container.image_pull_policy
        }

        if container.env:
            ret['env'] = [e.to_dict() for e in container.env]

        if container.resources:
            ret['resources'] = container.resources.to_dict()

        if container.volume_mounts:
            ret['volumeMounts'] = [
                vm.to_dict() for vm in container.volume_mounts]
        if container.liveness_probe:
            ret['liveness_probe'] = container.liveness_probe.to_dict()
        if container.readiness_probe:
            ret['readiness_probe'] = container.readiness_probe.to_dict()

        return ret

    def relate_svc(self, labels):
        for svc, svc_labels in self.svc_dict_sel.items():
            if is_subset_dict(svc_labels, labels):
                return self.svc_dict[svc]
        return None

    def relate_pvc(self, name):
        pvcs = self.used_pvcs.get(name)
        if not pvcs:
            return None
        ret = []
        for pvc in pvcs:
            pvc_content = self.pvcs.get(pvc)
            if pvc_content:
                ret.append(pvc_content)
        return ret

    def convert_volumes(self, service_name, volumes):
        ret = []
        for volume in volumes:
            if volume.config_map:
                self.used_config_maps[service_name].append(
                    volume.config_map.name)
            if volume.secret:
                self.used_secrets[service_name].append(
                    volume.config_map.name)
            if volume.persistent_volume_claim:
                self.used_pvcs[service_name].append(
                    volume.persistent_volume_claim.claim_name)
            ret.append(volume.to_dict())
        return ret

    def convert_image_pull_secrt(self, svc_name, secrets):
        ret = []
        for s in secrets:
            self.used_secrets[svc_name].append(s.name)
            ret.append(s.to_dict())
        return ret

    def get_deployments(self):
        deployments = self.manifests.get('deployments')
        if not deployments:
            return False
        for deployment in deployments.items:
            deployment_name = deployment.metadata.name
            if self.components and len(self.components) > 0:
                if deployment_name not in self.components:
                    continue
            values_content = self.convert_pod(deployment)
            spec = deployment.spec
            if spec.replicas:
                values_content['replicaCount'] = spec.replicas
            svc = self.relate_svc(spec.selector.match_labels)
            if svc:
                values_content['service'] = svc
            values_content['workloadType'] = 'deployment'
            if spec.template.spec.volumes:
                values_content['volumes'] = self.convert_volumes(
                    deployment_name,
                    spec.template.spec.volumes
                )
            pvcs = self.relate_pvc(deployment_name)
            if pvcs:
                values_content['persistence'] = pvcs
            if spec.template.spec.image_pull_secrets:
                values_content['image_pull_secrets'] = \
                    self.convert_image_pull_secrt(
                        deployment_name,
                        spec.template.spec.image_pull_secrets
                    )
            if spec.template.spec.init_containers:
                values_content['using_cmp_agent'] = True
                init_container = spec.template.spec.init_containers[0]
                if ':' not in init_container.image:
                    init_image = init_container.image
                    tag = 'latest'
                else:
                    init_image, tag = init_container.image.split(':')
                self.global_section['init'] = {
                    'image': {
                        'repository': init_image,
                        'tag': tag,
                        'pullPolicy': init_container.image_pull_policy
                    }
                }
                self._set_global_env(init_container.env)
            self.services[deployment_name] = values_content

    def get_stateful_sets(self):
        stateful_sets = self.manifests.get('stateful_sets')
        if not stateful_sets:
            return False
        for sts in stateful_sets.items:
            sts_name = sts.metadata.name
            if self.components and len(self.components) > 0:
                if sts_name not in self.components:
                    continue
            spec = sts.spec
            values_content = self.convert_pod(sts)
            values_content['workloadType'] = 'stateful_set'
            if spec.replicas:
                values_content['replicaCount'] = spec.replicas
            svc = self.relate_svc(spec.selector.match_labels)
            if svc:
                values_content['service'] = svc
            if spec.template.spec.volumes:
                values_content['volumes'] = self.convert_volumes(
                    sts_name,
                    spec.template.spec.volumes
                )
            pvcs = self.relate_pvc(sts_name)
            if pvcs:
                values_content['persistence'] = pvcs
            if spec.template.spec.image_pull_secrets:
                values_content['image_pull_secrets'] = \
                    self.convert_image_pull_secrt(
                        sts_name,
                        spec.template.spec.image_pull_secrets
                    )
            if spec.template.spec.init_containers:
                values_content['using_cmp_agent'] = True
                init_container = spec.template.spec.init_containers[0]
                if ':' not in init_container.image:
                    init_image = init_container.image
                    tag = 'latest'
                else:
                    init_image, tag = init_container.image.split(':')
                self.global_section['init'] = {
                    'image': {
                        'repository': init_image,
                        'tag': tag,
                        'pullPolicy': init_container.image_pull_policy
                    }
                }
                self._set_global_env(init_container.env)
            self.services[sts_name] = values_content
            self.services_sel[sts_name] = spec.selector.match_labels

    def get_daemon_sets(self):
        daemon_sets = self.manifests.get('daemon_sets')
        if not daemon_sets:
            return False
        for ds in daemon_sets.items:
            ds_name = ds.metadata.name
            if self.components and len(self.components) > 0:
                if ds_name not in self.components:
                    continue
            spec = ds.spec
            values_content = self.convert_pod(ds)
            values_content['workloadType'] = 'daemon_set'
            svc = self.relate_svc(spec.selector.match_labels)
            if svc:
                values_content['service'] = svc
            if spec.template.spec.volumes:
                values_content['volumes'] = self.convert_volumes(
                    ds_name,
                    spec.template.spec.volumes
                )
            pvcs = self.relate_pvc(ds_name)
            if pvcs:
                values_content['persistence'] = pvcs
            if spec.template.spec.image_pull_secrets:
                values_content['image_pull_secrets'] = \
                    self.convert_image_pull_secrt(
                        ds_name,
                        spec.template.spec.image_pull_secrets
                    )
            if spec.template.spec.init_containers:
                values_content['using_cmp_agent'] = True
                init_container = spec.template.spec.init_containers[0]
                if ':' not in init_container.image:
                    init_image = init_container.image
                    tag = 'latest'
                else:
                    init_image, tag = init_container.image.split(':')
                self.global_section['init'] = {
                    'image': {
                        'repository': init_image,
                        'tag': tag,
                        'pullPolicy': init_container.image_pull_policy
                    }
                }
                self._set_global_env(init_container.env)
            self.services[ds_name] = values_content
            self.services_sel[ds_name] = spec.selector.match_labels

    def get_secrets(self):
        secrets = self.manifests.get('secrets')
        if not secrets:
            return False
        for secret in secrets.items:
            secret_name = secret.metadata.name
            self.secrets[secret_name] = secret.data

    def get_config_maps(self):
        config_maps = self.manifests.get('config_maps')
        if not config_maps:
            return False
        for cm in config_maps.items:
            self.config_maps[cm.metadata.name] = cm.data

    def get_pvcs(self):
        pvcs = self.manifests.get('pvcs')
        if not pvcs:
            return False
        for pvc in pvcs.items:
            pvc_name = pvc.metadata.name
            self.pvcs[pvc_name] = {
                'name': pvc_name,
                'accessMode': pvc.spec.access_modes[0],
                'size': pvc.spec.resources.requests['storage'],
                'storageClass': pvc.spec.storage_class_name
            }

    def _valid_ports(self, ports):
        ret = []
        for port in ports:
            port = port.to_dict()
            if port['node_port'] is not None:
                del(port['node_port'])
            if port['name'] is None:
                port['name'] = '%s-%s' % (
                    port['protocol'].lower(), port['port'])
            ret.append(port)
        return ret

    def get_services(self):
        services = self.manifests.get('services')
        if not services:
            return False
        for svc in services.items:
            self.svc_dict[svc.metadata.name] = {
                'type': svc.spec.type,
                'ports': self._valid_ports(svc.spec.ports)
            }
            self.svc_dict_sel[svc.metadata.name] = svc.spec.selector
