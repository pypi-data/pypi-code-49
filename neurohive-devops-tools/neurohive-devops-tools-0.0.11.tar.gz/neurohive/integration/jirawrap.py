import os, sys
import logging
import argparse

from jira import JIRA


JIRA_USERNAME = os.getenv('JIRA_USERNAME')
JIRA_TOKEN = os.getenv('JIRA_TOKEN')

if not JIRA_TOKEN or not JIRA_USERNAME:
    logging.error('Enter credentials JIRA_TOKEN|JIRA_USERNAME')
    sys.exit(1)


def add_comment(server, task_id, comment):
    jira = JIRA(
        server=server,
        basic_auth=(JIRA_USERNAME, JIRA_TOKEN))
    jira.add_comment(task_id, comment)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', required=True)
    parser.add_argument('--task-id', required=True)
    parser.add_argument('--comment', required=True)
    args = parser.parse_args()
    add_comment(args.server, args.task_id, args.comment)

