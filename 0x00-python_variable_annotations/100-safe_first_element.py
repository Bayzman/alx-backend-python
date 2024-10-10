#!/usr/bin/env python3

""" Duck typing - first element of a sequence """
from typing import Iterable, Sequence, Any, Union


def safe_first_element(lst: Iterable[Sequence[Any]]) -> Union[Any, None]:
    """ The types of the elements of the input are not known """
    if lst:
        return lst[0]
    else:
        return None
