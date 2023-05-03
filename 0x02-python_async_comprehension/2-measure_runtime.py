#!/usr/bin/env python3
"""Module: 2-measure_runtime"""
import asyncio
from time import perf_counter
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures total runtime of async_comprehension"""
    start_time: float = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = perf_counter()
    return end_time - start_time

