import math

from watermill.expressions import Expression
from watermill.expressions import get_field


def test_get_field_expression():
    expr = get_field('field')
    assert isinstance(expr, Expression)

    result = expr({'field': 123})
    assert result == 123


def test_get_item_expression():
    expr = get_field('field')['sub']

    result = expr({
        'field': {
            'sub': 12.
        }
    })
    assert result == 12.


def test_add_expression():
    expr = get_field('field') + 15
    result = expr({'field': 2})
    assert result == 17



def test_div_expression():
    expr = get_field('field') // 3
    result = expr({'field': 15})
    assert result == 5


def test_sub_expression():
    expr = get_field('field') - 12.4
    result = expr({'field': 22.4})
    assert math.isclose(result, 10)


def test_mul_expression():
    expr = get_field('field') * 7
    result = expr({'field': 11})
    assert result == 77


def test_mod_expression():
    expr = get_field('field') % 3
    result = expr({'field': 16})
    assert result == 1


def test_multi_field_expressions():
    expr = get_field('left') % get_field('right') + 1
    result = expr({
        'left': 16,
        'right': 3
    })
    assert result == 2
