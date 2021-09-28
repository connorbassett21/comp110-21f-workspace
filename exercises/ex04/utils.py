"""List utility functions."""

__author__ = "730397999"

# TODO: Implement your functions here.


def all(value: int, list_of_values: list[int]) -> bool:
    """Prints yes if the input value is in the list; no if not."""
    i: int = 0
    while i < len(list_of_values):
        if value == list_of_values[i]:
            i += 1
        else:
            return False
    return True


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Prints yes if the two lists are equal; no if not."""
    i: int = 0
    if len(first_list) == len(second_list):
        while i < len(first_list) and len(second_list):
            if first_list[i] == second_list[i]:
                i += 1
            else:
                return False
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Identifies, and prints, the largest integer of a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 1
        maximum: int = input[0]
        while i < len(input):
            if input[i] > maximum:
                maximum = input[i]
                i += 1
            else:
                i += 1
        return maximum


print(max([88, 9, 3]))