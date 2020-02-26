import datetime
import json
import logging
import uuid
from copy import deepcopy
from typing import Dict, List

from cognite.client import CogniteClient
from cognite.client.data_classes.assets import Asset, AssetFilter, AssetList
from cognite.client.data_classes.time_series import TimeSeries, TimeSeriesFilter, TimeSeriesList

CURRENT_VERSION = 3
DATAKIT_TABLE_NAME = "datakits"
RESOURCE_TYPE_APIS = ["time_series", "assets", "files", "events"]

log = logging.getLogger("cognite-sdk")


class DataKitAPI:
    """The Data Kit API
    -------------------
    The data kit are combinations of all our other resource types packaged
    in a authenticated and sharable object. It can for example contain multiple
    resources: assets, time series, files etc. By design, the resources are
    lazily loaded and the actual data objects can only be loaded from the
    DataKit Class which is what this API interacts with. In other words, only
    the resource *queries* are stored in the data base and in the DataKit Class."""

    def __init__(self, cognite_client):

        self.client = cognite_client

        # Create db
        self.database = self.client.config.client_name
        db_list = self.client.raw.databases.list(limit=-1)
        names = [db.name for db in db_list]
        if self.database not in names:
            self.client.raw.databases.create(self.database)

        # Create table
        self.table = DATAKIT_TABLE_NAME
        tables = self.client.raw.tables.list(self.database, limit=-1)
        if tables.to_pandas().empty or self.table not in tables.to_pandas().name.values:
            self.client.raw.tables.create(self.database, self.table)

    def create(self, datakit):
        """Create a datakit and persist it in a data store for future retrieval.
        Resources cannot be added using this method; for this the user must call
        *update* after adding resources to the data kit.

        Parameters
        ----------
        datakit : DataKit
            The locally created data kit.

        Returns
        -------
        DataKit
            The created data kit
        """

        if datakit.id is None:
            datakit.id = str(uuid.uuid4())

        time_now = datetime.datetime.now()
        datakit.created_time = int(time_now.timestamp())
        datakit.last_updated_time = datakit.created_time

        rows = {
            datakit.id: {
                "name": datakit.name,
                "description": datakit.description,
                "resources": json.dumps(datakit.resources),
                "createdTime": datakit.created_time,
                "lastUpdatedTime": datakit.last_updated_time,
                "id": datakit.id,
                "externalId": datakit.external_id,
                "metadata": json.dumps(datakit.metadata),
                "version": CURRENT_VERSION,
            }
        }

        self.client.raw.rows.insert(self.database, self.table, row=rows)
        log.info(f"Datakit {datakit.id} created.")
        return datakit

    def delete(self, id: str):
        """Delete the data kit from the persistent data store.

        Parameters
        ----------
        id : str
            The id of the data kit to delete.
        """
        self._delete_multiple([id])
        log.info(f"Datakit {id} deleted.")

    def _delete_multiple(self, ids: List):
        self.client.raw.rows.delete(self.database, self.table, key=ids)

    def retrieve(self, id: str):
        """Retrieve Data Kit from persistent data store.

        Parameters
        ----------
        id : str
            The id of the data kit to retrieve.

        Returns
        -------
        Optional[DataKit]
            The datakit to return
        """
        row = self.client.raw.rows.retrieve(self.database, self.table, key=id)
        if row is not None:
            result = DataKit.from_db_row(self.client, row)
        else:
            result = None

        return result

    def update(self, datakit):
        """Update the data kit. This will add any new resources that were added to
        the data kit locally to the persistent data store.

        Args:
            datakit (DataKit):

        Returns
        -------
            DataKit
                The data kit which was updated
        """

        current = self.client.raw.rows.retrieve(self.database, self.table, key=datakit.id)

        current.columns["resources"] = json.dumps(datakit.resources)
        current.columns["lastUpdatedTime"] = int(datetime.datetime.now().timestamp())

        self.client.raw.rows.insert(self.database, self.table, current)

        return datakit


class DataKit:
    """Data Kits:
    A data kit is a combination of other data types in CDF."""

    # assets:
    #     Optional[List[AssetList]] = None
    # time_series:
    #     Optional[List[TimeSeriesList]] = None
    # files:
    #     Optional[List[FileMetadataList]] = None
    # name:
    #     str = "Data kit"

    def __init__(
        self,
        cognite_client=None,
        external_id: str = None,
        name: str = None,
        description: str = None,
        created_time: int = None,
        last_updated_time: int = None,
        metadata: Dict[str, str] = {},  # noqa
    ):

        if cognite_client is None:
            self.client = CogniteClient()
        else:
            self.client = cognite_client

        self.name = name
        empty_resource: Dict[str, List] = {"filters": [], "ids": []}

        self.resources = {
            "assets": deepcopy(empty_resource),
            "time_series": deepcopy(empty_resource),
            "events": deepcopy(empty_resource),
            "files": deepcopy(empty_resource),
        }
        self.description = description
        self.external_id = external_id
        self.metadata = metadata
        self.created_time = created_time
        self.last_updated_time = last_updated_time

        self.id = str(uuid.uuid4())

    @classmethod
    def from_db_row(cls, cognite_client, row):
        instance = cls(
            cognite_client,
            external_id=row.columns.get("externalId", None),
            name=row.columns.get("name", None),
            description=row.columns.get("description", None),
            created_time=row.columns["createdTime"],
            last_updated_time=row.columns["lastUpdatedTime"],
            metadata=json.loads(row.columns.get("metadata", "{}")),
        )
        instance.id = row.key
        instance.resources = json.loads(row.columns["resources"])

        return instance

    def __repr__(self):
        return "<DataKit>: " + json.dumps(self.resources)

    def add_resource(self, resource):
        """Add a resource to the Data Kit

        Parameters
        ----------
        resource : CogniteResource, CogniteFilter, List[CogniteResource]
            The resource to add to the data kit

        Returns
        -------
        DataKit
            The data kit with the added resource

        Raises
        ------
        NotImplementedError
            Resource type not implemented yet
        """
        filters = None
        resource_ids = None
        if isinstance(resource, Asset):
            resource_type = "assets"
            resource_ids = [resource.id]
        elif isinstance(resource, AssetFilter):
            resource_type = "assets"
            filters = resource.dump()
        elif isinstance(resource, AssetList):
            resource_type = "assets"
            resource_ids = [r.id for r in resource]
        elif isinstance(resource, TimeSeries):
            resource_type = "time_series"
            resource_ids = [resource.id]
        elif isinstance(resource, TimeSeriesFilter):
            resource_type = "time_series"
            filters = resource.dump()
        elif isinstance(resource, TimeSeriesList):
            resource_type = "time_series"
            resource_ids = [r.id for r in resource]
        else:
            raise NotImplementedError("Resource type not implemented yet")

        if filters:
            self.resources[resource_type]["filters"] += [filters]
        if resource_ids:
            self.resources[resource_type]["ids"] += resource_ids
            # dedupe
            self.resources[resource_type]["ids"] = list(set(self.resources[resource_type]["ids"]))

        return self

    def get_resource(self, resource_type):
        """Get the resource from CDF

        Parameters
        ----------
        resource_type : str, one of ['assets', 'time_series', 'files', 'events']
            What resource to fetch.

        Returns
        -------
        List[CogniteResource]
            The list of resources of this resource type contained in the data kit
        """
        resource_down = []

        assert resource_type in RESOURCE_TYPE_APIS, f"{resource_type} is not a valid resource"
        resource_api = self.client.__dict__[resource_type]
        resource = self.resources[resource_type]
        if len(resource["ids"]) > 0:
            resource_down += resource_api.retrieve_multiple(ids=list(set(resource["ids"])))  # dedupe

        for filt in resource["filters"]:
            resource_down += resource_api.search(filter=filt)

        # Dedupe
        ids = set()
        result = []
        for r in resource_down:
            if r.id not in ids:
                result += [r]
                ids.add(r.id)

        return result

    def remove_resource(self, resource_type):
        """Remove resource from data kit. This removes all ids and filters
        associated with the resource type.

        Parameters
        ----------
        resource_type : str
            the resource type to remove

        Returns
        -------
        DataKit
            The data kit with the removed resource
        """
        assert resource_type in RESOURCE_TYPE_APIS, f"{resource_type} is not a valid resource"

        self.resources[resource_type] = {"filters": [], "ids": []}

        return self
