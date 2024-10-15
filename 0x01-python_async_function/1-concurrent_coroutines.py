#!/usr/bin/env python3

""" Returns a list of all the delays """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of all the delays in ascending order without using
        sort()
    """
    delays = [await wait_random(max_delay) for _ in range(n)]

    return sorted(delays)
