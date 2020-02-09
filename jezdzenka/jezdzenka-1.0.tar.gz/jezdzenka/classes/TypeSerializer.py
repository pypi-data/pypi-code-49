from jezdzenka.classes.Type import Type
from tinydb_serialization import Serializer


class TypeSerializer(Serializer):
    OBJ_CLASS = Type  # The class this serializer handles

    def encode(self, obj):
        return obj.name

    def decode(self, s):
        return Type[s]
