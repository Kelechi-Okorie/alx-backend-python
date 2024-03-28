#!/usr/bin/env python3

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Annotate the parameters and return values of the element_length function.

    Parameters:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains
            an element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
