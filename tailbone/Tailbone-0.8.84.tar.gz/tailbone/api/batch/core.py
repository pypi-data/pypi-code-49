# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2019 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Tailbone Web API - Batch Views
"""

from __future__ import unicode_literals, absolute_import

import six

from rattail.time import localtime
from rattail.util import load_object

from cornice import resource

from tailbone.api import APIMasterView


class APIBatchMixin(object):
    """
    Base class for all API views which are meant to handle "batch" *and/or*
    "batch row" data.
    """

    def get_batch_class(self):
        model_class = self.get_model_class()
        if hasattr(model_class, '__batch_class__'):
            return model_class.__batch_class__
        return model_class

    def get_handler(self):
        """
        Returns a `BatchHandler` instance for the view.  All (?) custom batch
        API views should define a default handler class; however this may in all
        (?)  cases be overridden by config also.  The specific setting required
        to do so will depend on the 'key' for the type of batch involved, e.g.
        assuming the 'vendor_catalog' batch:

        .. code-block:: ini

           [rattail.batch]
           vendor_catalog.handler = myapp.batch.vendorcatalog:CustomCatalogHandler

        Note that the 'key' for a batch is generally the same as its primary
        table name, although technically it is whatever value returns from the
        ``batch_key`` attribute of the main batch model class.
        """
        key = self.get_batch_class().batch_key
        spec = self.rattail_config.get('rattail.batch', '{}.handler'.format(key),
                                       default=self.default_handler_spec)
        return load_object(spec)(self.rattail_config)


class APIBatchView(APIBatchMixin, APIMasterView):
    """
    Base class for all API views which are meant to handle "batch" *and/or*
    "batch row" data.
    """
    supports_toggle_complete = False

    def __init__(self, request, **kwargs):
        super(APIBatchView, self).__init__(request, **kwargs)
        self.handler = self.get_handler()

    def normalize(self, batch):

        created = batch.created
        created = localtime(self.rattail_config, created, from_utc=True)
        created = self.pretty_datetime(created)

        executed = batch.executed
        if executed:
            executed = localtime(self.rattail_config, executed, from_utc=True)
            executed = self.pretty_datetime(executed)

        return {
            'uuid': batch.uuid,
            '_str': six.text_type(batch),
            'id': batch.id,
            'id_str': batch.id_str,
            'description': batch.description,
            'notes': batch.notes,
            'rowcount': batch.rowcount,
            'created': created,
            'created_by_uuid': batch.created_by.uuid,
            'created_by_display': six.text_type(batch.created_by),
            'complete': batch.complete,
            'executed': executed,
            'executed_by_uuid': batch.executed_by_uuid,
            'executed_by_display': six.text_type(batch.executed_by or ''),
        }

    def create_object(self, data):
        """
        Create a new object instance and populate it with the given data.

        Here we'll invoke the handler for actual batch creation, instead of
        typical logic used for simple records.
        """
        user = self.request.user
        kwargs = dict(data)
        kwargs['user'] = user
        batch = self.handler.make_batch(self.Session(), **kwargs)
        if self.handler.should_populate(batch):
            self.handler.do_populate(batch, user)
        return batch

    def update_object(self, batch, data):
        """
        Logic for updating a main object record.

        Here we want to make sure we set "created by" to the current user, when
        creating a new batch.
        """
        # we're only concerned with *new* batches here
        if not batch.uuid:

            # assign creator; initialize row count
            batch.created_by_uuid = self.request.user.uuid
            if batch.rowcount is None:
                batch.rowcount = 0

        # then go ahead with usual logic
        return super(APIBatchView, self).update_object(batch, data)

    def mark_complete(self):
        """
        Mark the given batch as "complete".
        """
        batch = self.get_object()

        if batch.executed:
            return {'error': "Batch {} has already been executed: {}".format(
                batch.id_str, batch.description)}

        if batch.complete:
            return {'error': "Batch {} is already marked complete: {}".format(
                batch.id_str, batch.description)}

        batch.complete = True
        return self._get(obj=batch)

    def mark_incomplete(self):
        """
        Mark the given batch as "incomplete".
        """
        batch = self.get_object()

        if batch.executed:
            return {'error': "Batch {} has already been executed: {}".format(
                batch.id_str, batch.description)}

        if not batch.complete:
            return {'error': "Batch {} is already marked incomplete: {}".format(
                batch.id_str, batch.description)}

        batch.complete = False
        return self._get(obj=batch)

    @classmethod
    def defaults(cls, config):
        cls._batch_defaults(config)

    @classmethod
    def _batch_defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        permission_prefix = cls.get_permission_prefix()
        collection_url_prefix = cls.get_collection_url_prefix()
        object_url_prefix = cls.get_object_url_prefix()

        # primary / typical API
        resource.add_view(cls.collection_get, permission='{}.list'.format(permission_prefix))
        resource.add_view(cls.collection_post, permission='{}.create'.format(permission_prefix))
        resource.add_view(cls.get, permission='{}.view'.format(permission_prefix))
        batch_resource = resource.add_resource(cls, collection_path=collection_url_prefix,
                                               path='{}/{{uuid}}'.format(object_url_prefix))
        config.add_cornice_resource(batch_resource)

        if cls.supports_toggle_complete:

            # mark complete
            config.add_route('{}.mark_complete'.format(route_prefix), '{}/{{uuid}}/mark-complete'.format(object_url_prefix))
            config.add_view(cls, attr='mark_complete', route_name='{}.mark_complete'.format(route_prefix),
                            permission='{}.edit'.format(permission_prefix),
                            renderer='json')

            # mark incomplete
            config.add_route('{}.mark_incomplete'.format(route_prefix), '{}/{{uuid}}/mark-incomplete'.format(object_url_prefix))
            config.add_view(cls, attr='mark_incomplete', route_name='{}.mark_incomplete'.format(route_prefix),
                            permission='{}.edit'.format(permission_prefix),
                            renderer='json')


# TODO: deprecate / remove this
BatchAPIMasterView = APIBatchView


class APIBatchRowView(APIBatchMixin, APIMasterView):
    """
    Base class for all API views which are meant to handle "batch rows" data.
    """
    supports_quick_entry = False

    def __init__(self, request, **kwargs):
        super(APIBatchRowView, self).__init__(request, **kwargs)
        self.handler = self.get_handler()

    def normalize(self, row):
        batch = row.batch
        return {
            'uuid': row.uuid,
            '_str': six.text_type(row),
            '_parent_str': six.text_type(batch),
            '_parent_uuid': batch.uuid,
            'batch_uuid': batch.uuid,
            'batch_id': batch.id,
            'batch_id_str': batch.id_str,
            'batch_description': batch.description,
            'sequence': row.sequence,
            'status_code': row.status_code,
            'status_display': row.STATUS.get(row.status_code, six.text_type(row.status_code)),
        }

    def quick_entry(self):
        """
        View for handling "quick entry" user input, for a batch.
        """
        data = self.request.json_body

        uuid = data['batch_uuid']
        batch = self.Session.query(self.get_batch_class()).get(uuid)
        if not batch:
            raise self.notfound()

        entry = data['quick_entry']

        try:
            row = self.handler.quick_entry(self.Session(), batch, entry)
        except Exception as error:
            msg = six.text_type(error)
            if not msg and isinstance(error, NotImplementedError):
                msg = "Feature is not implemented"
            return {'error': msg}

        self.Session.flush()
        result = self._get(obj=row)
        result['ok'] = True
        return result

    @classmethod
    def defaults(cls, config):
        cls._batch_row_defaults(config)

    @classmethod
    def _batch_row_defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        permission_prefix = cls.get_permission_prefix()
        collection_url_prefix = cls.get_collection_url_prefix()
        object_url_prefix = cls.get_object_url_prefix()

        resource.add_view(cls.collection_get, permission='{}.view'.format(permission_prefix))
        resource.add_view(cls.get, permission='{}.view'.format(permission_prefix))
        rows_resource = resource.add_resource(cls, collection_path=collection_url_prefix,
                                              path='{}/{{uuid}}'.format(object_url_prefix))
        config.add_cornice_resource(rows_resource)

        if cls.supports_quick_entry:

            # quick entry
            config.add_route('{}.quick_entry'.format(route_prefix), '{}/quick-entry'.format(collection_url_prefix),
                             request_method=('OPTIONS', 'POST'))
            config.add_view(cls, attr='quick_entry', route_name='{}.quick_entry'.format(route_prefix),
                            permission='{}.edit'.format(permission_prefix),
                            renderer='json')
