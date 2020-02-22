from blacken_selection import dedent_lines
from blacken_selection import indent_lines
from blacken_selection import nr_of_space_prefix


def test_nr_of_space_prefix():
    assert nr_of_space_prefix("") == 0
    assert nr_of_space_prefix("a") == 0
    assert nr_of_space_prefix(" ") == 1
    assert nr_of_space_prefix(" a") == 1
    assert nr_of_space_prefix("  ") == 2
    assert nr_of_space_prefix("  a") == 2
    assert nr_of_space_prefix("  a ") == 2


def test_dedent_lines():
    assert dedent_lines([], 10) == []
    assert dedent_lines([""], 0) == [""]
    assert dedent_lines([" a"], 0) == [" a"]
    assert dedent_lines([" a"], 1) == ["a"]
    assert dedent_lines([" a", "bb", "ccc"], 1) == ["a", "b", "cc"]


def test_indent_lines():
    assert indent_lines([], 10) == []
    assert indent_lines(["a"], 1) == [" a"]
    assert indent_lines(["a", "  b", " c d"], 1) == [" a", "   b", "  c d"]

    assert indent_lines([""], 1) == [""]
