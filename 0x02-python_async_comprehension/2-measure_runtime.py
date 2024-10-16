#!/usr/bin/env python3

""" Measures the total runtime """

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the total runtime """
    start_time = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time()
    total_runtime = end_time - start_time

    return total_runtime
