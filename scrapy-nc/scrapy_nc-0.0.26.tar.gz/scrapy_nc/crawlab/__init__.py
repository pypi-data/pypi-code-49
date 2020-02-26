import os

def get_task_id():
    return os.environ.get('CRAWLAB_TASK_ID')
