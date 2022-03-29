"""Writing dictionary functions for Unit Testing."""

__author__ = "730227972"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    result: dict[str, str] = dict()
    count: int = 0
    for key in input:
        if input[key] in input:
            count += 1
            if count > 1:
                raise KeyError("sorry you have a duplicate!") 
                exit
        result[input[key]] = key 
    return result


def favorite_color(names_colors: dict[str, str]) -> str:
    """Identifying the most common color."""
    list_colors: list[str] = []
    dict_colors: dict[str, int] = {}
    list_numbers: list[int] = []
    for name in names_colors:
        list_colors.append(names_colors[name])
    for color in list_colors:
        if color in dict_colors:
            dict_colors[color] += 1
        else:
            dict_colors[color] = 1
    for colors in dict_colors:
        list_numbers.append(dict_colors[colors])
    maximum: int = max(list_numbers)
    switch_numbers_colors: dict[int, str] = {}
    for colors in dict_colors:
        switch_numbers_colors[dict_colors[colors]] = colors
    return switch_numbers_colors[maximum]
    

def count(color_list: list[str]) -> dict[str, int]:
    """Counting how many times a color is mentioned in a list."""
    counts_of_colors: dict[str, int] = {}
    for x in color_list:
        if x in counts_of_colors:
            counts_of_colors[x] += 1
        else:
            counts_of_colors[x] = 1
    return counts_of_colors