#!/usr/bin/env python3
'''Task 4's module.
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    lst = []
    cor = tuple(task_wait_random(max_delay) for i in range(n))
    for res in asyncio.as_completed(cor):
        com = await res
        lst.append(com)
    return lst
