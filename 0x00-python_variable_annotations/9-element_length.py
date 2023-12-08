#!/usr/bin/env python3
"""
This module provides a function to calc the length of elements in an iterable.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in an iterable.

    Parameters:
    - lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples
    where each tuple contains a sequence
    and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
