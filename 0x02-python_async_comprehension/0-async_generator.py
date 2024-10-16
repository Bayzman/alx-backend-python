#!/usr/bin/env python3

""" A coroutine that takes no arguments """

import asyncio
import random


async def async_generator():
    """ A coroutine that takes no arguments """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
