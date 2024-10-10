#!/usr/bin/env python3

""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that is multiplied by multiplier """

    def float_fn(n: float) -> float:
        """ multiplies multiplier by a float n """
        return (n * multiplier)

    return float_fn
