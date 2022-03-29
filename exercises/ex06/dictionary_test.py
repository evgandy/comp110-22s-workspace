"""Unit Testing Dictionary Functions."""

__author__ = "730227972"

from dictionary import invert, favorite_color, count 


# Unit Tests for invert function 


def test_empty_dict() -> None:
    """Checks for an empty dictionary."""
    assert invert({}) == {}


def test_2_items() -> None:
    """Checks that a dictionary of two pairs is properly inverted."""
    assert invert({"i": "am", "so": "tird"}) == {"am": "i", "tired": "so"}


def test_3_items() -> None:
    """Checks that a dictionary of three pairs is properly inverted."""
    assert invert({"no": "seriously", "this": "took", "me": "forever"}) == {"seriously": "no", "took": "this", "forever": "me"}


# Unit Tests for favorite_color function. 


def test_two_favorites() -> None:
    """Checks that the first color encountered is returned as favorite if there is a tie between two colors."""
    assert favorite_color({"Monique": "blue", "Evelyn": "blue", "Josh": "yellow", "Wendy": "yellow"}) == "blue"


def test_three_colors() -> None:
    """Checks that the function can identify the most popular color in a dictionary of three colors."""
    assert favorite_color({"Monique": "blue", "Evelyn": "blue", "Josh": "green"}) == "blue"


def test_four_colors() -> None:
    """Checks that the function can identify the most popular color in a dictionary of four colors."""
    assert favorite_color({"Monique": "blue", "Evelyn": "blue", "Josh": "yellow", "Wendy": "red"}) == "blue"


# Unit Tests for count function. 


def test_empty_list() -> None:
    """Checks that the function will return an empty dictionary if given an empty list."""
    assert count([]) == {}


def test_three_items() -> None:
    """Checks that the function can count the number of each of three items."""
    assert count(["ball", "ball", "basket"]) == {"ball": 2, "basket": 1}


def test_four_items() -> None:
    """Checks that the function can count the number of each of four items."""
    assert count(["ball", "basket", "mj", "mj"]) == {"ball": 1, "basket": 1, "mj": 2}