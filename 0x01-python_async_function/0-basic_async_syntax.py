#!/usr/bin/env python3
"""Basic asynchronous coroutine module"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    time = uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
