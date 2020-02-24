# Copyright 2020 Cognite AS
"""Cognite Geospatial API store and query spatial data.

 Spatial objects represent a revision of an object present in a geographic position at a point
 in time (or for all time if no time is specified). The object has a position according to a
 specific coordinate reference system and can be a point, linestring, polygon, or surface
 defined by a position in 3-dimensional space. Within the defined area, the object can have
 attributes or values associated with more specific points or areas.

"""
import base64
import os
from functools import partial

import numpy as np
from tornado import gen, ioloop

import cognite.geospatial.internal
from cognite.geospatial._raster import Raster
from cognite.geospatial.internal import (
    ExternalIdDTO,
    InternalIdDTO,
    SpatialDataRequestDTO,
    SpatialFilterDTO,
    SpatialIdsDTO,
    SpatialSearchRequestDTO,
)
from cognite.geospatial.internal.rest import ApiException

TORNADO_TIMEOUT_ERROR = 599
TORNADO_MESSAGE = "Could not get a response from the server. The server is down or timeout happens."


def _check_id(id: int):
    if id is not None and id > 9007199254740991:
        raise ValueError("Invalid value for `id`, must be a value less than or equal to `9007199254740991`")
    if id is not None and id < 1:
        raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")


def _check_external_id(external_id: str):
    if external_id is None:
        raise ValueError("Invalid value for `external_id`, must not be `None`")
    if external_id is not None and len(external_id) > 255:
        raise ValueError("Invalid value for `external_id`, length must be less than or equal to `255`")


def _throw_exception(ex):
    # check for tornado timout exception code
    if ex.status == TORNADO_TIMEOUT_ERROR:
        raise ApiException(status=TORNADO_TIMEOUT_ERROR, reason=TORNADO_MESSAGE)
    raise ex


def _check_id_geometry(id: int = None, external_id: str = None, geography=None):
    if id is None and external_id is None and geography is None:
        raise ValueError("Either id or external_id or geography must be provided")


def _check_either_external_id(id: int = None, external_id: str = None):
    if id is None and external_id is None:
        raise ValueError("Either id or external_id must be provided")


class CogniteGeospatialClient:

    """
    Main class for the seismic client
    """

    def __init__(
        self, api_key: str = None, base_url: str = None, port: int = None, project: str = None, timeout: int = 60000
    ):
        # configure env
        api_key = api_key or os.getenv("COGNITE_API_KEY")
        if api_key is None or not api_key.strip():
            raise ValueError(
                "You have either not passed an api key or not set the COGNITE_API_KEY environment variable."
            )
        self.configuration = cognite.geospatial.internal.Configuration()
        self.configuration.client_side_validation = False
        self.configuration.api_key["api-key"] = api_key.strip()

        base_url = base_url or "api.cognitedata.com"
        port = port or "443"
        self.configuration.host = base_url + ":" + str(port)

        api_client = cognite.geospatial.internal.ApiClient(self.configuration)
        self.api = cognite.geospatial.internal.SpatialApi(api_client)
        self.project = project
        self.timeout = timeout

    @gen.coroutine
    def get_spatial_info_async(self, id: int = None, external_id: str = None, project: str = None):
        """Retrieves spatial item information by internal ids or external ids.
        """
        _check_either_external_id(id, external_id)
        project = self._get_project(project)
        if id is not None:
            item = InternalIdDTO(id=id)
        elif external_id is not None:
            item = ExternalIdDTO(external_id=external_id)
        spatial_by_ids = SpatialIdsDTO(items=[item])
        try:
            response = yield self.api.by_ids_spatial_items(project, spatial_by_ids)
            if response is not None:
                items = response.items
                if len(items) > 0:
                    return items[0]
            return None
        except ApiException as e:
            _throw_exception(e)

    def get_spatial_info(self, id: int = None, external_id: str = None, project: str = None):
        """Retrieves spatial item information by internal ids or external ids.
        """
        run_func = partial(self.get_spatial_info_async, id, external_id, project)
        item = ioloop.IOLoop.current().run_sync(run_func, self.timeout)
        return item

    @gen.coroutine
    def get_spatial_async(self, id: int = None, external_id: str = None, project: str = None):
        """Retrieves spatial item data by internal ids or external ids.
        """
        _check_either_external_id(id, external_id)
        project = self._get_project(project)
        if id is not None:
            item = InternalIdDTO(id=id)
        elif external_id is not None:
            item = ExternalIdDTO(external_id=external_id)

        spatial_item = yield self.get_spatial_info_async(id=id, external_id=external_id, project=project)
        if spatial_item is None:
            return spatial_item

        try:
            response = yield self.api.get_spatial_items_data_names(project, item)
            if response is not None:
                # suport only rsater image
                raster = Raster(
                    id=spatial_item.id,
                    external_id=spatial_item.external_id,
                    name=spatial_item.name,
                    source=spatial_item.source,
                    crs=spatial_item.crs,
                    metadata=spatial_item.metadata,
                )
                for data_item in response.items:
                    data_request = SpatialDataRequestDTO(spatial_id=item, name=data_item.name)
                    data = yield self.api.get_spatial_items_data(project, data_request)
                    if data is not None and len(data.items) > 0:
                        ditem = data.items[0]
                        byte_buffer = base64.urlsafe_b64decode(ditem.value)
                        if ditem.type == "double":
                            vector = np.frombuffer(byte_buffer, dtype=np.double)
                            raster.add_double(data_item.name, vector)
                        elif ditem.type == "boolean":
                            vector = np.frombuffer(byte_buffer, dtype=np.uint8)
                            bit_array = np.unpackbits(vector, axis=0)
                            raster.add_boolean(data_item.name, np.array(bit_array, dtype=bool))
                        elif ditem.type == "text":
                            raster.add_text(data_item.name, str(byte_buffer, "utf-8"))

                return raster
            return None
        except ApiException as e:
            _throw_exception(e)

    def get_spatial(self, id: int = None, external_id: str = None, project: str = None):
        """Retrieves spatial item data by internal ids or external ids.
        """
        run_func = partial(self.get_spatial_async, id, external_id, project)
        result = ioloop.IOLoop.current().run_sync(run_func, self.timeout)
        return result

    @gen.coroutine
    def get_coverage_async(self, id: int = None, external_id: str = None, project: str = None):
        """Retrieves spatial item information by internal ids or external ids.
        """
        _check_either_external_id(id, external_id)
        project = self._get_project(project)
        if id is not None:
            item = InternalIdDTO(id=id)
        elif external_id is not None:
            item = ExternalIdDTO(external_id=external_id)
        spatial_by_ids = SpatialIdsDTO(items=[item])
        try:
            response = yield self.api.get_spatial_coverage(project, spatial_by_ids)
            if response is not None:
                items = response.items
                if len(items) > 0:
                    return items[0]
            return None
        except ApiException as e:
            _throw_exception(e)

    def get_coverage(self, id: int = None, external_id: str = None, project: str = None):
        """Retrieves spatial item information by internal ids or external ids.
        """
        run_func = partial(self.get_coverage_async, id, external_id, project)
        item = ioloop.IOLoop.current().run_sync(run_func, self.timeout)
        return item

    @gen.coroutine
    def find_spatial_async(
        self,
        spatial_type: str = None,
        metadata=None,
        geography: str = None,
        crs: str = None,
        limit: int = 10,
        project: str = None,
    ):
        """Searches and returns the spatial items based on resource type content or coordinates.
        """
        project = self._get_project(project)

        spatial_search_request = SpatialSearchRequestDTO(crs=crs, limit=limit)
        # spatial_search_request.limit(limit)
        if spatial_type is not None:
            spatial_search_request.type = spatial_type
        if metadata is not None:
            spatial_search_request.metadata = metadata
        if geography is not None:
            geometry = self._create_geometry(geography=geography)
            spatial_filter = SpatialFilterDTO("within", geometry, local_vars_configuration=self.configuration)

        try:
            response = yield self.api.search_spatial(project, spatial_search_request_dto=spatial_search_request)
            return response
        except ApiException as e:
            _throw_exception(e)

    def find_spatial(
        self,
        spatial_type: str = None,
        metadata=None,
        geography: str = None,
        crs: str = None,
        limit: int = 10,
        project: str = None,
    ):
        """Searches and returns the spatial items based on resource type content or coordinates.
        """
        run_func = partial(self.find_spatial_async, spatial_type, metadata, geography, crs, limit, project)
        result = ioloop.IOLoop.current().run_sync(run_func, self.timeout)
        return result

    @gen.coroutine
    def find_within_async(
        self,
        id: int = None,
        external_id: str = None,
        geography: str = None,
        distance=None,
        crs: str = None,
        limit: int = 10,
        project: str = None,
    ):
        """Selects features in the input feature layer within or contained by features in the selecting features layer.
        """
        project = self._get_project(project)
        geometry = self._create_geometry(id, external_id, geography)
        spatial_filter = SpatialFilterDTO(
            "within", geometry=geometry, distance_meter=distance, local_vars_configuration=self.configuration
        )
        spatial_search_request = SpatialSearchRequestDTO(
            limit=limit,
            name=None,
            start_time=None,
            end_time=None,
            metadata=None,
            asset_ids=None,
            source=None,
            created_time=None,
            last_updated_time=None,
            external_id_prefix=None,
            type=None,
            spatial_filter=spatial_filter,
            crs=crs,
        )

        try:
            response = yield self.api.search_spatial(project, spatial_search_request_dto=spatial_search_request)
            return response
        except ApiException as e:
            _throw_exception(e)

    def find_within(
        self,
        id: int = None,
        external_id: str = None,
        geography: str = None,
        distance=None,
        crs: str = None,
        limit: int = 10,
        project: str = None,
    ):
        """Selects features in the input feature layer within or contained by features in the selecting features layer.
        """
        run_func = partial(self.find_within_async, id, external_id, geography, distance, crs, limit, project)
        result = ioloop.IOLoop.current().run_sync(run_func, self.timeout)
        return result

    @gen.coroutine
    def find_within_completely_async(
        self,
        id: int = None,
        external_id: str = None,
        geography: str = None,
        distance=None,
        crs: str = None,
        limit: int = 10,
        project: str = None,
    ):

        """The result is identical to Within except when the feature in the input feature layer intersects the boundary of the feature in the selecting features layer; then it is not selected.
        """
        project = self._get_project(project)
        geometry = self._create_geometry(id, external_id, geography)
        spatial_filter = SpatialFilterDTO("completely_within", geometry, local_vars_configuration=self.configuration)
        spatial_search_request = SpatialSearchRequestDTO(
            limit=limit,
            name=None,
            start_time=None,
            end_time=None,
            metadata=None,
            asset_ids=None,
            source=None,
            created_time=None,
            last_updated_time=None,
            external_id_prefix=None,
            type=None,
            spatial_filter=spatial_filter,
            crs=crs,
        )
        try:
            response = yield self.api.search_spatial(project, spatial_search_request_dto=spatial_search_request)
            return response
        except ApiException as e:
            _throw_exception(e)

    def find_within_completely(
        self,
        id: int = None,
        external_id: str = None,
        geography: str = None,
        distance=None,
        crs: str = None,
        limit: int = 10,
        project: str = None,
    ):
        """The result is identical to Within except when the feature in the input feature layer intersects the boundary of the feature in the selecting features layer; then it is not selected.
        """
        run_func = partial(self.find_within_completely_async, id, external_id, geography, distance, crs, limit, project)
        result = ioloop.IOLoop.current().run_sync(run_func, self.timeout)
        return result

    def _create_geometry(self, id: int = None, external_id: str = None, geography: str = None):
        _check_id_geometry(id, external_id, geography)
        if id is not None:
            _check_id(id)
        if external_id is not None:
            _check_external_id(external_id)
        return cognite.geospatial.internal.GeometryDTO(
            id=id, external_id=external_id, wkt=geography, local_vars_configuration=self.configuration
        )

    def _get_project(self, project: str = None):
        if project is None and self.project is None:
            raise ValueError("Project mus be provided")
        return project if project is not None else self.project
