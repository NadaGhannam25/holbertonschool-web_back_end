#!/usr/bin/env python3
"""Module that provides a function to create a key-value tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string and the square of the number as float."""
    return (k, float(v * v))
