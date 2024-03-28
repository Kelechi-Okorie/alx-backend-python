#!/usr/bin/env python3
"""Takes a float and returns a function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a multiplier function"""

    def multiplier_function(x: float) -> float:
        """The multiplier function"""

        return x * multiplier
    return multiplier_function
