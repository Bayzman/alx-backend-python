#!/usr/bin/env python3

""" Altered wait_n function """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Altered wait_n function """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    tasks = [await task for task in asyncio.as_completed(delays)]

    return tasks
