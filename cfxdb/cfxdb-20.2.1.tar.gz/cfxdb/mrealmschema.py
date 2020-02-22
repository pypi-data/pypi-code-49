###############################################################################
#
# Crossbar.io Fabric Center
# Copyright (c) Crossbar.io Technologies GmbH. All rights reserved.
#
###############################################################################

from zlmdb import table
from zlmdb import MapStringUuid, MapUuidCbor, MapSlotUuidUuid, MapUuidStringUuid, MapUuidUuidUuid, MapUuidUuidCbor

from cfxdb.mrealm import WebCluster, WebService, WebClusterNodeMembership, parse_webservice
from cfxdb.log import MNodeLogs, MWorkerLogs

__all__ = ('MrealmSchema', )


#
# Web clusters
#
@table('719d029f-e9d5-4b25-98e0-cf04d5a2648b', marshal=WebCluster.marshal, parse=WebCluster.parse)
class WebClusters(MapUuidCbor):
    """
    Table: webcluster_oid -> webcluster
    """


@table('296c7d17-4769-4e40-8cb7-e6c394b93335')
class IndexWebClusterByName(MapStringUuid):
    """
    Index: webcluster_name -> webcluster_oid
    """


#
# Web cluster node memberships
#
@table('e9801077-a629-470b-a4c9-4292a1f00d43',
       marshal=WebClusterNodeMembership.marshal,
       parse=WebClusterNodeMembership.parse)
class WebClusterNodeMemberships(MapUuidUuidCbor):
    """
    Table: (webcluster_oid, node_oid) -> webcluster_node_membership
    """


#
# Web cluster services
#
@table('a8803ca3-09a0-4d72-8728-2469de8d50ac', marshal=WebService.marshal, parse=parse_webservice)
class WebServices(MapUuidCbor):
    """
    Table: webservice_oid -> webservice
    """


@table('d23d4dbb-5d5c-4ccc-b72a-0ff18363169f')
class IndexWebClusterWebServices(MapUuidUuidUuid):
    """
    Index: (webcluster_oid, webservice_oid) -> webservice_oid
    """


@table('f0b05bcf-f682-49bb-929e-ac252e9867fa')
class IndexWebServiceByPath(MapUuidStringUuid):
    """
    Index: (webcluster_oid, webservice_name) -> webservice_oid
    """


@table('62d0841c-602e-473e-a6d5-3d8ce01e9e06')
class IndexWebClusterPathToWebService(MapUuidStringUuid):
    """
    Index: (webcluster_oid, path) -> webservice_oid
    """


#
# Docs metadata
#
@table('e11680d5-e20c-40b1-97d9-380b5ace1cb3', marshal=(lambda x: x), parse=(lambda x: x))
class Docs(MapUuidCbor):
    """
    Table: doc_oid -> doc
    """


@table('d1de0b8c-3b6d-488b-8778-5bac8528ab4b')
class IndexObjectToDoc(MapSlotUuidUuid):
    """
    Index: (object_slot, object_oid) -> doc_oid
    """


class MrealmSchema(object):
    """
    Management realm database schema.
    """
    def __init__(self, db):
        self.db = db

    # webclusters: WebClusters
    webclusters = None
    """
    """

    # idx_webclusters_by_name: IndexWebClusterByName
    idx_webclusters_by_name = None
    """
    """

    # webcluster_node_memberships: WebClusterNodeMemberships
    webcluster_node_memberships = None
    """
    """

    # webservices: WebServices
    webservices = None
    """
    """

    # idx_webservices_by_path: IndexWebServiceByPath
    idx_webservices_by_path = None
    """
    """

    # idx_webcluster_path_to_service: IndexWebClusterPathToWebService
    idx_webcluster_path_to_service = None
    """
    """

    # idx_node_to_webclusters: IndexNodeToWebClusters
    idx_node_to_webclusters = None
    """
    """

    # idx_webcluster_to_nodes: IndexWebClusterToNodes
    idx_webcluster_to_nodes = None
    """
    """

    # docs: Docs
    docs = None
    """
    """

    # idx_object_to_doc: IndexObjectToDoc
    idx_object_to_doc = None
    """
    """

    # mnode_logs: MNodeLogs
    mnode_logs = None
    """
    Managed node log records.
    """

    # mworker_logs: MWorkerLogs
    mworker_logs = None
    """
    Managed node worker log records.
    """

    @staticmethod
    def attach(db):
        """
        Factory to create a schema from attaching to a database. The schema tables
        will be automatically mapped as persistant maps and attached to the
        database slots.

        :param db: zlmdb.Database
        :return: object of Schema
        """
        schema = MrealmSchema(db)

        # web clusters
        schema.webclusters = db.attach_table(WebClusters)

        schema.idx_webclusters_by_name = db.attach_table(IndexWebClusterByName)
        schema.webclusters.attach_index('idx1', schema.idx_webclusters_by_name,
                                        lambda webcluster: webcluster.name)

        schema.webcluster_node_memberships = db.attach_table(WebClusterNodeMemberships)

        # web services
        schema.webservices = db.attach_table(WebServices)

        schema.idx_webservices_by_path = db.attach_table(IndexWebServiceByPath)
        schema.webservices.attach_index('idx1', schema.idx_webservices_by_path, lambda webservice:
                                        (webservice.webcluster_oid, webservice.path))

        schema.idx_webcluster_webservices = db.attach_table(IndexWebClusterWebServices)
        schema.webservices.attach_index('idx2', schema.idx_webcluster_webservices, lambda webservice:
                                        (webservice.webcluster_oid, webservice.oid))

        schema.mnode_logs = db.attach_table(MNodeLogs)
        schema.mworker_logs = db.attach_table(MWorkerLogs)

        return schema
