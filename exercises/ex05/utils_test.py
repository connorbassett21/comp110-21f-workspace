"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730397999"


def test_only_evens_positive() -> None:
    """Tests to make sure single and double digit positive, even integers are returned."""
    assert only_evens([1, 2, 4, 3, 5, 10, 8]) == [2, 4, 10, 8]


def test_only_evens_negative() -> None:
    """Tests to make sure single and double digit negative, even integers are returned."""
    assert only_evens([0, -2, -8, -3, -17, -2]) == [0, -2, -8, -2]


def test_only_evens_empty_list() -> None:
    """Tests to make sure an empty list returns an empty list."""
    assert only_evens([]) == []


def test_sub_normal() -> None:
    """Tests to see if the function works when both integers are within the index range."""
    assert sub([5, 7, 2, 10, 3], 1, 4) == [7, 2, 10]


def test_sub_repeat() -> None:
    """Tests to see if the function works when all list values are 4."""
    assert sub([4, 4, 4, 4, 4, 4], 1, 3) == [4, 4]


def test_sub_out_of_range() -> None:
    """Tests to see if the function works when first integer is less than zero and second integer is greater than last index."""
    assert sub([3, 4, 6, 7, 9, 3], -7, 15) == [3, 4, 6, 7, 9]


def test_concat_positive() -> None:
    """Tests to see if the function works when both lists have positive integers."""
    assert concat([3, 4, 6, 7, 9, 3], [4, 3, 2, 9, 10]) == [3, 4, 6, 7, 9, 3, 4, 3, 2, 9, 10]


def test_concat_negative() -> None:
    """Tests to see if the function works when both lists have negative integers."""
    assert concat([-3, -4, -6, -7, -9, -3], [-4, -3, -2, -9, -10]) == [-3, -4, -6, -7, -9, -3, -4, -3, -2, -9, -10]


def test_concat_empty() -> None:
    """Tests to see if the function works when both lists are empty."""
    assert concat([], []) == []
