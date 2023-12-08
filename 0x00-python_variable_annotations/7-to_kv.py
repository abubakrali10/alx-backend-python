#!/usr/bin/env python3
"""
This module provides a function to convert a key-value pair.
"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    Converts a key-value pair.

    Args:
    - k (str): The key.
    - v (Union[int, float]): The value, which can be an integer or a float.

    Returns:
    tuple[str, float]: A tuple containing
    the original key and the square of the value.
    """
    return k, v * v
