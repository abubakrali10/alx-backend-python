#!/usr/bin/env python3
"""
This module provides a function to sum a list of mixed integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up the elements of a mixed list containing integers and floats.

    Args:
    - mxd_lst (List[Union[int, float]]): list containing integers and floats.

    Returns:
    float: The sum of the elements in the mixed list.
    """
    return sum(mxd_lst)
