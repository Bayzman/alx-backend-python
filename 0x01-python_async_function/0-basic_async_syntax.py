#!/usr/bin/env python3

""" Asynchronous coroutine that takes in an integer argument and returns it """

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
