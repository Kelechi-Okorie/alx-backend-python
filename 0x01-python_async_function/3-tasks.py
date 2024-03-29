#!/usr/bin/env python3
"""File for 3 tasks"""

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task[float]:
    """
    Creates an asyncio.Task for wait_random coroutine.

    Parameters:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task[float]: A task representing the execution
    """

    return asyncio.create_task(wait_random(max_delay))
