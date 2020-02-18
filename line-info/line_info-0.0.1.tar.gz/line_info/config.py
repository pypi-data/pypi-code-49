import json
import os

CONFIG_PATH = os.path.join(os.path.expanduser("~"), '.line_info_config.json')

JIRA_ISSUE_REGEX = r'[A-Z]{1,20}-\d{1,20}'
VCS_ISSUE_REGEX = r'#\d{1,99}'

JIRA_DOMAIN = None
GITLAB_TOKEN = None

__globals__ = globals()
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH) as config:
        __globals__.update(json.load(config))

for mutual_key in (__globals__.keys() & os.environ.keys()):
    if mutual_key.isupper():
        __globals__[mutual_key] = os.environ[mutual_key]
