import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from .models import Map as MapModel
from .models import Beam as BeamModel
from .models import MapFilePath as MapFilePathModel

##__________________________________________________________________||
class Map(SQLAlchemyObjectType):
    class Meta:
        model = MapModel
        interfaces = (relay.Node, )

class MapConnection(relay.Connection):
    class Meta:
        node = Map

##__________________________________________________________________||
class Beam(SQLAlchemyObjectType):
    class Meta:
        model = BeamModel
        interfaces = (relay.Node, )

# class BeamConnection(relay.Connection):
#      class Meta:
#          node = Beam

## The class "BeamConnection" is commented out because it causes the error
## "AssertionError: Found different types with the same name in the schema:
## BeamConnection, BeamConnection". In the class "Query" below
## "Beam._meta.connection" is used instead. This solution was mentioned in the
## issue
## https://github.com/graphql-python/graphene-sqlalchemy/issues/153#issuecomment-478744077

##__________________________________________________________________||
class MapFilePath(SQLAlchemyObjectType):
    class Meta:
        model = MapFilePathModel
        interfaces = (relay.Node, )

# class MapFilePathConnection(relay.Connection):
#     class Meta:
#         node = MapFilePath

##__________________________________________________________________||
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_maps = SQLAlchemyConnectionField(MapConnection)
    all_beams = SQLAlchemyConnectionField(Beam._meta.connection)
    all_map_file_paths = SQLAlchemyConnectionField(MapFilePath)

schema = graphene.Schema(query=Query, types=[Map, Beam, MapFilePath])

##__________________________________________________________________||
