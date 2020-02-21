"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import math
import traceback
from itertools import chain, tee
from typing import List, Optional, cast, Iterable, Iterator, Tuple
from urllib.parse import urlparse

import arrow
import attr
import deprecation
import pydash
from cortex.client import Client as CortexClient
from cortex.utils import decode_JWT, get_logger
from pymongo import MongoClient

from cortex_common.types import EntityEvent, ProfileAttributeType, ProfileSchema, ProfileAttributeSchema, \
    ProfileTagSchema, ProfileFacetSchema, ProfileTaxonomySchema
from cortex_common.types import ObservedProfileAttribute
from cortex_common.utils import chunk_iterable, timeit_safely
from cortex_profiles.build.attributes.utils.etl_utils import turn_attribute_into_entity_event, \
    turn_entity_event_into_attribute
from cortex_profiles.ext import clients
from cortex_profiles.ext.rest import ProfilesRestClient

log = get_logger(__name__)

__all__ = [
    "ProfilesBuilder",
    "BulkProfilesBuilder",
    "ProfileSchemaBuilder",
]


class BulkProfilesBuilder(object):

    def __init__(self, cortex_client: CortexClient, db_uri:Optional[str]=None, schemaId:Optional[str]=None):
        """
        - [ ] Todo ... add param of schemaId:Optional[str] to enable validation against schema before saving events
        :param cortex_client:
        :param db_uri:
        """

        # Database Stuff (explicitly referencing mongo for now ... will eventually decouple)
        self._db_uri = db_uri
        self._mongo_client: MongoClient = MongoClient(db_uri)
        self._mongo_db = urlparse(db_uri).path[1:]
        # Refreshing the client to ensure that there is a valid jwt token!
        self._profiles_client: ProfilesRestClient = (
            ProfilesRestClient.from_cortex_client(cortex_client).refresh_client()
        )
        # Initializing Builder State ...
        self._events: List[Iterator[EntityEvent]] = []
        self._attributes: List[Iterator[ProfileAttributeType]] = []

    def _extract_tenantId(self):
        return decode_JWT(
            self._profiles_client._serviceconnector.token, verify=False
        ).get("tenant")

    def _get_collection(self, collection):
        return self._mongo_client[self._mongo_db][collection]

    # def default_db_uri(self) -> str:
    #     """
    #     # The URI configured ... may be the cluster specific URI ...
    #     # The URI users connect to ... may be different ... maybe I shouldn't provide a default for now ... since this
    #     # will only work if the db is externalized ...
    #     # Also different tenants all use the same db ...
    #     :return:
    #     """
    #     config = self._profiles_client._get("graph/_/config").json()
    #     return base64decode_string(config.get(base64encode_string('mongo.graphUri'), ''))

    def ee_overrides(self, tenantId):
        return {
            "_environmentId": "cortex/default",
            "_tenantId": tenantId,
        }

    def attr_overrides(self, tenantId, version):
        return {
            "tenantId" : tenantId,
            "seq": version,
            "environmentId" : "cortex/default",
            "createdAt" : arrow.utcnow().datetime,
        }

    def with_events(self, event_chunk: Iterable[EntityEvent], **ee_to_attr_convertor_kwargs):
        """
        Appends the provided events to the list of events that will be used to build profiles.

        At this level ... we need to know what the attribute type is {inferred, observed, ...}
            ... currently the graph service assumes that entity events lead to observed attributes ...
        :param event_chunk:
        :return:
        """
        event_chunk_for_events, event_chunk_for_attrs = tee(event_chunk)
        # Add chunk of raw events to save ...
        self._events.append(event_chunk_for_events)
        # Add chunk of attributes to save ...
        self.with_attributes(
            turn_entity_event_into_attribute(
                e,
                **pydash.defaults(
                    ee_to_attr_convertor_kwargs,
                    {
                        "attributeType": ObservedProfileAttribute
                    }
                )
            )
            for e in event_chunk_for_attrs
        )
        return self

    def with_attributes(self, attribute_chunk:Iterable[ProfileAttributeType]):
        """
        Converts the provided attributes into a list of events and appends them to the list of events that will be
        used to build profiles.
        :param events:
        :return:
        """
        self._attributes.append(attribute_chunk)
        return self

    # def _database_connection(self):
    #
    # def _save_in_bulk(self, documents, collection):
    #     return documents.insert_many

    # Update all seqs ... to be now ...
    # Update all createdAt times ... incrementally as chunks are inserted ... ?

    def _format_chunk_response(self, items_in_chunk, chunk_index,
                               chunk_insert_duration, chunk_insert_response, chunk_insert_exception,
                               chunk_completion_time, verbose):
        response = {
            "chunk_number": chunk_index + 1,
            "total_items_in_chunk": len(items_in_chunk),
            "time_taken_to_insert_chunk": chunk_insert_duration,
            "insert_finished_at": str(chunk_completion_time),
            "exception_occurred": chunk_insert_exception is not None,
        }
        if verbose:
            if chunk_insert_exception is None:
                response["insert_response_inserted_ids"] = [str(y) for y in chunk_insert_response.inserted_ids]
                response["insert_response_acknowledged"] = chunk_insert_response.acknowledged
            # If an exception happened ... add traceback
            else:
                response["exception_traceback"] = traceback.log.info_exception(
                    *chunk_insert_exception
                )
                response["exception_type"] = chunk_insert_exception[0]
                response["exception_value"] = str(chunk_insert_exception[1])
        return response

    def build(self, verbose=False, chunk_size=10_000) -> Tuple[List,List]:
        """
        Saves attributes to profiles in bulk, one chunk at a time.
        (Optionally) Saves profile building events in bulk ...
        * It is the responsibility of the invoker to ensure that all chunks were properly inserted and retry as needed.
        * This method does not assert that all the chunks get saved fully;
            It does however return status of the bulk save for each chunk.
        * This method logs progress as chunks are incrementally saved ...

        For reference's sake ...:
        arrow.utcnow().datetime                  ==> datetime.datetime(2020, 2, 17, 16, 37, 25, 350303, tzinfo=tzutc())
        arrow.utcnow().datetime.timestamp()      ==> 1581957467.937602
        arrow.utcnow().datetime.timestamp()*1000 ==> 1581957467937.602
        :return: the resulting responses from the bulk output
        """
        tenantId = self._extract_tenantId()
        # The version of attributes is based on the time this method was invoked
        seq = math.floor(arrow.utcnow().datetime.timestamp() * 1000)

        # Interleave Attribute and Event Chunks so that the iterators tees dont get out of sync ...
        attribute_stream = chain(*self._attributes)
        event_stream = chain(*self._events)

        attribute_insert_responses = []
        processed_attributes_counter = 0
        attr_processing_time = 0

        event_insert_responses = []
        processed_event_counter = 0
        event_processing_time = 0

        (next_attr_chunk, next_event_chunk) = (
            next(enumerate(chunk_iterable(attribute_stream, chunk_size)), []),
            next(enumerate(chunk_iterable(event_stream, chunk_size)), []),
        )
        while next_attr_chunk or next_event_chunk:
            profile_ids_to_flush = set([])

            # Insert Each Chunk of attributes
            if next_attr_chunk:
                (attr_chunk_index, attr_chunk) = next_attr_chunk
                loaded_attrs_in_chunk = [
                    pydash.merge({}, dict(a), self.attr_overrides(tenantId, seq))
                    for a in attr_chunk
                ]
                (time, bulk_insert_response, bulk_insert_exception) = timeit_safely(precision=6)(
                    lambda: self._get_collection("attributes").insert_many(loaded_attrs_in_chunk, ordered=False)
                )()
                resp = self._format_chunk_response(
                    items_in_chunk=loaded_attrs_in_chunk, chunk_index=attr_chunk_index, chunk_insert_duration=time,
                    chunk_insert_response=bulk_insert_response, chunk_insert_exception=bulk_insert_exception,
                    chunk_completion_time=arrow.utcnow().datetime, verbose=verbose
                )
                processed_attributes_counter += resp['total_items_in_chunk']
                attr_processing_time += float(resp['time_taken_to_insert_chunk'])
                a, b, c, d = (
                    resp['total_items_in_chunk'], processed_attributes_counter,
                    resp['time_taken_to_insert_chunk'], attr_processing_time
                )
                log.info(
                    f"Inserted {a:,d} Attributes   in {c} seconds. {b:,d} so far in {d:2.4f} seconds"
                )
                attribute_insert_responses.append(resp)
                profile_ids_to_flush = profile_ids_to_flush.union([
                    pydash.get(attr, "profileId")
                    for attr in loaded_attrs_in_chunk
                ])

            # Insert Each Chunk of Events ...
            if next_event_chunk:
                (event_chunk_index, event_chunk) = next_event_chunk
                loaded_events_in_chunk = [
                    pydash.merge({}, dict(e), self.ee_overrides(tenantId))
                    for e in event_chunk
                ]
                (time, bulk_insert_response, bulk_insert_exception) = timeit_safely(precision=6)(
                    lambda: self._get_collection("entity-events").insert_many(loaded_events_in_chunk, ordered=False)
                )()
                resp = self._format_chunk_response(
                    items_in_chunk=loaded_events_in_chunk, chunk_index=event_chunk_index, chunk_insert_duration=time,
                    chunk_insert_response=bulk_insert_response, chunk_insert_exception=bulk_insert_exception,
                    chunk_completion_time=arrow.utcnow().datetime, verbose=verbose
                )
                processed_event_counter += resp['total_items_in_chunk']
                event_processing_time += float(resp['time_taken_to_insert_chunk'])
                a, b, c, d = (
                    resp['total_items_in_chunk'], processed_event_counter,
                    resp['time_taken_to_insert_chunk'], event_processing_time
                )
                log.info(
                    f"Inserted {a:,d} EntityEvents in {c} seconds. {b:,d} so far in {d:2.4f} seconds"
                )
                attribute_insert_responses.append(resp)
                profile_ids_to_flush = profile_ids_to_flush.union([
                    pydash.get(event, "entityId")
                    for event in loaded_events_in_chunk
                ])

            # Flush cache ...
            log.info(self._profiles_client.delete_cache_for_specific_profiles(list(profile_ids_to_flush)))

            (next_attr_chunk, next_event_chunk) = (
                next(enumerate(chunk_iterable(attribute_stream, chunk_size)), []) if next_attr_chunk else None,
                next(enumerate(chunk_iterable(event_stream, chunk_size)), []) if next_event_chunk else None,
            )

        return (seq, attribute_insert_responses, event_insert_responses)


class ProfilesBuilder(object):

    """
    A builder utility to aid in programmatic creation of Cortex Profiles.
    Not meant to be directly instantiated by users of the sdk.
    """

    def __init__(self, profiles_client:ProfilesRestClient, schemaId:Optional[str]=None):
        """
        - [ ] Todo ... add param of schemaId:Optional[str] to enable validation against schema before saving events
        :param profiles_client:
        :param schemaId:
        """
        self._schemaId = schemaId
        self._profiles_client = profiles_client
        self._events: List[EntityEvent] = []

    def with_events(self, events:List[EntityEvent]):
        """
        Appends the provided events to the list of events that will be used to build profiles.
        :param events:
        :return:
        """
        self._events.extend(events)
        return self

    @deprecation.deprecated(deprecated_in='6.0.1b1', details='Use with_events instead.')
    def with_attributes(self, attributes:List[ProfileAttributeType]):
        """
        Converts the provided attributes into a list of events and appends them to the list of events that will be
        used to build profiles.
        :param events:
        :return:
        """
        self._events.extend([
            turn_attribute_into_entity_event(a, defaultEntityType=self._schemaId)
            for a in attributes
        ])
        return self

    def build(self) -> List[str]:
        """
        Pushes profile building events and returns the response from the building process ...
        :return: the resulting Connection
        """
        # return Profile.get_profile(self._profileId, self._schemaId, self._profiles_client)
        return self._profiles_client.pushEvents(self._events)


class ProfileSchemaBuilder(object):

    """
    A builder utility to aid in programmatic creation of Schemas for Cortex Profiles.
    Not meant to be directly instantiated by users of the sdk.
    """

    def __init__(self, schema:ProfileSchema, profiles_client:ProfilesRestClient):
        """
        Initializes the builder from the profile schema type ...
        :param schema:
        :return:
        """
        self._schema = schema
        self._profiles_client = profiles_client

    def name(self, name:str) -> 'ProfileSchemaBuilder':
        """
        Sets the name of the schema ...
        :param name:
        :return:
        """
        self._schema = attr.evolve(self._schema, name=name)
        return self

    def title(self, title:str) -> 'ProfileSchemaBuilder':
        """
        Sets the title of the schema ...
        :param title:
        :return:
        """
        self._schema = attr.evolve(self._schema, title=title)
        return self

    def profileType(self, profileType:str) -> 'ProfileSchemaBuilder':
        """
        Sets the profileType of the schema ...
        :param profileType:
        :return:
        """
        self._schema = attr.evolve(self._schema, profileType=profileType)
        return self

    def description(self, description:str) -> 'ProfileSchemaBuilder':
        """
        Sets the description of the schema ...
        :param description:
        :return:
        """
        self._schema = attr.evolve(self._schema, description=description)
        return self

    def facets(self, facets:List[ProfileFacetSchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the facets of the schema ...
        :param facets:
        :return:
        """
        self._schema = attr.evolve(self._schema, facets=facets)
        return self

    def taxonomy(self, taxonomy:List[ProfileTaxonomySchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the taxonomy of the schema ...
        :param taxonomy:
        :return:
        """
        self._schema = attr.evolve(self._schema, taxonomy=taxonomy)
        return self

    def attributes(self, attributes:List[ProfileAttributeSchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the attributes of the schema ...
        :param attributes:
        :return:
        """
        self._schema = attr.evolve(self._schema, attributes=attributes)
        return self

    def attributeTags(self, attributeTags:List[ProfileTagSchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the attributeTags of the schema ...
        :param attributeTags:
        :return:
        """
        self._schema = attr.evolve(self._schema, attributeTags=attributeTags)
        return self

    def build(self) -> clients.ProfileSchema:
        """
        Builds and saves a new Profile Schema using the properties configured on the builder
        :return:
        """
        # Push Schema ...
        self._profiles_client.pushSchema(self._schema)
        # Get latest schema ...
        return clients.ProfileSchema.get_schema(
            cast(str, self._schema.name), self._profiles_client)


if __name__ == '__main__':
    pass
    # log.info(bulk_profile_builder.build(verbose=True))
    # Test to iteratively insert a million attributes!
    # Sum up all the times at the end!