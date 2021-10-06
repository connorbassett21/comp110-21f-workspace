"""List utility functions part 2."""

__author__ = "730397999"

# Define your functions below


def only_evens(list_of_ints: list[int]) -> list[int]:
    i: int = 0
    even_integers: list[int] = list([])
    while i < len(list_of_ints):
        if list_of_ints[i] % 2 == 0:
            even_integers.append(list_of_ints[i])
            i += 1
        else:
            i += 1
    return even_integers


def sub(a_list: list[int], first: int, second: int) -> list[int]:
    begin_number: int = first
    end_number: int = second
    final_list: list[int] = list([])
    if begin_number < 0:
        begin_number: int = 0
    if begin_number > len(a_list):
        return final_list
    if end_number < 0:
        return final_list
    if end_number > len(a_list):
        end_number: int = (len(a_list) - 1)
    if len(a_list) == 0:
        return final_list
    first_number: int = a_list[begin_number]
    second_number: int = a_list[end_number]
    final_list.append(first_number)
    final_list.append(second_number)
    return final_list


def concat(first: list[int], second: list[int]) -> list[int]:
    i: int = 0
    final_list: list[int] = list()
    while i < len(first):
        final_list.append(first[i])
        i += 1
    i: int = 0
    while i < len(second):
        final_list.append(second[i])
        i += 1
    return final_list