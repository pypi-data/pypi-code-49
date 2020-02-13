# -*- coding: utf-8 -*-

import sys
import os
import base64
import yaml
import argparse
import shutil
from .k8s import load_online_manifest
from .manifest2charts import Manifest2Charts


M2CHART_BASE_DIR = os.path.dirname(__file__)


def write_file(items, chart_dir, item_type='configmap'):
    if item_type == 'configmap':
        item_dir = os.path.join(chart_dir, "configmap")
    else:
        item_dir = os.path.join(chart_dir, "secret")
    os.mkdir(item_dir)
    for item in items:
        inner_item_dir = os.path.join(item_dir, item['name'])
        if not os.path.exists(inner_item_dir):
            os.mkdir(inner_item_dir)
        for file in item['files']:
            file_n = os.path.join(inner_item_dir, file['name'])
            if item_type == 'configmap':
                value = file['value']
            else:
                value = base64.b64decode(file['value']).decode()
            with open(file_n, 'w') as f:
                f.write(value)


def write_configmaps(configmaps, chart_dir):
    write_file(configmaps, chart_dir)


def write_secrets(configmaps, chart_dir):
    write_file(configmaps, chart_dir, item_type='secret')


def write_requirements(requirements, chart_dir):
    requirements_file = os.path.join(chart_dir, 'requirements.yaml')
    for item in requirements['dependencies']:
        child_chart = os.path.join(chart_dir, 'charts', item['name'])
        svc_templates = os.path.join(
            M2CHART_BASE_DIR,
            'templates/svc_templates'
        )
        shutil.copytree(svc_templates, child_chart)
        chart_yaml = os.path.join(child_chart, 'Chart.yaml')
        with open(chart_yaml, 'w') as f:
            f.write(yaml.safe_dump({
                'name': item['name'],
                'description': item['name'],
                'version': item['version']
            }))
    req_content = yaml.safe_dump(requirements)
    with open(requirements_file, 'w') as f:
        f.write(req_content)


def exec(args):
    cluster_name = os.path.basename(args.kubeconfig)
    chart_name = cluster_name + '__' + args.namespace

    if not os.path.exists("charts"):
        os.mkdir("charts")
    chart_dir = os.path.join("charts", chart_name)
    if os.path.exists(chart_dir):
        shutil.rmtree(chart_dir)
    app_templates = os.path.join(
        M2CHART_BASE_DIR,
        'templates/app_templates'
    )
    shutil.copytree(app_templates, chart_dir)

    manifests = load_online_manifest(
        args.kubeconfig,
        args.context,
        args.namespace
    )
    m2c = Manifest2Charts(manifests)

    ret = m2c.convert()

    filepath = os.path.join(chart_dir, "values.yaml")
    with open(filepath, 'w') as f:
        f.write(ret['values'])

    chart_yaml = os.path.join(chart_dir, 'Chart.yaml')
    with open(chart_yaml, 'w') as f:
        f.write(yaml.safe_dump({
            'name': chart_name,
            'description': chart_name,
            'version': 'v0'
        }))

    write_configmaps(ret['configmaps'], chart_dir)
    write_secrets(ret['secrets'], chart_dir)
    write_requirements(ret['requirements'], chart_dir)
    print("done ~~ chart saved in dir %s" % chart_dir)


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-k', '--kubeconfig', type=str,
        required=True, help="kubeconfig file path")
    parser.add_argument(
        '-c', '--context', type=str, default='',
        required=False, help="context name")
    parser.add_argument(
        '-n', '--namespace', type=str,
        required=False, help="namespace name")
    args = parser.parse_args()
    exec(args)


if __name__ == "__main__":
    main()
