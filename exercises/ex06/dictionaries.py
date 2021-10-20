"""Practice with dictionaries."""

__author__ = "730397999"

# Define your functions below


def invert(initial: dict[str, str]) -> dict[str, str]:
    """When given a dictionary, it inverts it."""
    inverted_list = {}
    for key in initial:
        inverted_list[initial[key]] = key
    if len(inverted_list) < len(initial):
        raise KeyError("You have the same key twice.")
    return inverted_list


def favorite_color(start: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    most_common: str = ""
    frequency: dict[str, int] = dict()
    for name in start:
        color = start[name]
        if color not in frequency:
            frequency[color] = 1
        else:
            frequency[color] += 1
    maximum: int = 0
    for color in frequency:
        if frequency[color] > maximum:
            maximum = frequency[color]
            most_common = color
    return most_common


def count(begin: list[str]) -> dict[str, int]:
    """Counts how many times a value appears in a value list."""
    frequency: dict[str, int] = dict()
    i: int = 0
    while i < len(begin):
        value = begin[i]
        if value not in frequency:
            frequency[value] = 1
        else:
            frequency[value] += 1
        i += 1
    return frequency