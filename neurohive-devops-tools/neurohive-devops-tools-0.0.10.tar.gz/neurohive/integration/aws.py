import json
import os
import time
import logging
import tempfile
from pathlib import Path

import boto3

logging.basicConfig(level=logging.INFO)

class LegacyServerCleanerException(Exception):
    pass


class LegacyServiceCleaner:
    def __init__(self):
        pass

    def cleanup_rule(self, rule_arn, target_group_arn):
        rule = self._describe_rule(rule_arn)
        remove_rule = None
        for action in rule["Actions"]:
            if action.get("Type") == "forward":
                targets_list_size = len(action["ForwardConfig"]["TargetGroups"])
                if targets_list_size == 1 and action["ForwardConfig"]["TargetGroups"][0]['TargetGroupArn'] == target_group_arn:
                    remove_rule = True
        if remove_rule:
            logging.info(f'remove rule: {rule_arn}')
            client = boto3.client('elbv2')
            response = client.delete_rule(
                RuleArn=rule_arn
            )
            self._check_response(response)

    def remove_target_group_from_rule(self, rule_arn, target_group_arn):
        rule = self._describe_rule(rule_arn)
        for action in rule['Actions']:
            if action['Type'] == "forward":
                for idx, tg in enumerate(action["ForwardConfig"]["TargetGroups"]):
                    if tg["TargetGroupArn"] == target_group_arn:
                        logging.info(f'Delete tg {target_group_arn} from rule {rule_arn}')
                        del action["ForwardConfig"]["TargetGroups"][idx]
                # special case last rule
                if len(action['ForwardConfig']['TargetGroups']) == 0:
                    return
        for condition in rule["Conditions"]:
            if "Values" in condition:
                del condition["Values"]
        del rule["Priority"]
        del rule["IsDefault"]
        client = boto3.client('elbv2')
        response = client.modify_rule(**rule)
        self._check_response(response)

    def remove_target_group(self, target_group_arn):
        client = boto3.client('elbv2')
        response = client.delete_target_group(
            TargetGroupArn=target_group_arn
        )
        self._check_response(response)

    def remove_sd_service(self, sd_id):
        logging.info(f"delete: {sd_id}")
        instances = self._list_sd_instances(sd_id)
        logging.info(f"remove instances: {instances}")
        for instance in instances:
            self._deregister_sd_instance(sd_id, instance['Id'])
        time.sleep(5)
        client = boto3.client('servicediscovery')
        response = client.delete_service(
            Id=sd_id
        )
        self._check_response(response)

    def remove_ecs_service(self, cluster, service):
        client = boto3.client('ecs')
        response = client.delete_service(
            cluster=cluster,
            service=service,
            force=True
        )
        self._check_response(response)

    def cleanup_deploys(self):
        bucket = 'mib-env.data.private'
        items = self._list_objects_s3_bucket(bucket)
        tmpdir = self._download_from_s3bucket(bucket, items)
        tmpdir='/var/folders/dq/z_z5nfs5099821s46qs7hkyc0000gp/T/tmpqi5al2mm'
        oldiest = self._get_oldiest(tmpdir)

        for deploy in oldiest:
            logging.info(f"delete: {deploy['filename']}")
            breakpoint()
            self._del_old_deploy(deploy)
            self.remove_deploy_data(bucket, deploy)

    def remove_deploy_data(self, bucket, item):
        var_name = item['filename'].split('/')[-1]
        data_name = f"{var_name.split('.')[0]}.state"
        logging.info(f"delete: {var_name}")
        print(var_name, data_name)
        client = boto3.client('s3')
        for name in [var_name, data_name]:
            response = client.delete_object(
                Bucket=bucket,
                Key=f'ecs/ustate/{name}'
            )

    def _del_old_deploy(self, item):
        td_data_dir = Path(item['filename']).parent
        tf_data_fn = item['filename'].split('/')[-1].split('.')[0]
        tf_data_fn = f'{tf_data_fn}.state'
        td_data_dir = td_data_dir.joinpath(tf_data_fn)
        item['state_data'] = json.loads(td_data_dir.read_text())['outputs']


        rule_arn = item['data']['rule_arn']
        target_group_arn = item['data']['target_group_arn']
        sd_id = item['state_data']['aws_service_discovery_service']['value']
        service_name = item['state_data']['aws_ecs_service']['value']
        self.remove_target_group_from_rule(rule_arn, target_group_arn)
        self.cleanup_rule(rule_arn, target_group_arn)
        self.remove_target_group(target_group_arn)
        self.remove_sd_service(sd_id)
        self.remove_ecs_service('mib', service_name)
        self.remove_deploy_data('mib-env.data.private', item)

    def _get_oldiest(self, dirname):
        root_path = Path(dirname)
        items = []
        for path in root_path.glob('*-ustate.auto.tfvars.json'):
            items.append({
                "filename": str(path),
                "data": json.loads(path.read_text())
            })
        logging.info(f"all vers: {[item['data']['lib_version'] for item in items]}")
        items_vers = {}
        for item in items:
            version = item['data']['lib_version']
            if not version in items_vers:
                items_vers[version] = list()
            items_vers[version].append(item)
        keep_part = sorted(items_vers.keys(), reverse=True)[:5]
        logging.info(f"keep part: {keep_part}")
        delete_items = []
        for item in items:
            if item['data']['lib_version'] not in keep_part:
                delete_items.append(item)
        logging.info(f"delete: {[item['data']['lib_version'] for item in delete_items]}")
        return delete_items

    def _deregister_sd_instance(self, sd_id, instance_id):
        client = boto3.client('servicediscovery')
        response = client.deregister_instance(
            ServiceId=sd_id,
            InstanceId=instance_id
        )
        self._check_response(response)

    def _list_sd_instances(self, sd_id):
        client = boto3.client('servicediscovery')
        response = client.list_instances(
            ServiceId=sd_id
        )
        self._check_response(response)
        return response["Instances"]

    def _describe_rule(self, rule_arn):
        client = boto3.client('elbv2')
        response = client.describe_rules(
            RuleArns=[
                rule_arn
            ]
        )
        self._check_response(response)
        return response['Rules'][0]

    def _check_response(self, response):
        if isinstance(response, dict):
            if response.get('ResponseMetadata').get('HTTPStatusCode') != 200:
                raise LegacyServerCleanerException("Failed response", response)

    def _list_objects_s3_bucket(self, bucket):
        client = client = boto3.client('s3')
        response = client.list_objects_v2(
            Bucket=bucket,
            Prefix='ecs/ustate',
        )
        self._check_response(response)
        items = [item['Key'] for item in response['Contents']]
        return items

    def _download_from_s3bucket(self, bucket, items):
        tmpdir = tempfile.mkdtemp()
        s3 = boto3.resource('s3')
        for item in items:
            dest_path = item.split('/')[-1]
            logging.info(f'Downloading: {item} to {tmpdir}/{dest_path}')
            s3.meta.client.download_file(
                bucket,
                item,
                f'{tmpdir}/{dest_path}'
            )
        return tmpdir


if __name__ == '__main__':
    lc = LegacyServiceCleaner()
    lc.cleanup_deploys()
