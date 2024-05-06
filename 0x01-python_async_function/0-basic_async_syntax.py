#!/usr/bin/env python3
"""this is an async module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """this is the function that waits for a delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
