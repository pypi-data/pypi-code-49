from django.conf import settings
import time
from .models import ActionEvent


def record_action_start(request, action_id, object_id):
    with_track = getattr(settings, 'TRACK_ACTIONS', True)
    if not with_track:
        return None
    event = ActionEvent()
    event.request_data = request.data
    event.action_id = action_id
    event.object_id = object_id
    has_user = getattr(request, 'user')
    if has_user:
        event.actor_id = request.user.id
    start = time.perf_counter()
    return (start, event)


def record_action_end(start, event, response):
    stop = time.perf_counter()
    with_track = getattr(settings, 'TRACK_ACTIONS', True)
    if not with_track:
        return None

    duration = (stop - start)
    print('duration: ', duration)
    event.duration = duration
    event.complete = True
    event.response_data = response.data
    event.status_code = response.status_code
    event.save()
    return event
