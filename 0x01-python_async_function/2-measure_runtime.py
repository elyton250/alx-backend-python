#!/usr/bin/env python3
"""this for time measurement"""
import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n, max_delay):
    """this function is the for time meauremen"""
    time_started = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_ended = time.time()
    elap_time = time_ended - time_started
    return elap_time / n
