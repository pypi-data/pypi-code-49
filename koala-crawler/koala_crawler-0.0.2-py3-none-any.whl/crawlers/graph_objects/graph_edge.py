from collections.abc import MutableMapping, Sequence
from koala_crawler.crawlers.graph_objects.graph_object_base import GraphObjectBase


class GraphEdge(GraphObjectBase):

    def __init__(self, edge: MutableMapping, required_fields: Sequence):
        super().__init__(obj=edge, required_fields=required_fields)
        self._edge = edge

    def as_json(self) -> MutableMapping:
        """ Returns the Graph edge object as mapping object

        :return: dict: Graph edge object including unique identifier
        """
        return self._edge
