#!/usr/bin/env python3
"""
Module for measuring the average time it takes to execute wait_n function.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time it takes to execute the wait_n function.

    Args:
    - n (int): The number of delays to wait for.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    float: The average time per wait.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time() - start
    return end / n
