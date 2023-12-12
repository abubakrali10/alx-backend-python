#!/usr/bin/env python3
"""
Module for creating an asyncio task for wait_random function.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task for the wait_random function.

    Args:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    asyncio.Task: The asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
