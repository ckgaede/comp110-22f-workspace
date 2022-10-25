"""Exercise 07 - Dictionaries."""

__author__ = 730483243


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts dictionary values."""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result:
            raise KeyError("There is a KeyError!")
        result[a[key]] = key
    return result


def favorite_color(a: dict[str, str]) -> str:
    """Returns most popular favorite color from a group of names."""
    colors: list[str] = []
    frequency: int = 0
    favorite: str = ""
    for key in a:
        colors.append(a[key])
    color_counts: dict[str, int] = count(colors)
    for key in color_counts:
        if color_counts[key] > frequency:
            frequency = color_counts[key]
            favorite = key
    return favorite


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a string appears in a list."""
    frequencies: dict[str, int] = {}
    for item in a:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies