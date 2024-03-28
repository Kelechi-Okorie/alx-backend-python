#!/usr/bin/env python3
"""To kv function"""

form typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """To kv function"""

    return k, float(v) ** 2
