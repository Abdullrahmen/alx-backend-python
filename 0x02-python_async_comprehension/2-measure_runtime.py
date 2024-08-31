#!/usr/bin/env python3
"""measure_runtime coroutine"""
import asyncio
from time import time
ac = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it"""
    start = time()
    await asyncio.gather(ac(), ac(), ac(), ac())
    return time() - start
