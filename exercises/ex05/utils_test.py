"""Unit Testing a Series of Utility Functions."""

__author__ = "730227972"


from utils import only_evens, sub, concat 


def test_first_item() -> None: 
    """Edge case that tests what the first number in the produced list is."""
    list_int: list[int] = [1, 2, 3, 4]
    assert only_evens(list_int)[0] == 2


def test_correct_items() -> None:
    """Use case that tests the function is selecting all of the even items."""
    list_int: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(list_int) == [2, 4, 6]


def test_no_evens() -> None:
    """Use case that tests the function will produce a blank list if there are no evens."""
    list_int: list[int] = [1, 3, 5, 7]
    assert only_evens(list_int) == [] 


def test_first_sub() -> None:
    """Edge case that tests what the first number in the produced list is."""
    list_sub: list[int] = [10, 20, 30, 40]
    assert sub(list_sub, 1, 3)[0] == 20


def test_in_range_indices() -> None:
    """Use case that tests the function can select the correct numbers within the indicated indices."""
    list_sub: list[int] = [10, 20, 30, 40]
    assert sub(list_sub, 1, 3) == [20, 30]


def test_out_range_indices() -> None: 
    """Use case that tests the function can provide the entire list if the indices are both out of range."""
    list_sub: list[int] = [10, 20, 30, 40]
    assert sub(list_sub, -2, 8) == [10, 20, 30, 40]


def test_concat_empty() -> None:
    """Edge case that tests if the function will produce an empty list if it is given two empty lists to concatenate."""
    list_1: list[int] = list()
    list_2: list[int] = list() 
    assert concat(list_1, list_2) == []


def test_concat_single_item() -> None:
    """Use case that tests if the function can concatenate two lists each with a single item."""
    list_1: list[int] = [10]
    list_2: list[int] = [20]
    assert concat(list_1, list_2) == [10, 20]


def test_concat_multiple_items() -> None: 
    """Use case that tests if the function can concatenate two lists each with multiple items."""
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [5, 6, 7, 8]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8]