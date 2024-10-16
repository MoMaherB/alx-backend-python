#!/usr/bin/env python3
"""
Concurrency of 4 Asynchronous Comprehension operations
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    mport async_comprehension from the previous file and write
    a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    Collect 10 random numbers using an async comprehensing,
    then return the 10 random numbers.
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.perf_counter()
    return (end - start)
