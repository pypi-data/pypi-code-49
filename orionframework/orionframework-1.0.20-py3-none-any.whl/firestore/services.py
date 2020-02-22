import os

import firebase_admin
from django.conf import settings
from django.utils.functional import cached_property
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from firebase_admin import credentials, firestore

from orionframework.middleware import get_user
from orionframework.utils import lists
from orionframework.utils.booleans import to_boolean


class FirestoreChangeSynchronizer(object):
    enabled = getattr(settings, 'ORION_FIRESTORE_SYNC_ENABLED', True)
    debug = getattr(settings, 'ORION_FIRESTORE_SYNC_DEBUG', True)

    def __init__(self, collection, enabled=None, debug=None):
        self.collection = collection

        self.enabled = to_boolean(enabled, FirestoreChangeSynchronizer.enabled)
        self.debug = to_boolean(enabled, FirestoreChangeSynchronizer.debug)

    @cached_property
    def store(self):
        return firestore.client()

    def get(self, record, record_id=None):
        values = [str(value) for value in (lists.as_list(self.collection) + [record_id or record.id])]
        path = "/".join(values)
        if self.debug:
            print("Firestore path: " + path)
        return self.store.document(path)

    def log(self, record, record_id=None, modified_by=None, **kwargs):
        if not self.enabled:
            return

        if not modified_by:
            user = get_user()
            if user:
                modified_by = user.id

        doc = self.get(record, record_id)

        data = {
            "modified_by": modified_by
        }

        if isinstance(record, ActivatorModel):
            data.update({
                'status': record.status
            })

        if isinstance(record, TimeStampedModel):
            data.update({
                'modified': record.modified
            })

        data.update(kwargs)

        doc.set(data, merge=True)
