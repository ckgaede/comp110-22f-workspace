"""Exercise 05 using list utility functions - unit tests."""

__author__ = "7304843243"

from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Provides list of evens given an empty list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_only_evens_all_odd() -> None:
    """Provides empty list given list of all odds."""
    a: list[int] = [1, 3, 5, 7, 9, 11]
    assert only_evens(a) == []


def test_only_evens_mixed() -> None:
    """Provides full list given list of odds and evens mixed."""
    a: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(a) == [0, 2, 4, 6, 8]


def test_concat_both_empty() -> None:
    """Concatenates two empty lists."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_one_empty() -> None:
    """Concatenates a full list and an empty one."""
    a: list[int] = [1, 2, 3]
    b: list[int] = []
    assert concat(a, b) == [1, 2, 3]


def test_concat_both_full() -> None:
    """Concatenates two lists with multiple entries."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [4, 5, 6]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]


def test_sub_beyond_scope() -> None:
    """Start and end indices are outside the scope of the list."""
    a: list[int] = [2, 4, 6, 8, 10]
    start_idx: int = -5
    end_idx: int = 6
    assert sub(a, start_idx, end_idx) == [2, 4, 6, 8]


def test_sub_most() -> None:
    """Subset contains most values in original list."""
    a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_idx: int = 0
    end_idx: int = 8
    assert sub(a, start_idx, end_idx) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub_some() -> None:
    """Subset contains only a few values from original list."""
    a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_idx: int = 3
    end_idx: int = 5
    assert sub(a, start_idx, end_idx) == [4, 5]