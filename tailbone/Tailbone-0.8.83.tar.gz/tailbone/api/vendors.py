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
Tailbone Web API - Vendor Views
"""

from __future__ import unicode_literals, absolute_import

import six

from rattail.db import model

from cornice import Service
from cornice.resource import resource, view

from tailbone.api import APIMasterView


@resource(collection_path='/vendors', path='/vendor/{uuid}')
class VendorView(APIMasterView):

    model_class = model.Vendor
    autocomplete_fieldname = 'name'

    def normalize(self, vendor):
        return {
            'uuid': vendor.uuid,
            '_str': six.text_type(vendor),
            'id': vendor.id,
            'name': vendor.name,
        }

    @view(permission='vendors.list')
    def collection_get(self):
        return self._collection_get()

    @view(permission='vendors.create')
    def collection_post(self):
        return self._collection_post()

    @view(permission='vendors.view')
    def get(self):
        return self._get()

    @view(permission='vendors.edit')
    def post(self):
        return self._post()


def includeme(config):
    config.scan(__name__)

    autocomplete = Service(name='vendors.autocomplete', path='/vendors/autocomplete')
    autocomplete.add_view('GET', 'autocomplete', klass=VendorView)
    config.add_cornice_service(autocomplete)
