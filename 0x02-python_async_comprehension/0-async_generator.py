#!/usr/bin/env python3
"""coroutine called async_generator"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.'''
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
