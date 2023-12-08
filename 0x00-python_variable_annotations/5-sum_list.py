#!/usr/bin/env python3
"""
This module provides mathematical operations on lists of floating-point numbers.
"""

from typing import List


def sum_list(sum_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point numbers.

    Args:
    - sum_list (List[float]): The list of floating-point numbers.

    Returns:
    float: The sum of the input list.
    """
    return sum(sum_list)
