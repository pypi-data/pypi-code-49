import sys
sys.dont_write_bytecode = True
from Slack import Slack

 
slack = Slack()
slack.notify_slack_channel(None)