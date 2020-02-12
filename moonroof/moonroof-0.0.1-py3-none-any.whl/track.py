def track(queue, endpoint, data):
    queue.put({'endpoint': endpoint, **data})
