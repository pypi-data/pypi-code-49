from __future__ import absolute_import

import os
import sys
import argparse
import logging
import ntpath
import json
import requests
import base64
import yaml
import docker
import boto3

from .launchers.launch_sast_scanner import run_sast_scanner
from .launchers.launch_dast_scanner import run_dast_scanner
from .launchers.launch_sca_scanner import run_sca_scanner
from .launchers.docker_util import get_formated_timestamp, create_skenoutput_folder, delete_skenoutput_folder

SKEN_SERVER_BASE_URL = 'https://cli.sken.ai/api'
#SKEN_SERVER_BASE_URL = 'http://localhost:8080/api'
LANGUAGES = ['ruby', 'javascript', 'typescript', 'python', 'php',
             'java', 'nodejs', 'license', 'go', 'python2']
SCANNERS = ['sast', 'dast', 'sca']
SECRETS = ['gitleaks']
config = {}
parsed_args = {}
scan_info = {}
scan_error_occurred = False

def get_scan_info():
    try:
        payload = {'projectId': config['projectid'], 'apiId': config['apiid']}
        resp = requests.get(SKEN_SERVER_BASE_URL + "/cli/getScanData", params=payload)
        global scan_info
        scan_info = resp.json()

        if not scan_info['success']:
            print('Failed to get scan info from sken server, ' + scan_info['message'])
            exit(0)
    except Exception as e:
        print('Failed to get scan info from sken server. ' + str(e))
        exit(0)

def read_config(build_dir):
    sken_config = {}
    succeed = False
    if os.path.exists(build_dir + 'sken.yaml'):
        with open(build_dir + 'sken.yaml', 'r') as stream:
            try:
                sken_config = yaml.safe_load(stream)
                sken_config['build_dir'] = build_dir
                succeed = True
            except yaml.YAMLError as exc:
                print('Read '+(build_dir + 'sken.yaml')+' failed, please check the content.')
                logging.exception(exc)
                exit(0)
    else:
        print('File not found: %s' % (build_dir + 'sken.yaml'))

    return succeed, sken_config

def get_build_dir():
    if  'build_dir' in config:
        return config['build_dir']

    build_dir = ''
    if parsed_args.path is not None:
        build_dir = parsed_args.path
    elif 'WORKSPACE' in os.environ:
        build_dir = os.environ['WORKSPACE']
    elif 'TRAVIS_BUILD_DIR' in os.environ:
        build_dir = os.environ['TRAVIS_BUILD_DIR']
    else:
        build_dir = os.getcwd()

    if not build_dir.endswith(os.path.sep):
        build_dir = build_dir + os.path.sep

    return build_dir

def combine_args_config(sken_config):
    if parsed_args.api_id is not None:
        sken_config['apiid'] = parsed_args.api_id

    if parsed_args.project_id is not None:
        sken_config['projectid'] = parsed_args.project_id

    if parsed_args.scanner is not None:
        sken_config['scanner'] = parsed_args.scanner

    if parsed_args.secrets is not None:
        sken_config['secrets'] = parsed_args.secrets

    if parsed_args.lang is not None:
        sken_config['language'] = parsed_args.lang
    
    if not 'variables' in sken_config or not type(sken_config['variables']) is dict:
        sken_config['variables'] = {}

    if parsed_args.dast_url is not None:
        sken_config['variables']['DAST_URL'] = parsed_args.dast_url

    if parsed_args.dast_full_scan is not None:
        sken_config['variables']['DAST_FULL_SCAN'] = parsed_args.dast_full_scan == 'yes'

def precheck():
    build_dir = get_build_dir()
    succeed, sken_config = read_config(build_dir)

    combine_args_config(sken_config)
    if not 'apiid' in sken_config or sken_config['apiid'] is None:
        print('Please specify "apiid" in sken.yaml or use --api_id flag.')
        exit(0)
    
    if not 'projectid' in sken_config or sken_config['projectid'] is None:
        print('Please specify "projectid" in sken.yaml or use --project_id flag.')
        exit(0)

    if not 'scanner' in sken_config or sken_config['scanner'] is None:
        print('Please specify "scanner" in sken.yaml or use --scanner flag.')
        exit(0)

    global config
    config = sken_config
    config['build_dir'] = build_dir

def select_scanner():
    # create skenoutput folder
    create_skenoutput_folder(config['build_dir'] + os.path.sep + 'skenoutput')

    scanners = config['scanner'].split(',')
    for scanner in scanners:
        scanner = scanner.lower()

        if not scanner in SCANNERS:
            print("Scanner for %s hasn't been supported." % scanner)
            continue
        
        if scanner == 'sast':
            print('SAST scanner selected')
            run_sast()
        elif scanner == 'license':
            print('License scanner selected')
            run_sast('license')
        elif scanner == 'dast':
            print('DAST scanner selected')
            dast_vars = config['variables']
            run_dast(dast_vars)
        elif scanner == 'sca':
            print('SCA scanner selected')
            run_sca()
        else:
            print("Scanner for %s hasn't been supported." % scanner)
            continue
    
    # remove skenoutput folder if all scans succeed
    if not scan_error_occurred:
        delete_skenoutput_folder()

def run_scan(scanner_type, scan_config):
    try:
        if scanner_type == 'sast':
            out_file, scan_start, scan_end = run_sast_scanner(scan_config)
        elif scanner_type == 'dast':
            out_file, scan_start, scan_end = run_dast_scanner(scan_config)
        elif scanner_type == 'sca':
            out_file, scan_start, scan_end = run_sca_scanner(scan_config)

        timing_file = generate_scan_result_file(scan_config['build_dir'], scan_start, scan_end)

        if os.path.exists(out_file):
            timestamp = upload_output(out_file, timing_file)
            trigger_etl(timestamp, ntpath.basename(out_file), scan_config['scanner'])
    except Exception as e:
        global scan_error_occurred
        scan_error_occurred = True
        print('Failed to run scan ' + str(e))

    return out_file, scan_start, scan_end

def run_dast(dast_vars):
    if 'DAST_URL' in dast_vars and dast_vars['DAST_URL'] is not None:
        dast_url = dast_vars['DAST_URL']
    else:
        print('Please specify "DAST_URL" in sken.yaml or use --dast_url comand flag')
        return

    full_scan = True
    if 'DAST_FULL_SCAN' in dast_vars and dast_vars['DAST_FULL_SCAN'] is not None:
        full_scan = dast_vars['DAST_FULL_SCAN']

    scanner = 'ZAP'
    run_scan('dast', {'scanner': scanner, 'build_dir': get_build_dir(), 'scan_info': scan_info, 'url': dast_url, 'full_scan': full_scan})

def run_sca():
    build_dir = get_build_dir()
    run_scan('sca', {'scanner': 'dependency-check', 'build_dir': build_dir, 'scan_info': scan_info})

def run_sast(p_code_lang=None):
    code_lang = ''
    if p_code_lang:
        code_lang = p_code_lang
    elif 'language' in config and config['language'] is not None:
        code_lang = config['language']

    if not code_lang or code_lang is None:
        print('Please specify "language" in sken.yaml or use --lang flag.')
        return

    build_dir = get_build_dir()
    code_lang = code_lang.lower()
    #secrets
    if 'secrets' in config:
        secrets = config['secrets'].lower()
        if secrets in SECRETS:
            code_lang = code_lang + ',' + secrets
        else:
            print('Unsupported secrets config: ' + secrets)

    languages = code_lang.split(',')

    for code_lang in languages:
        if code_lang in LANGUAGES:
            print('Supported language %s found' % code_lang)
            scanners = ''
            if code_lang == 'ruby':
                scanners = 'brakeman'
            elif code_lang == 'javascript':
                scanners = 'nodejsscan,eslintsec'
            elif code_lang == 'typescript':
                scanners = 'tslintsec'
            elif code_lang == 'license':
                scanners = 'licensescan'
            elif code_lang == 'go':
                scanners = 'gosec'
            elif code_lang == 'python2':
                if sys.version_info >= (3, 0):
                    print('Incompatible Python versions. Version 3 installed but Version 2 of Bandit requested.')
                    continue

                scanners = 'banditpy2'
            elif code_lang == 'python':
                if sys.version_info < (3, 0):
                    print('Incompatible Python versions. Version 2 installed but Version 3 of Bandit requested.')
                    continue

                scanners = 'banditpy3'
            elif code_lang == 'java':
                scanners = 'findsecbugs'
            elif code_lang == 'php':
                scanners = 'phpcs'
            
            if scanners:
                scanner_list = scanners.split(',')
                for scanner in scanner_list:
                    run_scan('sast', {'scanner': scanner , 'build_dir': build_dir, 'scan_info': scan_info})
            else:
                print("Scanner for %s hasn't been supported." % code_lang)
                continue
        else:
            if code_lang == 'gitleaks':
                run_scan('sast', {'scanner': code_lang , 'build_dir': build_dir, 'scan_info': scan_info})
            else:
                print('Unsupported secrets config: ' + secrets)
                continue

def generate_scan_result_file(build_dir, scan_start, scan_end):
    data = {
        'scanStart': scan_start,
        'scanEnd': scan_end
    }

    if not build_dir.endswith(os.path.sep):
        build_dir = build_dir + os.path.sep

    with open(build_dir + 'scan-timing.json', 'w') as f:
        f.write(json.dumps(data))
    
    return build_dir + 'scan-timing.json'

def upload_output(output_file, timing_file):
    print('Uploading output file...')
    timestamp = get_formated_timestamp()
    file_name = ''

    try:
        session = boto3.Session(
            aws_access_key_id=scan_info['awsAccessKeyId'], 
            aws_secret_access_key=scan_info['awsSecretAccessKey'], 
            region_name=scan_info['awsRegion'])

        s3 = session.resource('s3')
        file_name = ntpath.basename(output_file)
        data = open(output_file, 'rb')
        s3.Bucket('sken-scanner-output').put_object(Key=config['projectid'] + '/' + timestamp + '/' + file_name, Body=data)
        
        file_name = ntpath.basename(timing_file)
        data = open(timing_file, 'rb')
        s3.Bucket('sken-scanner-output').put_object(Key=config['projectid'] + '/' + timestamp + '/' + file_name, Body=data)
        print('Output file uploaded')
    except Exception as e:
        print('Failed to upload output file: ' + str(e))

    return timestamp

def trigger_etl(timestamp, fileName, scanner):
    print('ETL started')
    try:
        payload = {'projectId': config['projectid'], 'apiId': config['apiid'], 'timestamp': timestamp, 'fileName': fileName, 'scanner': scanner}
        resp = requests.get(SKEN_SERVER_BASE_URL + "/cli/doETL", params=payload)
        etl_result = resp.json()

        if not etl_result['success']:
            print(etl_result['message'])
            return

        print('ETL Succeeded')
    except Exception as e:
        print('Failed to trigger ETL: ' + str(e))

def main():
    parser = argparse.ArgumentParser(description='Sken Runner.')
    parser.add_argument('-s', '--scanner', metavar='scanner', choices=SCANNERS, help='support scanners: ' + ','.join(SCANNERS))
    parser.add_argument('-l' ,'--lang', metavar='language', choices=LANGUAGES, help='support languages: ' + ','.join(LANGUAGES))
    parser.add_argument('-p' ,'--path', metavar='project path', help='path of the project to be scanned.')
    parser.add_argument('--dast_url', metavar='DAST URL', help='URL to be scanned.')
    parser.add_argument('--dast_full_scan', metavar='DAST full scan', choices=['yes', 'no'], help='DAST full scan or quick scan.')
    parser.add_argument('--secrets', metavar='secrets config', help='secrets config.')

    parser.add_argument('--api_id', metavar='API ID', help='API Id.')
    parser.add_argument('--project_id', metavar='Project Id', help='Project Id.')
    global parsed_args
    parsed_args = parser.parse_args()
    
    precheck()
    get_scan_info()
    select_scanner()

if __name__ == "__main__":
    main()
