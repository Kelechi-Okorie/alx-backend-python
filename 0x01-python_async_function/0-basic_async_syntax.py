#!/usr/bin/env python3
"""Takes an integer, waits a random amount of time and return it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds and eventually returns it.

    Parameters:
        max_delay (int) :Maximum delay in secods (default is 10);

    Returns:
        float: Random delay in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
