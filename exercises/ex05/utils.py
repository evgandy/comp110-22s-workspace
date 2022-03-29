"""Writing 'list' utility functions for Unit Testing."""

__author__ = "730227972"


def only_evens(list_int: list[int]) -> list[int]:
    """Returning the even numbers in a list of numbers.""" 
    i: int = 0 
    result_list: list[int] = list()
    while i < len(list_int):
        if list_int[i] % 2 == 0: 
            result_list.append(list_int[i]) 
        i += 1
    return result_list 


def sub(list_sub: list[int], index_1: int, index_2: int) -> list[int]:
    """Returning a subset of a list based on given indices."""
    result_sub: list[int] = list()
    if index_1 < 0:
        index_1 = 0
    if index_2 > len(list_sub):
        index_2 = len(list_sub)
    if len(list_sub) == 0 or index_2 <= 0 or index_1 > len(list_sub):
        return result_sub
    while index_1 < index_2:
        result_sub.append(list_sub[index_1])
        index_1 += 1
    return result_sub


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combining two smaller lists into one big list."""
    final_list: list[int] = list(list_1) 
    for i in list_2:
        final_list.append(i)
    return final_list 