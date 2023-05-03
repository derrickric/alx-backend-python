#!/usr/bin/env python3
"""Module: 0-main"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values() -> None:
    """Coroutine that prints the values yielded by async_generator"""
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    print(result)


asyncio.run(print_yielded_values())

