#!/usr/bin/env python3
"""Uses random from previous task"""

import asyncio
from typing import List
# from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns wait_random n times
    with the specified max_delay

    Parameters:
        n (int): Number of times to spawn wait_random coroutine.
        max_delay (int): Max delay in seconds

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """

    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
