#!/usr/bin/env python3
"""this for time measurement"""
import asyncio
import time
from typing import Tuple


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """this function is the for time measurement"""
    time_started: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_ended: float = time.time()
    elap_time: float = time_ended - time_started
    return elap_time / n
