from django.conf import settings

VERSION = '1.0.4'

REST_FILE_MANAGER = getattr(settings, 'REST_FILE_MANAGER', {})
UPLOADS_DIR = REST_FILE_MANAGER.get('UPLOADS_DIR', 'files/')
