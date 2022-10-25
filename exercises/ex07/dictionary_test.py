"""EX07 - Unit Tests for Dictionaries."""

__author__ = 730483243


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Edge - Inverts an empty dictionary."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_three_letters() -> None:
    """Use - Inverts a dictionary with three entries."""
    a: dict[str, str] = {"A": "B", "C": "D", "E": "F"}
    assert invert(a) == {"B": "A", "D": "C", "F": "E"}


def test_invert_numbers() -> None:
    """Use - Inverts dictionary of numbers to simulate squares/roots relationships."""
    a: dict[str, str] = {"1": "1", "2": "4", "3": "9"}
    assert invert(a) == {"1": "1", "4": "2", "9": "3"}


def test_favorite_color_none() -> None:
    """Edge - There is no favorite because all colors have the same frequency."""
    a: dict[str, str] = {"Audrey": "red", "Caroline": "blue", "AJ": "green", "Jonesy": "yellow"}
    assert favorite_color(a) == "red"


def test_favorite_color_highest() -> None:
    """Use - Returns the name of the most frequent favorite color."""
    a: dict[str, str] = {"Audrey": "red", "Caroline": "red", "AJ": "green", "Jonesy": "yellow"}
    assert favorite_color(a) == "red"


def test_favorite_color_tied() -> None:
    """Use - When there's a tie for favorite, it returns the first one in the list."""
    a: dict[str, str] = {"Audrey": "red", "Caroline": "red", "AJ": "green", "Jonesy": "green"}
    assert favorite_color(a) == "red"


def test_count_empty() -> None:
    """Edge - Takes frequencies of entries in an empty list."""
    a: list[str] = []
    assert count(a) == {}


def test_count_one_repeated() -> None:
    """Use - Takes frequencies of a list where only one of the entries is repeated."""
    a: list[str] = ["A", "B", "C", "A", "D", "E", "F", "A"]
    assert count(a) == {"A": 3, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1}


def test_count_multiple_repeated() -> None:
    """Use - Takes frequencies of a list where multiple values are repeated."""
    a: list[str] = ["A", "B", "C", "A", "B", "C", "A", "C"]
    assert count(a) == {"A": 3, "B": 2, "C": 3}