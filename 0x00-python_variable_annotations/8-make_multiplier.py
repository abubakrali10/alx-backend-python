#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Parameters:
    - multiplier (float): The multiplier to be used in the created function.

    Returns:
    Callable[[float], float]: multiplies its input by the given multiplier.
    """
    def multi(num: float) -> float:
        """
        Multiplies a number by the given multiplier.

        Parameters:
        - num (float): The number to be multiplied.

        Returns:
        float: The result of the multiplication.
        """
        return num * multiplier
    return multi
