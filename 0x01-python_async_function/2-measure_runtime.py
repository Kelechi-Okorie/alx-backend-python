#!/usr/bin/env python3
"""Measure the runtime"""

import time
import asyncio
# wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).

    Parameters:
        n (int): Number of times to spawn wait_random coroutine.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average execution time.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
