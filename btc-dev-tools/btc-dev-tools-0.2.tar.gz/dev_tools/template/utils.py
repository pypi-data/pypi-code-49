

# region template render features

class Collector:
    """
    Collector class for constructing nested template structures.
    """

    block_str: str = None

    def __init__(self, *args, **kwargs):
        self.nodes = []

    def prepare_node(self, node: str) -> str:
        return str(node)

    def get_block_str(self) -> str:
        return self.block_str

    def get_all_nodes(self, nested_list: list) -> None:
        for node in nested_list:
            if isinstance(node, list):
                self.get_all_nodes(node)
            else:
                self.nodes.append(node)

    def get_all_nodes_from_dict(self, dict_for_parse: dict) -> list:
        for key, value in dict_for_parse.items():
            self.get_all_nodes(value)
        nodes = self.nodes[:]
        self.nodes = []
        return nodes

    def parse_nested_list(self, nested_list: list) -> str:
        """
        Recursive parse nested lists and wrap free or list's nodes in blocks.
        """

        order_list = []

        for node in nested_list:
            if isinstance(node, list):
                list_nodes_str = self.parse_nested_list(node)
                order_list.append((self.get_block_str() % list_nodes_str) if list_nodes_str else '')
            else:
                order_list.append(self.prepare_node(node))

        return ''.join(order_list)

# endregion
