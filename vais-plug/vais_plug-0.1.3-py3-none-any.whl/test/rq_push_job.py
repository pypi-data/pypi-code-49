from rq import Queue
from redis import Redis
# from worker.rq_worker import count_words_at_url
import time
from vais_plugin.plugin_config import *

# Tell RQ what Redis connection to use
redis_conn = Redis(host='localhost', port=6379)
q = Queue('skeleton_job_test/normal', connection=redis_conn)  # no args implies the default queue

config = Config()
config.add_user_config(
    EditText(config_code='key_ignore', title="Keyword ignored", description="List of words will be ignored"))

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue('sample_plugin.handle_job', *['emas',
                                              '5de0943f936aa200080a5cbf',
                                              {
                                                  "audio_info/normal": {
                                                      "data": {
                                                          "bucket": "test",
                                                          "key": "4596.mp3",
                                                          "audio_id": "5de48f4cf9bb550006069230"
                                                      }
                                                  }
                                              },
                                              None,
                                              None])
print(job.result)  # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result)  # => 889
