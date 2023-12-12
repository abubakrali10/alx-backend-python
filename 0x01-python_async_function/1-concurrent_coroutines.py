#!/usr/bin/env python3
"""
This modules creates a function that Asynchronously wait for 'n' random delays
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronously wait for 'n' random delays.

    Args:
    - n (int): The number of delays to wait for.
    - max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    List[float]:
    A list of random floating-point numbers
    representing the durations of the delays.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
