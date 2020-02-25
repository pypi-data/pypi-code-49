from starsheep.listeners.listener import Listener


class RejectListener(Listener):
    reason = None

    def __init__(self, listener_name, document, context):
        super(RejectListener, self).__init__(listener_name, document, context)

        if 'reason' not in document:
            raise Exception('Missing "reason" in listener ' + listener_name)
        self.reason = document['reason']

    def starsheep_apply(self, listener_filter):
        if isinstance(listener_filter, str):
            self.apply(listener_filter)
        elif isinstance(listener_filter, list):
            for f in listener_filter:
                self.apply(f)

    def on_create(self, object_id, key):
        if 'create' in self.call_on:
            raise Exception(self.reason)

    def on_created(self, object_id, key):
        if 'created' in self.call_on:
            raise Exception(self.reason)

    def on_owned_create(self, object_id, key):
        if 'owned_created' in self.call_on:
            raise Exception(self.reason)

    # Before update
    def on_update(self, object_id, field, old_value, new_value):
        if 'update' in self.call_on:
            raise Exception(self.reason)

    def on_owned_update(self, object_id, field, old_value, new_value):
        if 'owned_update' in self.call_on:
            raise Exception(self.reason)

    def on_authorized_update(self, object_id, field, old_value, new_value):
        if 'authorized_update' in self.call_on:
            raise Exception(self.reason)

    def on_unauthorized_update(self, object_id, field, old_value, new_value):
        if 'unauthorized_update' in self.call_on:
            raise Exception(self.reason)

    # After updated
    def on_updated(self, object_id, field, old_value, new_value):
        if 'updated' in self.call_on:
            raise Exception(self.reason)

    def on_owned_updated(self, object_id, field, old_value, new_value):
        if 'owned_updated' in self.call_on:
            raise Exception(self.reason)

    def on_authorized_updated(self, object_id, field, old_value, new_value):
        if 'authorized_updated' in self.call_on:
            raise Exception(self.reason)

    def on_unauthorized_updated(self, field, old_value, new_value):
        if 'unauthorized_updated' in self.call_on:
            raise Exception(self.reason)

    # Before field delete
    def on_delete(self, object_id, field, value):
        if 'delete' in self.call_on:
            raise Exception(self.reason)

    def on_owned_delete(self, object_id, field, value):
        if 'owned_delete' in self.call_on:
            raise Exception(self.reason)

    def on_authorized_delete(self, object_id, field, value):
        if 'authorized_delete' in self.call_on:
            raise Exception(self.reason)

    def on_unauthorized_delete(self, object_id, field, value):
        if 'unauthorized_delete' in self.call_on:
            raise Exception(self.reason)

    # After field deleted
    def on_deleted(self, object_id, field, value):
        if 'deleted' in self.call_on:
            raise Exception(self.reason)

    def on_owned_deleted(self, object_id, field, value):
        if 'owned_deleted' in self.call_on:
            raise Exception(self.reason)

    def on_authorized_deleted(self, object_id, field, value):
        if 'authorized_deleted' in self.call_on:
            raise Exception(self.reason)

    def on_unauthorized_deleted(self, object_id, field, value):
        if 'unauthorized_deleted' in self.call_on:
            raise Exception(self.reason)

    # Before whole object removed
    def on_remove(self, object_id):
        if 'remove' in self.call_on:
            raise Exception(self.reason)

    def on_owned_remove(self, object_id):
        if 'owned_remove' in self.call_on:
            raise Exception(self.reason)

    def on_authorized_remove(self, object_id):
        if 'authorized_remove' in self.call_on:
            raise Exception(self.reason)

    def on_unauthorized_remove(self, object_id):
        if 'unauthorized_remove' in self.call_on:
            raise Exception(self.reason)
