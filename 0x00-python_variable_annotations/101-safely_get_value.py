#!/usr/bin/env python3

""" Duck typing - more involved type annotations """
from typing import Dict, TypeVar, Union, Mapping, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Using TypeVar """
    if key in dct:
        return dct[key]
    else:
        return default
