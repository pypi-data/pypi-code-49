# Copyright (C) 2018-2019  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

from swh.web.common import service, utils
from swh.web.common.utils import (
        resolve_swh_persistent_id,
        get_persistent_identifier
)
from swh.web.api.apidoc import api_doc, format_docstring
from swh.web.api.apiurls import api_route


@api_route(r'/resolve/(?P<swh_id>.*)/',
           'api-1-resolve-swh-pid')
@api_doc('/resolve/')
@format_docstring()
def api_resolve_swh_pid(request, swh_id):
    """
    .. http:get:: /api/1/resolve/(swh_id)/

        Resolve a Software Heritage persistent identifier.

        Try to resolve a provided `persistent identifier <https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html>`_
        into an url for browsing the pointed archive object. If the provided
        identifier is valid, the existence of the object in the archive
        will also be checked.

        :param string swh_id: a Software Heritage persistent identifier

        :>json string browse_url: the url for browsing the pointed object
        :>json object metadata: object holding optional parts of the persistent identifier
        :>json string namespace: the persistent identifier namespace
        :>json string object_id: the hash identifier of the pointed object
        :>json string object_type: the type of the pointed object
        :>json number scheme_version: the scheme version of the persistent identifier

        {common_headers}

        **Allowed HTTP Methods:** :http:method:`get`, :http:method:`head`, :http:method:`options`

        :statuscode 200: no error
        :statuscode 400: an invalid persistent identifier has been provided
        :statuscode 404: the pointed object does not exist in the archive

        **Example:**

        .. parsed-literal::

            :swh_web_api:`resolve/swh:1:rev:96db9023b881d7cd9f379b0c154650d6c108e9a3;origin=https://github.com/openssl/openssl/`
    """  # noqa
    # try to resolve the provided pid
    swh_id_resolved = resolve_swh_persistent_id(swh_id)
    # id is well-formed, now check that the pointed
    # object is present in the archive, NotFoundExc
    # will be raised otherwise
    swh_id_parsed = swh_id_resolved['swh_id_parsed']
    object_type = swh_id_parsed.object_type
    object_id = swh_id_parsed.object_id
    service.lookup_object(object_type, object_id)
    # id is well-formed and the pointed object exists
    swh_id_data = swh_id_parsed._asdict()
    swh_id_data['browse_url'] = request.build_absolute_uri(
        swh_id_resolved['browse_url'])
    return swh_id_data


@api_route(r'/known/',
           'api-1-swh-pid-known', methods=['POST'])
@api_doc('/known/', noargs=True, tags=['hidden'])
@format_docstring()
def api_swh_pid_known(request):
    """
    .. http:post:: /api/1/known/

        Check if a list of Software Heritage persistent identifier is present
        in the archive depending on their id (sha1_git).

        Returns:
            A dictionary with:
                keys(str): Persistent identifier
                values(dict): A dictionary containing the key 'known'. (true if
                the pid is present, False otherwise)

    """
    persistent_ids = [get_persistent_identifier(pid)
                      for pid in request.data]

    response = {str(pid): {'known': False} for pid in persistent_ids}

    # group pids by their type
    pids_by_type = utils.group_swh_persistent_identifiers(persistent_ids)
    # search for hashes not present in the storage
    missing_hashes = service.lookup_missing_hashes(pids_by_type)

    for pid in persistent_ids:
        if pid.object_id not in missing_hashes:
            response[str(pid)]['known'] = True

    return response
