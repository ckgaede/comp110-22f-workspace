"""Exercise 05 using list utility functions."""

__author__ = "7304843243"


def only_evens(a: list[int]) -> list[int]:
    """Returns new list with only even numbers."""
    i: int = 0
    b: list() = []
    while i <= (len(a) - 1):
        if a[i] % 2 == 0:
            b.append(a[i])
        i += 1
    return b


def concat(a: list[int], b: list[int]) -> list[int]:
    """Joins two lists together and lists all their entries in order."""
    idx_a: int = 0
    idx_b: int = 0
    c: list() = []
    while idx_a <= (len(a) - 1):
        c.append(a[idx_a])
        idx_a += 1
    while idx_b <= (len(b) - 1):
        c.append(b[idx_b])
        idx_b += 1
    return c


def sub(a: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Makes a subset starting at start_idx and ending at end_idx - 1."""
    b: list() = []
    if start_idx < 0:
        start_idx = 0
    if end_idx > (len(a) - 1):
        end_idx = len(a)
    if len(a) == 0 or start_idx > (len(a) - 1) or end_idx <= 0:
        return b
    while start_idx < end_idx:
        b.append(a[start_idx])
        start_idx += 1
    return b


    