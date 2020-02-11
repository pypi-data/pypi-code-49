from rq import Queue
from redis import Redis
# from worker.rq_worker import count_words_at_url
import time

# Tell RQ what Redis connection to use
redis_conn = Redis(host='localhost', port=6379)
q = Queue('skeleton_job_test/normal', connection=redis_conn)  # no args implies the default queue

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
                                              None])
print(job.result)  # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result)  # => 889
