#!/usr/bin/env python

import requests
from plasmacli.project_manager import get_config
import os
from xxhash import xxh32_hexdigest

host = 'http://localhost:8196'

def daemon_ping():
    try:
        response = requests.get(host+'/api/ping')
        if response.status_code == 200:
            output = True
    except Exception as e:
        print('> Unable to connect to plasma daemon')
        return False
    

def run_workflow(workflow_name):
    config = get_config()
    daemon_available = daemon_ping()
    if daemon_available:
        workflow_id = xxh32_hexdigest(workflow_name)
        json = {}
        json['project-config'] = config
        json['workflow-name'] = workflow_name
        json['workflow-id'] = workflow_id
        json['host'] = 'local'
        json['action'] = 'start'
        response = requests.post(host+'/api/workflow/'+workflow_id+'/run')
        if response.status_code == 201:
            print('> Executing workflow')
        else:
            print('> Unable to execute_workflow')
    else:
        return False


def stop_workflow(workflow_id):
    daemon_available = daemon_ping()
    if daemon_available:
        json = {}
        json['host'] = 'local'
        json['action'] = 'stop'
        response = requests.post(host+'/api/workflow/'+workflow_id+'/run')
        if response.status_code == 200:
            print('> Stopping workflow')
        else:
            print('> Unable to execute_workflow')
    else:
        return False



def schedule_workflow(workflow_id,cron_rule):
    daemon_available = daemon_ping()
    if daemon_available:
        json = {}
        json['cron-rule'] = cron_rule
        response = requests.post(host+'/api/workflow/'+workflow_id+'/schedule')
        if response.status_code == 200:
            print('> Workflow Scheduled')
        else:
            print('> Unable to schedule workflow')
    else:
        return False


def schdeule_workflow(workflow_id,cron_rule):
    daemon_available = daemon_ping()
    if daemon_available:
        json = {}
        json['cron-rule'] = cron_rule
        response = requests.post(host+'/api/workflow/'+workflow_id+'/schedule')
        if response.status_code == 200:
            print('> Stopping workflow')
        else:
            print('> Unable to execute_workflow')
    else:
        return False


def list_workflows():
    plasma_config = get_config()
    workflows_path = plasma_config['paths']['workflows_path']
    workflows = os.listdir(workflows_path)
    if workflows:
        print('> listing workflows ')
        for item in workflows:
            if item.endswith('.yml'):
                print('\t- '+item)
        print()
    else:
        print('> no workflows have been created\n')

