from collections.abc import MutableMapping, Callable
from koala_crawler.crawlers.graph_objects.graph_object_base import GraphObjectBase
from koala_crawler.exceptions.crawler_exceptions import InvalidGraphObject


class GraphNode(GraphObjectBase):

    def __init__(self, node, node_type, required_fields, id_creator):
        super().__init__(obj=node, required_fields=required_fields)
        self._node = node
        self._node["id"] = self._create_node_id(id_creator)
        self._node["type"] = node_type

    def as_json(self) -> MutableMapping:
        """ Returns the Graph node as mapping object

        :return: dict: Graph node object including unique identifier
        """
        return {"prop": self._node}

    def _create_node_id(self, id_creator: Callable) -> str:
        try:
            node_id = id_creator(self._node)
        except KeyError as missing_key:
            raise InvalidGraphObject(self.__class__.__name__, self._required_fields, missing_key)
        else:
            return node_id
