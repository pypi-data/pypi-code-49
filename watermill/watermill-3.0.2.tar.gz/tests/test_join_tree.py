from copy import deepcopy
from dataclasses import dataclass

from watermill.expressions import get_field
from watermill.stream_join import get_tree_pairs
from watermill.stream_join import join_streams
from watermill.stream_join import JoinTree
from watermill.stream_join import JoinTreeNode
from watermill.stream_join import JoinTreePair
from watermill.stream_join import JoinWith


@dataclass
class Foo:
    pass


@dataclass
class Bar:
    pass


@dataclass
class Baz:
    pass


def test_build_simple_join():
    left_expression = get_field('field')
    right_expression = get_field('field')
    join = join_streams(
        Foo,
        JoinWith(
            with_type=Bar,
            left_expression=left_expression,
            right_expression=right_expression,
        ),
    )
    assert isinstance(join, JoinTree)
    assert join.root_node == JoinTreeNode(user_type=Foo)
    assert get_tree_pairs(join, join.root_node) == [JoinTreePair(
        left_node=JoinTreeNode(user_type=Foo),
        right_node=JoinTreeNode(user_type=Bar),
        left_expression=left_expression,
        right_expression=right_expression,
    )]


def test_build_multi_join():
    left_expression = get_field('field')
    right_expression = get_field('field')

    second_left_expression = get_field('field')
    second_right_expression = get_field('field')

    join = join_streams(
        Foo,
        JoinWith(
            with_type=Bar,
            left_expression=left_expression,
            right_expression=right_expression,
        ),
        JoinWith(
            with_type=Baz,
            left_expression=second_left_expression,
            right_expression=second_right_expression,
        )
    )

    assert isinstance(join, JoinTree)
    assert join.root_node == JoinTreeNode(user_type=Foo)
    assert get_tree_pairs(join, join.root_node) == [JoinTreePair(
        left_node=JoinTreeNode(user_type=Foo),
        right_node=JoinTreeNode(user_type=Bar),
        left_expression=left_expression,
        right_expression=right_expression,
    ), JoinTreePair(
        left_node=JoinTreeNode(user_type=Foo),
        right_node=JoinTreeNode(user_type=Baz),
        left_expression=second_left_expression,
        right_expression=second_right_expression,
    )]


def test_build_chained_join():
    left_expression = get_field('field')
    right_expression = get_field('field')

    second_left_expression = get_field('field')
    second_right_expression = get_field('field')

    nested_join = join_streams(
        Bar,
        JoinWith(
            with_type=Baz,
            left_expression=second_left_expression,
            right_expression=second_right_expression,
        )
    )

    join = join_streams(
        Foo,
        JoinWith(
            with_type=nested_join,
            left_expression=left_expression,
            right_expression=right_expression,
        ),
    )

    assert isinstance(join, JoinTree)
    assert join.root_node == JoinTreeNode(user_type=Foo)
    assert get_tree_pairs(join, join.root_node) == [JoinTreePair(
        left_node=JoinTreeNode(user_type=Foo),
        right_node=JoinTreeNode(user_type=Bar),
        left_expression=left_expression,
        right_expression=right_expression,
    )]
    assert get_tree_pairs(join, JoinTreeNode(user_type=Bar)) == [JoinTreePair(
        left_node=JoinTreeNode(user_type=Bar),
        right_node=JoinTreeNode(user_type=Baz),
        left_expression=second_left_expression,
        right_expression=second_right_expression,
    )]

    def test_build_multi_chained_join():
        #
        #        Baz
        #       /
        #     Bar
        #    /   \ Quux
        # Foo
        #    \
        #     Qwe
        #      \
        #       Asd

        Quux, Qwe, Asd = (deepcopy(cls) for cls in [Bar] * 3)
        e = get_field('field')

        bbq_join = join_streams(
            Bar,
            JoinWith(
                with_type=Baz,
                left_expression=e,
                right_expression=e
            ),
            JoinWith(
                with_type=Quux,
                left_expression=e,
                right_expression=e
            )
        )

        qa_join = join_streams(
            Qwe,
            JoinWith(
                with_type=Asd,
                left_expression=e,
                right_expression=e
            )
        )

        join = join_streams(
            Foo,
            JoinWith(
                with_type=bbq_join,
                left_expression=e,
                right_expression=e
            ),
            JoinWith(
                with_type=qa_join,
                left_expression=e,
                right_expression=e
            )
        )

        assert join.root_node == JoinTreeNode(user_type=Foo)
        assert get_tree_pairs(join, join.root_node) == [JoinTreePair(
            left_node=JoinTreeNode(user_type=Foo),
            right_node=JoinTreeNode(user_type=Bar),
            left_expression=e,
            right_expression=e,
        ), JoinTreePair(
            left_node=JoinTreeNode(user_type=Foo),
            right_node=JoinTreeNode(user_type=Qwe),
            left_expression=e,
            right_expression=e,
        )]

        assert get_tree_pairs(join, JoinTreeNode(user_type=Bar)) == [JoinTreePair(
            left_node=JoinTreeNode(user_type=Bar),
            right_node=JoinTreeNode(user_type=Baz),
            left_expression=e,
            right_expression=e,
        ), JoinTreePair(
            left_node=JoinTreeNode(user_type=Bar),
            right_node=JoinTreeNode(user_type=Quux),
            left_expression=e,
            right_expression=e,
        )]

        assert get_tree_pairs(join, JoinTreeNode(user_type=Qwe)) == [JoinTreePair(
            left_node=JoinTreeNode(user_type=Qwe),
            right_node=JoinTreeNode(user_type=Asd),
            left_expression=e,
            right_expression=e,
        )]
