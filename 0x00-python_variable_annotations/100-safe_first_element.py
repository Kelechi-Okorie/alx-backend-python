#!/usr/bin/env
"""Correct duck-type annotation"""

from typing import Union


def safe_first_element(lst: Union[list, tuple]) -> Union[object, None]:
    """
    Annotate the parameters.

    Parameters:
    lst (Unon[list, tuple]) A list or tuple.

    Returns:
        Union[object, None]: The first element of the input list or tuple,
            or None if the input is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
