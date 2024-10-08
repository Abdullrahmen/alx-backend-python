#!/usr/bin/env python3
'''measure_time function module
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    start = time.time()
    res = asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start)/n
