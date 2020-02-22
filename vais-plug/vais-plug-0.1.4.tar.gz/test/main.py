#!/usr/bin/env python
import logging
import os

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
from test import sample_plugin

if not os.environ.get('PLUGIN_CODE'):
    os.environ['BACKEND_ENDPOINT'] = 'http://192.168.1.193:8888/api/v1/plugins'
    os.environ['REDIS_HOST'] = 'localhost'
    os.environ['REDIS_PORT'] = '6379'
    os.environ['JOB_QUEUE'] = 'skeleton_job_test'
    os.environ['PLUGIN_CODE'] = 'skeleton'
    os.environ['DEPENDED_PLUGIN_CODE'] = 'audio_info'
    os.environ['PLUGIN_NAME'] = 'Skeleton Plugin'
    os.environ['PLUGIN_DESCRIPTION'] = 'Skeleton Plugin description'
    os.environ['CONFIG_FILE'] = './config.yam'

if __name__ == "__main__":
    my_plugin = sample_plugin.SamplePlugin()
    my_plugin.run(sample_plugin.__file__, sample_plugin.handle_job,
                  sample_plugin.SamplePlugin.VERSION_CODE, ignore_register=True)
    # from apscheduler.schedulers.background import BackgroundScheduler
    # import time
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(lambda: print(time.time()), 'interval', seconds=5)
    # scheduler.start()
    # time.sleep(30)
    # scheduler.shutdown()
