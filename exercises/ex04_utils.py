"""EX04 - List Utility Functions."""


__author__ = "730483243"


def all(list_input: list[int], integer: int) -> bool:
    """Says whether all the integers in the list are the same as the given int."""
    i: int = 0
    while i < len(list_input) and integer == list_input[i]:
        i += 1
        if i == len(list_input):
            return True
    return False


def max(list_input: list[int]) -> int:
    """Returns the largest integer in a list."""
    if len(list_input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    alt_i: int = 0
    while i < len(list_input):
        while alt_i < len(list_input) and list_input[i] >= list_input[alt_i]:
            if alt_i == (len(list_input) - 1):
                return list_input[i]
            alt_i += 1
        i += 1
    return list_input[i]


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Determines if every element at every index is equal."""
    i: int = 0
    while len(first_list) == len(second_list): 
        while i < len(first_list):
            if first_list[i] == second_list[i]:
                i += 1
            else:
                return False
        return True
    return False