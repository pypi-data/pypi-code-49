###############################################################################
#
# Crossbar.io Fabric Center
# Copyright (c) Crossbar.io Technologies GmbH. All rights reserved.
#
###############################################################################

from zlmdb import table
from zlmdb import MapStringUuid, MapUuidCbor, MapUuidUuidCbor, MapUuidStringUuid,\
    MapTimestampUuidFlatBuffers

from cfxdb.mrealm import ManagementRealm, Node
from cfxdb.user import User, ActivationToken, UserMrealmRole, Organization
from cfxdb.usage import MasterNodeUsage

__all__ = ('GlobalSchema', )


@table('1219e71c-a62c-415a-bd15-ddf45e3a658b', marshal=ManagementRealm.marshal, parse=ManagementRealm.parse)
class ManagementRealms(MapUuidCbor):
    """
    Table: oid -> mrealm
    """


@table('1d2e8045-ea2b-4456-be4a-7a234d3622d6')
class IndexManagementRealmByName(MapStringUuid):
    """
    Index: pubkey -> oid
    """


@table('ae89d956-273a-4ce3-b63d-52b07ae35742', marshal=Node.marshal, parse=Node.parse)
class Nodes(MapUuidCbor):
    """
    Table: oid -> node
    """


@table('1336c623-5f38-4397-ad5b-2e6b716b57b0')
class IndexNodesByPubkey(MapStringUuid):
    """
    Index: pubkey -> node_oid
    """


@table('6d071a33-0577-4f72-a2e1-11182f60ab9c')
class IndexNodesByAuthid(MapUuidStringUuid):
    """
    Index: (mrealm_oid, authid) -> node_oid
    """


@table('fa1ed0fc-304e-4f66-8092-d901df1735e4', marshal=User.marshal, parse=User.parse)
class Users(MapUuidCbor):
    """
    CFC global users table.

    The table holds all CFC users registered in this CFC domain.
    """


@table('aa2754e5-a859-4986-8749-1299828dc6e1')
class IndexUsersByName(MapStringUuid):
    """
    Index (by name) on users table.
    """


@table('882a24e4-90cc-4823-94fe-c1d938daffe6')
class IndexUsersByPubkey(MapStringUuid):
    """
    Index on Users: by pubkey.
    """


@table('933447a3-dd79-4599-bd9a-e0d88d9b84cb')
class IndexUsersByEmail(MapStringUuid):
    """
    Index on Users: by email.
    """


@table('eccdfc57-5632-4ad4-9c2b-2ac11e9d389f', marshal=UserMrealmRole.marshal, parse=UserMrealmRole.parse)
class UserMrealmRoles(MapUuidUuidCbor):
    """
    """


@table('c968886e-a2e2-490c-bc2a-6b684c3130f6', marshal=ActivationToken.marshal, parse=ActivationToken.parse)
class ActivationTokens(MapUuidCbor):
    """
    CFC user activations.
    """


@table('0f6a9014-2e39-4cfd-9f2b-f6ffd3d3deca')
class IndexActivationTokensByAuthidPubkey(MapStringUuid):
    """
    """


@table('ae2fe53f-f8ec-4484-8a8f-cabdf1b38358', marshal=Organization.marshal, parse=Organization.parse)
class Organizations(MapUuidCbor):
    """
    CFC global organizations table.

    The table holds all CFC organizations defined in this CFC domain.
    """


@table('3fb82ab2-430d-43a1-8200-fcd6355d0410')
class IndexOrganizationsByName(MapStringUuid):
    """
    Index (by name) on organizations table.
    """


@table('e38f7bf1-2514-400c-8c30-a979b2138503', build=MasterNodeUsage.build, cast=MasterNodeUsage.cast)
class UsageRecords(MapTimestampUuidFlatBuffers):
    """
    Usage metering records.
    """


class GlobalSchema(object):
    """
    CFC database schema.
    """
    def __init__(self, db):
        self.db = db

    # nodes: Nodes
    nodes = None
    """
    Nodes.
    """

    # idx_nodes_by_pubkey: IndexNodesByPubkey
    idx_nodes_by_pubkey = None
    """
    Index on nodes: by pubkey
    """

    # idx_nodes_by_authid: IndexNodesByAuthid
    idx_nodes_by_authid = None
    """
    Index on nodes: by authid
    """

    # organizations = Organizations
    organizations = None
    """
    Organizations.
    """

    # idx_organizations_by_name = IndexOrganizationsByName
    idx_organizations_by_name = None
    """
    Index on organizations: by name
    """

    # users: Users
    users = None
    """
    Users.
    """

    # idx_users_by_pubkey: IndexUsersByPubkey
    idx_users_by_pubkey = None
    """
    Index on users: by pubkey
    """

    # idx_users_by_email: IndexUsersByEmail
    idx_users_by_email = None
    """
    Index on users: by email
    """

    # activation_tokens: ActivationTokens
    activation_tokens = None
    """
    User activation tokens.
    """

    # idx_act_tokens_by_authid_pubkey: IndexActivationTokensByAuthidPubkey
    idx_act_tokens_by_authid_pubkey = None
    """
    Index on user activation tokens: by authid+pubkey
    """

    # mrealms: ManagementRealms
    mrealms = None
    """
    Management realms.
    """

    # idx_mrealms_by_name: IndexManagementRealmByName
    idx_mrealms_by_name = None
    """
    Index on management realms: by name.
    """

    # users_mrealm_roles: UserMrealmRoles
    users_mrealm_roles = None
    """
    User roles map: mrealm_oid, user_oid => UserRoles
    """

    usage = None
    """
    Usage metering records: by timestamp
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
        schema = GlobalSchema(db)

        # Organizations
        #
        schema.organizations = db.attach_table(Organizations)

        schema.idx_organizations_by_name = db.attach_table(IndexOrganizationsByName)
        schema.organizations.attach_index('idx1', schema.idx_organizations_by_name, lambda org: org.name)

        # Users
        #
        schema.users = db.attach_table(Users)

        schema.idx_users_by_pubkey = db.attach_table(IndexUsersByPubkey)
        schema.users.attach_index('idx1', schema.idx_users_by_pubkey, lambda user: user.pubkey, nullable=True)

        schema.idx_users_by_email = db.attach_table(IndexUsersByEmail)
        schema.users.attach_index('idx2', schema.idx_users_by_email, lambda user: user.email, nullable=True)

        schema.activation_tokens = db.attach_table(ActivationTokens)

        schema.idx_act_tokens_by_authid_pubkey = db.attach_table(IndexActivationTokensByAuthidPubkey)
        schema.activation_tokens.attach_index('idx1', schema.idx_act_tokens_by_authid_pubkey,
                                              lambda token: token.email + token.pubkey)

        # Management Realms
        #
        schema.mrealms = db.attach_table(ManagementRealms)

        schema.idx_mrealms_by_name = db.attach_table(IndexManagementRealmByName)
        schema.mrealms.attach_index('idx1', schema.idx_mrealms_by_name, lambda mrealm: mrealm.name)

        schema.users_mrealm_roles = db.attach_table(UserMrealmRoles)

        # Nodes
        #
        schema.nodes = db.attach_table(Nodes)

        schema.idx_nodes_by_pubkey = db.attach_table(IndexNodesByPubkey)
        schema.nodes.attach_index('idx1', schema.idx_nodes_by_pubkey, lambda node: node.pubkey)

        schema.idx_nodes_by_authid = db.attach_table(IndexNodesByAuthid)
        schema.nodes.attach_index('idx2',
                                  schema.idx_nodes_by_authid,
                                  lambda node: (node.mrealm_oid, node.authid),
                                  nullable=True)

        # Usage metering
        #
        schema.usage = db.attach_table(UsageRecords)

        return schema
