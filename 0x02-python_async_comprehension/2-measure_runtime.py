#!/usr/bin/env python3
"""
This module defines a coroutine that measures the total runtime of executing
async_comprehension four times in parallel using asyncio.gather.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
    float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time() - start_time
    return end_time
