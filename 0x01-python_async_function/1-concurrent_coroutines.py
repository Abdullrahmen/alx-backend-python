#!/usr/bin/env python3
"""multiple coroutines at the same time"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    lst = []
    cor = tuple(wait_random(max_delay) for i in range(n))
    for res in asyncio.as_completed(cor):
        com = await res
        lst.append(com)
    return lst
