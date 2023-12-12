#!/usr/bin/env python3
"""
module provides an asynchronous function for waiting a random amount of time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait a random amount of time.

    Args:
    - max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    float: A random floating-point num representing the duration of the delay.
    """
    random_val: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val
