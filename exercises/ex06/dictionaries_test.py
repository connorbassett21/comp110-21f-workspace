"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730397999"


def test_invert_three_keys() -> None:
    """Tests to see if the function can invert a dictionary with three keys."""
    assert invert({"hello": "howdy", "yo": "greetings", "hey": "pal"}) == {"howdy": "hello", "greetings": "yo", "pal": "hey"}


def test_invert_nothing() -> None:
    """Tests to see that an empty dictionary returns an empty dictionary."""
    assert invert({}) == {}


def test_invert_duplicate_keys() -> None:
    """Tests to see that the function can invert a dictionary with one key."""
    assert invert({"big": "mike"}) == {"mike": "big"}


def test_favorite_color_basic() -> None:
    """Tests to see if the most common color is returned."""
    assert favorite_color({"Tim": "Blue", "Connor": "Purple", "Bob": "Blue"}) == "Blue"


def test_favorite_color_first() -> None:
    """Tests to see if the first one os returned if there are the same number of duplicates."""
    assert favorite_color({"Tim": "Blue", "Connor": "Purple", "Bob": "Blue", "Rico": "Pruple"}) == "Blue"


def test_favorite_color_capital() -> None:
    """Tests to see if capitalization affects the function."""
    assert favorite_color({"Tim": "blue", "Connor": "Purple", "Bob": "Blue", "Richard": "Purple"}) == "Purple"


def test_count_simple() -> None:
    """Tests to see is a dictionary is created with the number of times a key appears."""
    assert count(["blue", "wild", "wild", "haha"]) == {"blue": 1, "wild": 2, "haha": 1}


def test_count_empty() -> None:
    """Tests to see if an empty list returns an empty dictionary."""
    assert count([]) == {}


def test_count_capitals() -> None:
    """Tests to ensure the function is case sensitive."""
    assert count(["blue", "wild", "Wild", "haha"]) == {"blue": 1, "wild": 1, "Wild": 1, "haha": 1}