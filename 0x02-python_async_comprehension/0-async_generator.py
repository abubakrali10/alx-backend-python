#!/usr/bin/env python3
"""
This module defines an asynchronous generator that yields random numbers
between 0 and 10 after waiting for 1 second in each iteration.
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Yields:
    float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
