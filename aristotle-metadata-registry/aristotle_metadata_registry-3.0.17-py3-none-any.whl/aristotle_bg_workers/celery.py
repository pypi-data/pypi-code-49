from celery import Celery

# from celery.schedules import crontab
# from aristotle_bg_workers.tasks import recache_visibility

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aristotle_mdr.settings')

app = Celery('aristotle')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
# app.autodiscover_tasks(related_name='downloader')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# TODO: finish setting up periodic tasks
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     """A helper function to setup periodic tasks"""
#     sender.add_periodic_task(
#         crontab()
#     )


