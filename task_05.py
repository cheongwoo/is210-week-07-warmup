#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


def flip_keys(to_flip):
    """Reverse the order of the inner sequence

    Args:
        to_flip (list): List that has nested, immutable sequences inside
    Returns:
        list: The original list with its inner elements reversed
    Example:

        >>> flip_keys([(1, 2, 3), 'abc', (4, 5, 6)])
        [(3, 2, 1), 'cba', (6, 5, 4)]
    """
    num = 0
    for seq in to_flip:
        seq[::-1]
        num += 1
        return to_flip
