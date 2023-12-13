#!/usr/bin/env python3
"""
async comprehension
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    Returns:
    List[float]: List of 10 random numbers.

    Raises:
    None
    """
    return [rand_num async for rand_num in async_generator()]
