#!/usr/bin/env python3
"""Returns sum of list of integers and floats as floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of list of integers and floats as floats"""

    return sum(mxd_lst)
