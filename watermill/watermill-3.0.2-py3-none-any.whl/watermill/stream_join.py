from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Callable
from typing import List
from typing import Mapping
from typing import Optional
from typing import Type
from typing import Union

from botox import Injector

from watermill.expressions import Expression
from watermill.message_brokers.message_broker import StreamsShift
from watermill.stream_types import JoinedStreamType
from watermill.stream_types import StreamType
from watermill.windows import Window


@dataclass
class JoinTreeNode:
    user_type: Type[StreamType]
    window_func: Optional[Callable] = None


@dataclass
class JoinTreePair:
    left_node: JoinTreeNode
    right_node: JoinTreeNode
    left_expression: Expression
    right_expression: Expression


@dataclass
class JoinTree:
    root_node: JoinTreeNode
    pairs: List[JoinTreePair] = field(default_factory=list)


@dataclass
class JoinWith:
    with_type: Union[Type[StreamType], JoinTree]
    left_expression: Expression
    right_expression: Expression


def join_streams(
        left_stream_type: Union[Type[StreamType], Window],
        *joins: JoinWith,
):
    assert joins
    if isinstance(left_stream_type, Window):
        root_node = JoinTreeNode(
            user_type=left_stream_type.cls,
            window_func=left_stream_type.window_func
        )
    else:
        root_node = JoinTreeNode(
            user_type=left_stream_type,
        )
    pairs = []
    for join_info in joins:
        if isinstance(join_info.with_type, JoinTree):
            right_tree = join_info.with_type
            right_type = right_tree.root_node.user_type
            pairs.extend(right_tree.pairs)
        else:
            right_type = join_info.with_type

        right_node = JoinTreeNode(
            user_type=right_type,
        )
        pairs.append(JoinTreePair(
            left_node=root_node,
            right_node=right_node,
            left_expression=join_info.left_expression,
            right_expression=join_info.right_expression,
        ))

    return JoinTree(
        root_node=root_node,
        pairs=pairs,
    )


def compare_streams(left: Any, right: Any) -> StreamsShift:
    if left < right:
        return StreamsShift.Less
    elif left == right:
        return StreamsShift.Equal
    return StreamsShift.Greater


def get_tree_pairs(join_tree: JoinTree, join_node: JoinTreeNode) -> List[JoinTreePair]:
    pairs = []
    for pair in join_tree.pairs:
        if pair.left_node == join_node:
            pairs.append(pair)

    return pairs


def get_join_data_mapping(
        processing_func_type_hints: Type[Callable],
        parent_children_map: Mapping[StreamType, List[JoinedStreamType]]
) -> List[Mapping[StreamType, List[JoinedStreamType]]]:
    data_mapping = []
    for arg_name in list(processing_func_type_hints.keys())[1:-1]:
        type_hint = processing_func_type_hints[arg_name]

        if not hasattr(type_hint, '__origin__'):
            break

        hint_type, join_types = type_hint.__reduce__()[1]
        if not issubclass(hint_type, Mapping):
            break

        left_type, right_type_alias = join_types
        right_type = right_type_alias.__reduce__()[1][1]

        result_items = {}

        for parent_item, children in parent_children_map.items():
            if isinstance(parent_item, left_type):
                for child in children:
                    if isinstance(child, right_type):
                        result_items.setdefault(parent_item, []).append(child)
        data_mapping.append(result_items)
    return data_mapping


def get_injected_kwargs(processing_func_type_hints, injector: Injector) -> Mapping[str, Any]:
    kwargs = {}
    for arg_name in list(processing_func_type_hints.keys())[1:-1]:
        type_hint = processing_func_type_hints[arg_name]
        if hasattr(type_hint, '__origin__'):
            continue

        kwargs[arg_name] = injector.deliver(type_hint, strict=True)

    return kwargs
